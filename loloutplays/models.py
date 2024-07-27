from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.


class LoloutplaysStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='video/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('loloutplays:story-detail', args=[self.id])


class Comment(models.Model):
    story = models.ForeignKey(LoloutplaysStory, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.story)

# class LoloutplaysStory:
#     def __init__(self, id, title, author, description, video, date_posted, comments):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.description = description
#         self.video = video
#         self.date_posted = date_posted
#         self.comments = comments
#
#
# story1 = LoloutplaysStory(
#     1,
#     "Master Yi Easy Pentakill",
#     "jimmychiu",
#     "",
#     "video/video1.webm",
#     datetime.now(),
#     ["No comment"]
# )
#
# story2 = LoloutplaysStory(
#     2,
#     "Irelia Insane Escape",
#     "ripkobebryant",
#     "",
#     "video/video2.webm",
#     datetime.now(),
#     ["No comment"]
# )
#
# story3 = LoloutplaysStory(
#     3,
#     "Jayce Pentakill",
#     "gimmemoney",
#     "",
#     "video/video3.webm",
#     datetime.now(),
#     ["aaronwang: This is awesome!"]
# )
#
# story4 = LoloutplaysStory(
#     4,
#     "Yone Insane Ult",
#     "opopop666",
#     "I am incredible haha haha haha haha haha haha haha haha haha haha haha haha haha haha haha ",
#     "video/video4.webm",
#     datetime.now(),
#     ["No comment"]
# )
#
# story5 = LoloutplaysStory(
#     5,
#     "Vayne Amazing Backdoor",
#     "aaronwang",
#     "",
#     "video/video5.webm",
#     datetime.now(),
#     ["asiagodtone: Easy peasy"]
# )
#
# story6 = LoloutplaysStory(
#     6,
#     "Lee Sin Ult Four",
#     "yuanthonyu",
#     "",
#     "video/video6.webm",
#     datetime.now(),
#     ["No comment"]
# )
#
# loloutplays_stories = [
#     story1,
#     story2,
#     story3,
#     story4,
#     story5,
#     story6,
# ]

regular_user = {"username": "jimmychiu", "password": "password"}
admin = {"username": "admin", "password": "iamadmin"}