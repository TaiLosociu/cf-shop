from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm, NewsletterForm
from django.core.mail import send_mail
from .models import Newsletter, Contact
from django.views.generic import CreateView


def contact(request, *args, **kwargs):
    """ Contact page functionality """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            # Send email
            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(
                request, 'Thank you for contacting us \
                        we will come back to you shortly.')
            # Redirect to home page
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Something went wrong, please try again.'
            )
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def newsletter(request):
    """ Allows user to signup for a newsletter
     and check if user is already in database """
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            redirect_url = request.POST['redirect_url']
            signed_up = Newsletter.objects.values_list('email', flat=True)

            if email in signed_up:
                messages.error(request, 'This email is alredy signed up!')
            else:
                form = NewsletterForm(request.POST)
                newsletter = form.save(commit=False)
                newsletter.name = name
                newsletter.email = email
                newsletter.save()
                messages.success(request, f'{email} \
                has been successfully added to our mailing list')
            return redirect(redirect_url)
    except ValueError:
        messages.error(
            request, 'Please enter your name and a valid email adress')
        return redirect(redirect_url)


class about(CreateView):
    """ A view to show about page """

    template_name = 'about/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
