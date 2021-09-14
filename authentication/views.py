from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect


User = get_user_model()


def signup(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        email = request.POST['email'].strip()

        if not username:
            errors['username'] = "Username Field is Required!"
        elif len(username) <= 7:
            errors['username'] = "Username must have a length of at least 8 characters!"
        else:
            is_used = User.objects.filter(username=username).exists()
            if is_used:
                errors['username'] = "This Username is already taken!"

        if not password1:
            errors['password1'] = "Password1 is Required!"
        elif len(password1) <= 7:
            errors['password1'] = "Password must have a length of at least 8 characters!"
        if not password2:
            errors['password2'] = "Password2 is Required!"
        if password1 and password2 and password1 != password2:
            errors['password1'] = "Passwords Do not Match!!!"

        if not email:
            errors['email'] = "Email Field is Required!"
        else:
            is_used = User.objects.filter(email=email).exists()
            if is_used:
                errors['email'] = "This Email is already taken!"

        if not first_name:
            errors['first_name'] = "First Name Field is Required!"
        is_valid = len(errors.keys()) == 0
        if is_valid:
            # create user!
            user = User.objects.create_user(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password1
            )
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('/?signup=successful')
    context = {
        'errors': errors
    }
    return render(request, 'signup.html', context)


