from django.shortcuts import render, redirect
from .models import Planting, Reward, TreeType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(request, 'clicker/home.html')

@login_required
def click_plant(request):
    tree_type = TreeType.objects.first() 

    # Registra la plantación
    Planting.objects.create(user=request.user, tree_type=tree_type)

    # Verifica y otorga recompensas
    user_plantings = Planting.objects.filter(user=request.user).count()
    unlocked_rewards = Reward.objects.filter(required_plantings__lte=user_plantings, tree_type=tree_type)
    for reward in unlocked_rewards:
        reward.unlocked_by.add(request.user)
    
    return redirect('clicker:clicker_page')

@login_required
def leaderboard(request):
    leaderboard = User.objects.annotate(total_plantings=Count('planting')).order_by('-total_plantings')
    return render(request, 'clicker/leaderboard.html', {'leaderboard': leaderboard})

@login_required
def rewards(request):
    rewards = Reward.objects.filter(unlocked_by=request.user)
    return render(request, 'clicker/rewards.html', {'rewards': rewards})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('clicker:clicker_page')
    else:
        form = RegisterForm()
    return render(request, 'clicker/register.html', {'form': form})