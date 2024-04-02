from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import StudentForm,LoginForm
from django.db import connection
from django.contrib.auth.hashers import check_password
from . models import Student


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = 'Data updated successfully'
            return render(request, 'joining_form.html', {'message': msg}) 
    else:
        form = StudentForm()
        return render(request, 'joining_form.html', {'form': form})
    return render(request, 'joining_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print("Username entered:", username)
            print("Password entered:", password)

            # Query the database to retrieve user data
            with connection.cursor() as cursor:
                cursor.execute("SELECT username, password FROM student_login.login_page_student WHERE username = %s", [username])
                row = cursor.fetchone()

            if row:
                db_username, hashed_password_from_db = row
                print("Username from database:", db_username)
                print("Hashed password from database:", hashed_password_from_db)

                # Validate username and password
                if username == db_username and password == hashed_password_from_db:
                    
                    print("Authentication successful")
                    return render(request, 'welcome.html')
                else:
                   
                    print("Authentication failed: Invalid username or password")
                    error = 'Invalid username or password' 
            else:
                
                print("User not found")
                error = 'User not found'
        else:
            
            print("Form is not valid")
            error = 'Invalid form data'
    else:
        form = LoginForm()
        error = None

    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    
    return redirect('login')
