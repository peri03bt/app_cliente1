from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/create/', views.ProjectsCreateView.as_view(), name='projects-create'),
    path('projects/update/<int:pk>/', views.ProjectsUpdateView.as_view(), name='projects-update'),
    path('projects/delete/<int:pk>/', views.ProjectsDeleteView.as_view(), name='projects-delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/send/', views.contact_view, name='email'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('terms/', views.TermsView.as_view(), name='terms'),
]
