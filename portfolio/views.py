from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, WorkExperience

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Work Exp
    work_experiences = WorkExperience.objects.all() 


    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'work_experiences': work_experiences,
    }


    return render(request, 'index.html', context)