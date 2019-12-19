from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.db.models import Q
from articles.models import Comment

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # Option 1: Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in!')
                    return redirect('/')

                    # # Option 2: Don't log in immediately, redirect to log in page instead
                    # user.save()
                    # messages.success(
                    #     request, 'You are now registered and can log in')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        # Logout User
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('/')
    return render(request, 'logout.html')


def dashboard(request):
    users_comments = Comment.objects.filter(
        Q(user__username__icontains=request.user.username)).order_by('-timestamp')

    context = {
        'comments': users_comments
    }
    return render(request, 'dashboard.html', context)
