from django.db import models

class BaseDate(models.Model):

    autoNow             = True
    autoNowAdd          = True
    date                = models.DateField(auto_now=autoNow,auto_now_add=autoNowAdd)

    class Meta:
        abstract = True


class BaseTime(models.Model):

    autoNow             = True
    autoNowAdd          = True
    time                = models.TimeField(auto_now=autoNow,auto_now_add=autoNowAdd)

    class Meta:
        abstract = True


class BaseDateTime(models.Model):

    autoNow             = True
    autoNowAdd          = True
    date                = models.DateField(auto_now=autoNow,auto_now_add=autoNowAdd)
    time                = models.TimeField(auto_now=autoNow,auto_now_add=autoNowAdd)
    class Meta:
        abstract = True


class BaseDateAndTime(models.Model):

    autoNow             = True
    autoNowAdd          = True
    date                = models.DateTimeField(auto_now=autoNow,auto_now_add=autoNowAdd)
    class Meta:
        abstract = True