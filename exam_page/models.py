from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#user = models.ForeignKey(User, on_delete=models.CASCADE)




class exam(models.Model):
    exam_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    number_of_questions=models.IntegerField()
    pass_score=models.IntegerField()
    duration=models.IntegerField()
    created_at=models.DateField(default=timezone.now)
    deleted_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    #updated_by=models.ForeignKey(User,on_delete=models.CASCADE)
    #deleted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    is_deleted=models.IntegerField()
    ip_address=models.GenericIPAddressField()
    def __str__(self):
       return self.name    

class question(models.Model):
    question_id=models.AutoField(primary_key=True)
    exam_id=models.ForeignKey(exam,on_delete=models.CASCADE)
    question_body=models.CharField(max_length=300)
    question_type=models.CharField(max_length=50)
    created_at=models.DateField(default=timezone.now)
    deleted_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    is_deleted=models.IntegerField()
    ip_address=models.GenericIPAddressField()
    

class answer(models.Model):
    answer_id=models.AutoField(primary_key=True)
    question_id=models.ForeignKey(question,on_delete=models.CASCADE)
    answer_body=models.CharField(max_length=300)
    is_correct=models.CharField(max_length=50)
    created_at=models.DateField(default=timezone.now)
    deleted_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    is_deleted=models.IntegerField()
    ip_address=models.GenericIPAddressField()
   



    