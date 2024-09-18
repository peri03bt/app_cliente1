from django.shortcuts import render
from django.views.generic import TemplateView

# Email
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'home/index.html'

class ResumeView(TemplateView):
    template_name = 'home/resume.html'

class ProjectsView(TemplateView):
    template_name = 'home/projects.html'

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
                'peridev88@gmail.com',
                ['peridev88@gmail.com',],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your form submission.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})