from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from actions.models import Action


# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        user = authenticate(username=username, password=password)
        user.details.gender = gender
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            request.session['role'] = user.details.role
            messages.add_message(request, messages.SUCCESS,
                                 "You successfully registered with the username: %s" % user.username)
            return redirect("loloutplays:loloutplay_home")
    return render(request,
                  "users/user/register.html",
                  )


def profile(request, username):
    user = get_object_or_404(User, username=username)
    actions = Action.objects.all().order_by('-created')
    user_actions = [action for action in actions if action.user.username == user.username]
    return render(request,
                  "users/user/profile.html",
                  {"user": user, "actions": user_actions},
                  )


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect("loloutplays:loloutplays_story_list")


def logout_user(request):
    del request.session['username']
    del request.session['role']
    logout(request)
    return redirect("loloutplays:loloutplay_home")


def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.password = make_password(password)
        user.save()
        if request.session['username'] != username:
            messages.add_message(request, messages.SUCCESS, "The profile was successfully updated.")
        else:
            messages.add_message(request, messages.SUCCESS, "Your profile was successfully updated.")
        return render(request, "users/user/profile.html", {"user": user})
    return redirect("loloutplays:loloutplay_home")


def edit_role(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        role = request.POST.get("user-role")
        if user.details.role == 'admin' and user.username == request.session['username'] and role == 'regular':
            request.session['role'] = 'regular'
        user.details.role = role
        user.save()
        messages.add_message(request, messages.SUCCESS, "The role was successfully updated.")
        return render(request, "users/user/profile.html", {"user": user})
    return redirect("loloutplays:loloutplay_home")
