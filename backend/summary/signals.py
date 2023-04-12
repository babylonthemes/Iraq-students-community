from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Summary,SummaryComment,SummaryTimeline,TimelineEvent,CommentReply


@receiver(post_save, sender=Summary)
def summary_adn_timeline(sender,instance,created,**kwargs):
    if created:
        timeline = SummaryTimeline.objects.create(
            summary=instance
        )
        
        timeline.save()
        
        event = TimelineEvent.objects.create(
            user=instance.author,
            timeline=timeline,
            caption=f" قام {instance.author.first_name +' ' + instance.author.last_name} بأنشاء ملخص جديد ",
            eventRelated="SUMMARY",
            eventMethod="S_ADD",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&id={instance.id}"
        )
        
        
        event.save()
        
    
    else:
        timeline = SummaryTimeline.objects.get_or_create(summary=instance)[0]
        event = TimelineEvent.objects.create(
            user=instance.author,
            timeline=timeline,
            caption=f" قام {instance.author.first_name +' ' + instance.author.last_name} بتعديل  الملخص {instance.title} ",
            eventRelated="SUMMARY",
            eventMethod="S_EDIT",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&id={instance.id}"
        )
        event.save()
        



@receiver(post_save, sender=SummaryComment)
def comment(sender,instance,created,**kwargs):
    if created:
        timeline = SummaryTimeline.objects.get_or_create(summary=instance.summary)[0]
        
        event = TimelineEvent.objects.create(
            user=instance.user,
            timeline=timeline,
            caption=f" قام {instance.user.first_name +' ' + instance.user.last_name}   بأضافة تعليق جديد على الملخص  {instance.summary.title} ",
            eventRelated="COMMENT",
            eventMethod="C_ADD",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&summaryId={instance.id}&commentId={instance.id}"
        )
        
        
        event.save()
        
    
    else:
        timeline = SummaryTimeline.objects.get_or_create(summary=instance)[0]
        event = TimelineEvent.objects.create(
            user=instance.user,
            timeline=timeline,
            caption=f" قام {instance.user.first_name +' ' + instance.user.last_name} بتعديل تعليقه على الملخص {instance.summary.title} ",
            eventRelated="COMMENT",
            eventMethod="C_EDIT",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&summaryId={instance.summary.id}&commentId={instance.id}"
        )
        event.save()





@receiver(post_save, sender=SummaryComment)
def reply(sender,instance,created,**kwargs):
    if created:
        timeline = SummaryTimeline.objects.get_or_create(summary=instance.summary)[0]
        
        event = TimelineEvent.objects.create(
            user=instance.user,
            timeline=timeline,
            caption=f" قام {instance.user.first_name +' ' + instance.user.last_name}   بأضافة رد  جديد على التعليق  {instance.comment.text} ",
            eventRelated="REPLY",
            eventMethod="R_ADD",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&summaryId={instance.id}&commentId={instance.comment.id},&replyId={instance.id}"
        )
        
        
        event.save()
        
    
    else:
        timeline = SummaryTimeline.objects.get_or_create(summary=instance)[0]
        event = TimelineEvent.objects.create(
            user=instance.user,
            timeline=timeline,
            caption=f" قام {instance.user.first_name +' ' + instance.user.last_name} بتعديل رده  على التعليق {instance.comment.text} ",
            eventRelated="REPLY",
            eventMethod="R_EDIT",
            url=f"http://localhost:3000/summaries/subject={instance.subject.name}&summaryId={instance.id}&commentId={instance.comment.id},&replyId={instance.id}"
        )
        event.save()

