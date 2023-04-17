from django.db import models
from django.contrib.auth import get_user_model
from .dateAndTime import BaseDateTime


User = get_user_model()




class BaseQuestion(BaseDateTime,models.Model):

    """# Base Question 
    
    ## required related names 
    
    * user > author id
    
    * subject > question subject 
    
    """
    
    title               = models.CharField(max_length=200)
    content             = models.TextField(max_length=3000)
    tags                = models.CharField(max_length=100)


    
    def __str__(self) -> str:
        return self.title if self.title is not None else "No title " + str(self.id)

    def get_tags(self):
        tags = []
        for tag in self.tags.split(","):
            tags.append("#",tag)

        return tags


    class Meta:
        abstract = True

class BaseQuestionAnswer(BaseDateTime,models.Model):
    
    text                = models.TextField(max_length=5000)

    
    
    class Meta:
        abstract = True


class BaseQuestionVote(BaseDateTime,models.Model):
    
    """Vote

        read the comment above 
    """
    vote                = models.BooleanField(blank=True,null=True,default=True)


    class Meta:
        abstract = True



class BaseQuestionComment(BaseDateTime,models.Model):

    """Comment

        Since each question has many answers the comment was created to ask user to edit his question or add more details 
        To keep ever object sperate and organized 

    """
    text                = models.TextField(max_length=500)


    
    def __str__(self) -> str:
        return self.text


class BaseCommentReply(BaseDateTime,models.Model):
    
    text                = models.TextField(max_length=500)

    
    def __str__(self) -> str:
        return self.text
    

