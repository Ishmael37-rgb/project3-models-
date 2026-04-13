from django.shortcuts import render
from app.forms import ContactForm

# Create your views here.
def contact(request):
    return render(request, 'contact.html')
def contact2(request):
    context={}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success_message'] = 'Your message has been sent successfully.'
        context['form']= form
    return render(request, 'contact2.html', context)
