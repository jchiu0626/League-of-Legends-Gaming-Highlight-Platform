from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import regular_user, admin, LoloutplaysStory, User, Comment
from datetime import datetime
from actions.models import Action

# Create your views here.


def loloutplay_home(request):
    if request.session.get("username", False):
        actions = Action.objects.all().order_by('-created')
        return render(request,
               "loloutplays/loloutplays_story/dashboard.html",
                      {"actions": actions},
                      )
    else:
        loloutplays_stories = LoloutplaysStory.objects.all()
        return render(request,
               "loloutplays/loloutplays_story/home.html",
                      {"stories": loloutplays_stories},
                      )


def loloutplay_story_list(request):
    sort = request.GET.get('sort', '-date_posted')
    loloutplays_stories = LoloutplaysStory.objects.all().order_by(sort)
    return render(request,
           "loloutplays/loloutplays_story/list.html",
                  { "stories": loloutplays_stories }
                  )


def loloutplay_story_detail(request, story_id):
    story = get_object_or_404(LoloutplaysStory, id=story_id)
    comments = story.comments.all().order_by('-date_posted')
    return render(request, "loloutplays/loloutplays_story/detail.html",
                  {"story": story, "comments": comments}
                  )


def add_story(request):
    loloutplays_stories = LoloutplaysStory.objects.all()
    if request.method == "GET":
        return render(request, "loloutplays/loloutplays_story/add.html")
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        role = request.POST.get("role")
        user = User.objects.get(username=request.session.get("username"))
        new_story = LoloutplaysStory(
            title=title,
            author=request.session.get("username"),
            user=user,
            description=description,
            video=file,
            comments=None)
        new_story.save()
        # log the action
        action = Action(
            user=user,
            verb="uploaded a new highlight",
            target=new_story,
        )
        action.save()
        messages.add_message(request, messages.SUCCESS, "You successfully uploaded your outplay: %s" % new_story.title)
        return render(request, "loloutplays/loloutplays_story/detail.html", {"story": new_story})


def edit_story(request, story_id):
    loloutplays_stories = LoloutplaysStory.objects.all()
    if not request.session.get('username'):
        return redirect('loloutplays:login')
    for story in loloutplays_stories:
        if story.id == story_id:
            if request.method == 'GET':
                return render(request, 'loloutplays/loloutplays_story/edit.html', {'story': story})

            elif request.method == 'POST':
                title = request.POST.get('title')
                description = request.POST.get('description')
                video = request.FILES.get('video')
                story.title = title
                story.description = description
                user = User.objects.get(username=request.session.get("username"))
                if video:  # only update video if a new file was uploaded
                    story.video = video
                story.date_posted = datetime.now()
                story.save()
                action = Action(
                    user=user,
                    verb="edited a highlight",
                    target=story,
                )
                action.save()
                messages.add_message(request, messages.INFO, "You successfully edited your outplay: %s" % story.title)
                return redirect('loloutplays:story-detail', story_id=story.id)


def delete_story(request, story_id):
    loloutplays_stories = LoloutplaysStory.objects.all()
    for story in loloutplays_stories:
        if story.id == story_id:
            title = story.title
            story.delete()
            user = User.objects.get(username=request.session.get("username"))
            action = Action(
                user=user,
                verb="deleted a highlight",
            )
            action.save()
            messages.add_message(request, messages.WARNING, "You successfully deleted the outplay: %s" % title)
            return redirect('loloutplays:loloutplays_story_list')


def add_comment(request, story_id):
    if request.method == 'POST':
        if 'username' in request.session:
            username = request.session['username']
            user = User.objects.get(username=username)

            story = get_object_or_404(LoloutplaysStory, id=story_id)
            comment_text = request.POST.get('text')
            Comment.objects.create(story=story, author=user, text=comment_text)
            action = Action(
                user=user,
                verb="comment on a highlight",
                target=story,
            )
            action.save()
            return redirect('loloutplays:story-detail', story_id=story.id)
    return redirect('loloutplays:story-detail', story_id=story_id)


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    story = get_object_or_404(LoloutplaysStory, id=comment.story.id)
    if request.method == 'POST':
        comment_text = request.POST.get('text')
        comment.text = comment_text
        comment.save()
        user = User.objects.get(username=request.session.get("username"))
        action = Action(
            user=user,
            verb="edited their comment on a highlight",
            target=story,
        )
        action.save()
        return redirect('loloutplays:story-detail', story_id=comment.story.id)
    return render(request, 'loloutplays/loloutplays_story/edit_comment.html', {'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    story = get_object_or_404(LoloutplaysStory, id=comment.story.id)
    if request.method == 'POST':
        story_id = comment.story.id
        comment.delete()
        user = User.objects.get(username=request.session.get("username"))
        action = Action(
            user=user,
            verb="deleted a comment on a highlight",
            target=story,
        )
        action.save()
        return redirect('loloutplays:story-detail', story_id=story_id)
