from django.db import models
from django.contrib.auth import get_user_model
from subject.models import Subject

User = get_user_model()


class Summary(models.Model):
    PRIVACE_SETS = (
        ("public","Public"),
        ("private","Private")
    )
    author              = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='userSummaries')
    subject             = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,related_name='subjectSummaries')
    title               = models.CharField(max_length=150)
    content             = models.JSONField(default={})
    privace             = models.CharField(max_length=30,choices=PRIVACE_SETS)
    collabs             = models.ManyToManyField(User,related_name='user_collabs')
    shares              = models.IntegerField(default=0)
    subject             = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    description         = models.TextField(max_length=1000)


    def __str__(self) -> str:
        return self.title


class SummaryComment(models.Model):
    summary             = models.ForeignKey(Summary,on_delete=models.CASCADE,related_name='summaryComments')
    user                = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='userComments')
    text                = models.TextField(max_length=500)
    date                = models.DateField()
    time                = models.TimeField()

    
    def __str__(self) -> str:
        return self.text

class CommentReply(models.Model):
    comment = models.ForeignKey(SummaryComment,on_delete=models.CASCADE,related_name='commentReply')
    summary             = models.ForeignKey(Summary,on_delete=models.CASCADE)
    user                = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    text                = models.TextField(max_length=500)
    date                = models.DateField()
    time                = models.TimeField()
    
    def __str__(self) -> str:
        return self.text

class SummaryTimeline(models.Model):
    summary             = models.OneToOneField(Summary,on_delete=models.CASCADE,related_name='summaryTimline')
    date                = models.DateField(auto_now=True)
    time                = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.summary.title

class TimelineEvent(models.Model):
    
    EVENT_RELATED = (
        ("COMMENT","Comment"),
        ("SUMMARY","Summary"),
        ("REPLY","Reply")
    )
    EVENT_METHOD = (
        # Comment
        ("C_ADD","Add Comment"),
        ("C_EDIT","Edit Comment"),
        ("C_DELETE","Delete Comment"),
        # Summary
        ("S_ADD","Add Summary"),
        ("S_EDIT","Edit Summary"),
        ("S_DELETE","Delete Summary"),
        # Reply
        ("R_ADD","Add Reply"),
        ("R_EDIT","Edit Reply"),
        ("R_DELETE","Delete Reply")
        
    )
    user                = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    timeline            = models.ForeignKey(SummaryTimeline,on_delete=models.PROTECT,related_name='timelineEvents')
    caption             = models.CharField(max_length=200)
    eventRelated        = models.CharField(max_length=10,choices=EVENT_RELATED)
    eventMethod         = models.CharField(max_length=10,choices=EVENT_METHOD)
    url                 = models.URLField(max_length=300,null=True,blank=True)
    date                = models.DateField(auto_now=True)
    time                = models.TimeField(auto_now=True)   
    

    def __str__(self) -> str:
        return self.caption.replace("($)",self.user.first_name + ' ' + self.user.last_name)
