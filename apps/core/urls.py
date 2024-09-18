from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/send/', views.contact_view, name='email'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('terms/', views.TermsView.as_view(), name='terms'),
]
