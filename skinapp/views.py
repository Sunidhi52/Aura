from django.shortcuts import render
from django.views import generic
from .models import NormalSkin, OilySkin, DrySkin, CombinationSkin, Recommendations, HealthcareRecommendations, body_Recommendations
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def homepage(request):
    recommendations = Recommendations.objects.all()
    return render(request, 'homepage.html', {'recommendations': recommendations})

def normal_skin(request):
    normal_skin_products = NormalSkin.objects.all()  
    return render(request, 'normal_skin.html', {'products': normal_skin_products})

def oily_skin(request):
    oily_skin_products = OilySkin.objects.all()  
    return render(request, 'oily_skin.html', {'products': oily_skin_products})

def dry_skin(request):
    dry_skin_products = DrySkin.objects.all()
    return render(request, 'dry_skin.html', {'products': dry_skin_products})

def combination_skin(request):
    combination_skin_products = CombinationSkin.objects.all()
    return render(request, 'combination_skin.html', {'products': combination_skin_products})

def about(request):
    return render(request, 'about.html')

def bodycare(request):
    recommendations = body_Recommendations.objects.all()
    healthcare_products = HealthcareRecommendations.objects.all()
    context = {
        'recommendations': recommendations,
        'healthcare_products': healthcare_products
    }
    return render(request, 'bodycare.html', context)

def find(request):
    return render(request, 'find.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, 'Sign up failed. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class NormalSkinList(generic.ListView):
    model = NormalSkin
    template_name = 'skincare/normalskin_list.html'
    context_object_name = 'normal_skins'

class OilySkinList(generic.ListView):
    model = OilySkin
    template_name = 'skincare/oilyskin_list.html'
    context_object_name = 'oily_skins'

class DrySkinList(generic.ListView):
    model = DrySkin
    template_name = 'skincare/dryskin_list.html'
    context_object_name = 'dry_skins'

class CombinationSkinList(generic.ListView):
    model = CombinationSkin
    template_name = 'skincare/combination_skin_list.html'
    context_object_name = 'combination_skins'

class NormalSkinDetail(generic.DetailView):
    model = NormalSkin
    template_name = 'skincare/normalskin_detail.html'
    context_object_name = 'normal_skin'

class OilySkinDetail(generic.DetailView):
    model = OilySkin
    template_name = 'skincare/oilyskin_detail.html'
    context_object_name = 'oily_skin'

class DrySkinDetail(generic.DetailView):
    model = DrySkin
    template_name = 'skincare/dryskin_detail.html'
    context_object_name = 'dry_skin'

class CombinationSkinDetail(generic.DetailView):
    model = CombinationSkin
    template_name = 'skincare/combination_skin_detail.html'
    context_object_name = 'combination_skin'




    
