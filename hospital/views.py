from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from .models import Doctor


class hospitalView(TemplateView):
    template_name = 'index.html'


class DoctorListView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'doctor-team.html'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = 'Healthcae Contact'

        if name and message and email_from:
            send_mail(
                subject + " - " + name,
                message +
                email_from,
                ['yourname@gmail.com', ],
                fail_silently=False,
            )
            messages.success(request, f'Your message has been sent. Thank you {name}!')

        return redirect('contact')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home/')  # Redirect to the appointments page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Registration successful. Welcome, {user.username}!')
            return redirect('home')  # Update 'home' to the actual URL name of your home page
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


from django.shortcuts import render

from django.shortcuts import render


def basic(request):
    return render(request, 'basic.html')


def pregnant_women_nutrition_page(request):
    # Add any additional logic or data retrieval here if needed
    return render(request, 'pregnant.html')


from django.shortcuts import render


def newly_born_child_nutrition_page(request):
    # Add any additional logic or data retrieval here if needed
    return render(request, 'newly-born-child-page.html')


from django.shortcuts import render


def gym_trainers_nutrition_page(request):
    # Add any additional logic or data retrieval here if needed
    return render(request, 'gym_trainers_nutrition_page.html')
