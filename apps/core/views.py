from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
# Email
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, PostProjectsForm
from .models import PostProjects



class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['CLIENT_SMS'] = settings.CLIENT_SMS        
        return context

class ResumeView(TemplateView):
    template_name = 'home/resume.html'

class ProjectsView(TemplateView):
    template_name = 'home/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['EMAIL_HOST_USER'] = settings.EMAIL_HOST_USER
        context['CLIENT_SMS'] = settings.CLIENT_SMS
        context['CLIENT_NUMBER_STR'] = settings.CLIENT_NUMBER_STR
        context['projects'] = PostProjects.objects.order_by('?')
        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()        
        return context
    
class PrivacyView(TemplateView):
    template_name = 'home/privacy.html'

class TermsView(TemplateView):
    template_name = 'home/terms.html'

def contact_view(request):
    email_host_user = settings.EMAIL_HOST_USER

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Enviar o e-mail
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

            send_mail(
                'Contact Form Submission',
                full_message,
                email_host_user,
                [email_host_user,],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your form submission.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# CRUD Projects
class ProjectsListView(ListView):
    model = PostProjects
    template_name = 'home/projects_CRUD/projects_list.html'
    context_object_name = 'projects'

class ProjectsCreateView(CreateView):
    model = PostProjects
    form_class = PostProjectsForm
    template_name = 'home/projects_CRUD/projects_form.html'
    success_url = reverse_lazy('projects-list')

class ProjectsUpdateView(UpdateView):
    model = PostProjects
    form_class = PostProjectsForm
    template_name = 'home/projects_CRUD/projects_form.html'
    success_url = reverse_lazy('projects-list')

class ProjectsDeleteView(DeleteView):
    model = PostProjects
    template_name = 'home/projects_CRUD/projects_confirm_delete.html'
    success_url = reverse_lazy('projects-list')