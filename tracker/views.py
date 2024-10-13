from django.shortcuts import render, redirect
from .models import FoodEntry
from .forms import FoodEntryForm, UserSignupForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout


#Create your views here.

# User signup view
def signup(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'signupform': form}
    return render(request, 'signup.html', context = context)

# User login view
def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request, username=username, password=password)
             if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        messages.error(request, 'Invalid username or password')
    context = {'loginform':form}
    return render(request, 'login.html', context=context)

# Home view
def home(request):
    return render(request, 'home.html')


# Dashboard view
@login_required(login_url = 'login')
def dashboard(request):
    breakfast_form = FoodEntryForm()
    lunch_form = FoodEntryForm()
    supper_form = FoodEntryForm()
    food_entries = FoodEntry.objects.filter(user=request.user)
    total_calories = sum(entry.calories for entry in food_entries)
    context = {
        'breakfast_form': breakfast_form,
        'lunch_form': lunch_form,
        'supper_form': supper_form,
        'food_entries': food_entries,
        'total_calories': total_calories,
    }
    return render(request, 'dashboard.html', context)

# Add food view
@login_required(login_url = 'login')
def add_food(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user  
            food_entry.meal_type = request.POST.get('meal_type') 
            food_entry.save()
            return redirect('dashboard')
    else:
        form = FoodEntryForm()
    return render(request, 'add_food.html', {'form': form})
   

# Remove food view
@login_required(login_url = 'login')
def remove_food(request, food_id):
    food_entry = FoodEntry.objects.get(id=food_id, user=request.user)
    food_entry.delete()
    return redirect('dashboard')

#Reset calories view
@login_required(login_url = 'login')
def reset_calories(request):
    calorie_tracker = FoodEntry.objects.get(user=request.user) 
    calorie_tracker.calories = 0
    calorie_tracker.save()
    return redirect('dashboard')

# User logout view
def logout(request):
    auth_logout(request)
    return redirect('login')