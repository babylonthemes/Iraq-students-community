from django.contrib import admin
from .models import Summary,SummaryComment,SummaryTimeline,TimelineEvent,CommentReply

admin.site.register(Summary)
admin.site.register(SummaryComment)
admin.site.register(SummaryTimeline)
admin.site.register(TimelineEvent)
admin.site.register(CommentReply)

