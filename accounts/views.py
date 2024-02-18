from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('profile')  # Redirect to dashboard after registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profilePage')  # Redirect to the 'profilePage' URL pattern
        else:
            error_message = 'Invalid username or password'
            return render(request, 'accounts/login.html', {'form': AuthenticationForm(), 'error_message': error_message})
    else:
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})

def profilePage(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    # Redirect to some page after logout, for example, the login page
    return redirect('loginPage')



