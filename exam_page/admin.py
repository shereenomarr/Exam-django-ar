from django.contrib import admin
from .models import exam
from .models import question
from .models import answer
# Register your models here.
#exam model
admin.site.register(exam)
#question model
admin.site.register(question)
# answer model
admin.site.register(answer)