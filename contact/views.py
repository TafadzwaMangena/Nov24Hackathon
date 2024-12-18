from django.shortcuts import render
from .models import Faq


def contact(request):
    return render(request, 'contact/contact.html')


def faq_page(request):
      # Fetch all the FAQs from the database
    faq_list = Faq.objects.all()
    
    # Pass the FAQs to the template
    return render(request, 'contact/faq.html', {'faq_list': faq_list})
