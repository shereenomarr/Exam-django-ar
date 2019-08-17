from django.shortcuts import render,redirect
from .forms import usercreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form=usercreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'congratulation{username} Registrarion was successful')
            return redirect('home')


    else:
            form= usercreationForm()
    return render (request,'user/register.html',{
                'titile':'sign in',
                 'form':form,
                  })
