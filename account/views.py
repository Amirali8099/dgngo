from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


def register_page(request):
    login_form = LoginForm()

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)

        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            first_name = register_form.cleaned_data['first_name']
            password = register_form.cleaned_data['password']

            if User.objects.filter(email__iexact=email).exists():
                register_form.add_error('email', 'این ایمیل قبلاً ثبت شده است')
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=first_name,
                    password=password,
                )
                login(request, user)
                return redirect('home')
    else:
        register_form = RegistrationForm()

    context = {
        'register_form': register_form,
        'login_form': login_form,
        'active_tab': 'register',
    }
    return render(request, 'account/login_register.html', context)


def login_page(request):
    register_form = RegistrationForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                login_form.add_error(None, 'ایمیل یا رمز عبور اشتباه است')
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active_tab': 'login',
    }
    return render(request, 'account/login_register.html', context)


def logout_page(request):
    logout(request)
    return redirect('login_page')


# Create your views here.
