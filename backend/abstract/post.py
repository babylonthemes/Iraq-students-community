from django.db import models
from django.contrib.auth import get_user_model
from .dateAndTime import BaseDateTime

User = get_user_model()

class BasePost(BaseDateTime,models.Model):

    """Post

    
    # Database fields 
    
    thumbnail : ImageField > post thumbnail
    title : CharField : string  > post title 
    content : TextField : String > post content 
    tags : CharField : string > post tags separated by , [after formating and separating the tags , (#) will be added in the start of the word (example : "#code" ) ]

    > date : DateField  datetime : publishing date & default=datetime.now()
    
    > time : TimeField datetime : publishing time & default=datetime.now()
    
    ! see https://docs.python.org/3/library/datetime.html for [ date & time fields ]
    
    ! see https://docs.djangoproject.com/en/4.2/topics/db/models/ for [ django fields such as (CharField,DateField,ForeignField,...etc) ]
    
    """
    uploadTo            = "abstract/posts/%Y/%m/%d"
    thumbnail           = models.ImageField(upload_to=uploadTo)
    title               = models.CharField(max_length=200)
    content             = models.TextField(max_length=3000)
    tags                = models.CharField(max_length=100)



    class Meta:
        abstract = True
        


class BasePostComment(BaseDateTime,models.Model):

    """# Post omment
    

        
        ## Database fields 
                
        > text : TextField : string > comment text
        
        > date : DateField  datetime : publishing date & default=datetime.now()
        
        > time : TimeField datetime : publishing time & default=datetime.now()
        
        ! see https://docs.python.org/3/library/datetime.html for [ date & time fields ]
        
        ! see https://docs.djangoproject.com/en/4.2/topics/db/models/ for [ django fields such as (CharField,DateField,ForeignField,...etc) ]

    """

    text                = models.TextField(max_length=1000)


    
    def __str__(self) -> str:
        return self.text


