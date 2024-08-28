from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .utils import login_required_redirect
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

@login_required_redirect
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Use 'username' because it's now set to email
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to the index page after successful login
            else:
                form.add_error(None, 'Invalid email or password')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
