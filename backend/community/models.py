from django.db import models
from django.contrib.auth import get_user_model
from abstract.question import BaseQuestion,BaseQuestionComment,BaseCommentReply,BaseQuestionVote,BaseQuestionAnswer
User = get_user_model()

appname = "community_"



class CommunityQuestion(BaseQuestion,models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='community_user_questions')
    subject = models.ForeignKey('subject.Subject',on_delete=models.SET_NULL,null=True,blank=False,related_name='community_subject_questions')


    
class CommunityQuestionAnswer(BaseQuestionAnswer,models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='community_user_questions_answers')
    question = models.ForeignKey(CommunityQuestion,on_delete=models.CASCADE,related_name='community_question_answers')

    
class CommunityQuestionVote(BaseQuestionVote,models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='community_user_votes')
    question = models.ForeignKey(CommunityQuestion,on_delete=models.CASCADE,related_name='community_question_votes')


class CommunityQuestionComment(BaseQuestionComment,models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='community_user_comments')
    question = models.ForeignKey(CommunityQuestion,on_delete=models.CASCADE,related_name='community_question_comments')


class CommunityCommentReply(BaseCommentReply,models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='community_user_replies')
    question = models.ForeignKey(CommunityQuestion,on_delete=models.CASCADE,related_name='community_question_replies')


# Posts 