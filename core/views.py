from django.shortcuts import render
from .models import Feature, Stat, Testimonial, FAQ ,Event ,Course ,Session


def home(request):
    features = Feature.objects.all()
    stats = Stat.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()

    return render(request, 'home.html', {
        'features': features,
        'stats': stats,
        'testimonials': testimonials,
        'faqs': faqs
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def dashboard(request):
    return render(request, 'dashboard.html')

def course(request):
    status = request.GET.get('status')

    courses = Course.objects.all()

    if status:
        courses = courses.filter(status=status)

    completed_count = Course.objects.filter(status='Completed').count()

    context = {
        'courses': courses,
        'completed_count': completed_count,
        'certificates': completed_count,  # simple logic
        'hours_spent': "142h 30m"  # static (can make dynamic later)
    }

    return render(request, 'course.html', context)

from datetime import datetime

def sessions_view(request):
    sessions = Session.objects.all()

    days = [
        {"name": "Mon", "date": "Dec,04,12,25", "day_number": "04", "active": True},
        {"name": "Tue", "date": "Dec,05,12,25", "day_number": "05"},
        {"name": "Wed", "date": "Dec,06,12,25", "day_number": "06"},
        {"name": "Thu", "date": "Dec,07,12,25", "day_number": "07"},
        {"name": "Fri", "date": "Dec,08,12,25", "day_number": "08"},
        {"name": "Sat", "date": "Dec,09,12,25", "day_number": "09"},
        {"name": "Sun", "date": "Dec,10,12,25", "day_number": "10"},
    ]

    return render(request, 'session.html', {
        'sessions': sessions,
        'days': days,
        'today_date': datetime.today().strftime('%b %d, %Y'),
        'current_day': datetime.today().strftime('%A'),
    })

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages


# REGISTER
def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect('home')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('home')


# LOGIN
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('home')


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('home')

def attendance(request):
    return render(request, 'attendance.html')