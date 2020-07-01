from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from .forms import UserForm


# class ChangeForm(forms.Form):
#     username = forms.CharField(label='UserName')
#     password = forms.CharField(label='Old Password', widget=forms.PasswordInput())
#     password = forms.CharField(label='New Password', widget=forms.PasswordInput())


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username)
            if user:
                info = 'This UserName has been registered'
            elif len(user) == 0:
                info = 'Registration successful'
                user = User(username=username, password=password)
                user.save()

            return HttpResponse(info)

    else:
        form = UserForm()

    return render(request, 'html/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username)
            if user:
                password = User.objects.filter(username=username, password=password)
                if password:
                    info = 'Login successful'
                    return HttpResponse(info)
                else:
                    info = 'Please check your password'
            elif len(user) == 0:
                info = 'Please check your username'

            return HttpResponse(info)
    else:
        form = UserForm()

    return render(request, 'html/login.html', {'form': form})


# def change_password(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             old_password = form.cleaned_data['oldPassword']
#             new_password = form.cleaned_data['newPassword']
#
#             user = User.objects.filter(username=username)
#             if user:
#                 password = User.objects.filter(username=username, password=old_password)
#                 if password:
#                     User.objects.filter(username=username, password=old_password).Update(password=new_password)
#                     info = 'Successfully update password'
#                 else:
#                     info = 'Your input password is not correct'
#             elif len(user) == 0:
#                 info = 'Your input username is not existence'
#
#             return HttpResponse(info)
#     else:
#         form = ChangeForm()
#
#     return render(request, 'html/ChangePassword.html', {'form': form})




