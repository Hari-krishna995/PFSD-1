from django.urls import path
from django.urls import path

from .views import register_view, basic, pregnant_women_nutrition_page, newly_born_child_nutrition_page, \
    gym_trainers_nutrition_page
from . import views
from .views import login_view

urlpatterns = [
    path('home/', views.hospitalView.as_view(), name='hospital'),
    # path('service/', views.service, name='service'),
    # path('schedule/', views.schedule, name='schedule'),

    path('doctor/', views.DoctorListView.as_view(), name='doctor_team'),

    path('contact/', views.ContactView.as_view(), name='contact'),
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('basic/', basic, name='basic'),
    path('pregnantWomen/', pregnant_women_nutrition_page, name='pregnantWomen'),
    path('newly-born-child-nutrition-page/', newly_born_child_nutrition_page, name='newly_born_child_nutrition_page'),
    path('gym-trainers-nutrition-page/', gym_trainers_nutrition_page, name='gym_trainers_nutrition_page'),

    # path('about/', views.about, name='about'),
    # path('testimonial/', views.testimonial, name='testimonial'),
]