from django.db import models
from django.utils import timezone
from django.conf import settings

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    dt          = models.DateTimeField(verbose_name="投稿日",default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE,related_name="posted_user")
    comment     = models.CharField(verbose_name="コメント",max_length=200)

    good        = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="良いね",through="GoodTopic",related_name="posted_good",null=True,blank=True)
    bad         = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="悪いね",through="BadTopic",related_name="posted_bad",null=True,blank=True)

    def __str__(self):
        return self.comment

class GoodTopic(models.Model):

    class Meta:
        db_table = "good_topic"

    dt          = models.DateTimeField(verbose_name="良いねした時刻",default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="良いねしたユーザー",on_delete=models.CASCADE)
    target      = models.ForeignKey(Topic,verbose_name="良いねしたトピック",on_delete=models.CASCADE)

    def __str__(self):
        return self.target.comment

class BadTopic(models.Model):

    class Meta:
        db_table = "bad_topic"

    dt          = models.DateTimeField(verbose_name="悪いねした時刻",default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="悪いねしたユーザー",on_delete=models.CASCADE)
    target      = models.ForeignKey(Topic,verbose_name="悪いねしたトピック",on_delete=models.CASCADE)

    def __str__(self):
        return self.target.comment





"""
class Message(models.Model):

    class Meta:
        db_table = "message"

    dt          = models.DateTimeField(verbose_name="作成日",default=timezone.now)
    from_user   = models.ForeignKey(,verbose_name="送信元",on_delete=models.CASCADE)
    content     = models.CharField(verbose_name="内容",max_length=200)

    to_user     = models.ManyToManyField(ToUser,verbose_name="宛先")
    tags        = models.ManyToManyField(Tag,verbose_name="タグ")

    def __str__(self):
        return self.content

"""
