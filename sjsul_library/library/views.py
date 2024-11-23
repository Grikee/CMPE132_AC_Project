from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import LibraryUserCreationForm
from .models import Role, LibraryUser
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')

# Register view for creating new users (with role assignment)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create LibraryUser instance after saving user
            role = Role.objects.first()  # Or assign a default role
            LibraryUser.objects.create(user=user, role=role)
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                
                # Ensure the LibraryUser object exists
                library_user, created = LibraryUser.objects.get_or_create(user=user)
                
                # Debugging print statements
                print(f"User: {user.username}, Role: {library_user.role}")
                
                # Role-based redirection
                if library_user.role == 'Member':
                    return redirect('member_dashboard')
                elif library_user.role == 'Librarian':
                    return redirect('librarian_dashboard')
                elif library_user.role == 'Administrator':
                    return redirect('admin_dashboard')
                else:
                    # If role is not defined, redirect to a default page
                    return redirect('home')  # Adjust 'home' to a relevant URL
            else:
                # Handle invalid credentials
                form.add_error(None, "Invalid username or password")
        else:
            # Handle form errors
            form.add_error(None, "Form is invalid.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Logout view to log out the user
def logout_user(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user first
            # Create a LibraryUser and assign a default role
            library_user = LibraryUser.objects.create(user=user, role='Member')
            library_user.save()  # Save the LibraryUser instance
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def profile_view(request):
    # your logic for displaying user profile
    return render(request, 'profile.html')

# Role-based views
def member_dashboard(request):
    if request.user.libraryuser.role != 'Member':
        return redirect('unauthorized')  # Redirect unauthorized users
    return render(request, 'member_dashboard.html')
    
def librarian_dashboard(request):
    if request.user.libraryuser.role != 'Librarian':
        return redirect('unauthorized')
    return render(request, 'librarian_dashboard.html')

def admin_dashboard(request):
    if request.user.libraryuser.role != 'Administrator':
        return redirect('unauthorized')
    return render(request, 'admin_dashboard.html')

def unauthorized(request):
    return render(request, 'unauthorized.html')