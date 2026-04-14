from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contacts(request):
    return render(request, 'contacts.html')
def contacts2(request):
    context={}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success_message'] = 'Your message has been sent successfully.'
        context['form']= form
    else:
        context['error_message'] = 'There was an error sending your message. Please try again.'
        context['form']= form
    return render(request, 'contacts2.html', context)
