from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    Display the contact us form and handle submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your message!')

        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)