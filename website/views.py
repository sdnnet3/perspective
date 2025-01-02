from django.contrib import messages
from django.shortcuts import render, redirect
from website.forms import SubscribeForm  # Ensure this import is correct
from website.services.mailchimp_service import MailchimpService  # Ensure this import is correct
from website.models import Product  # Ensure this import is correct

def product_list(request):
    products = Product.objects.all()
    return render(request, 'website/product_list.html', {'products': products})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mailchimp_service = MailchimpService()
            try:
                mailchimp_service.subscribe_user(email, first_name, last_name)
                messages.success(request, 'You have been subscribed!')
            except Exception as e:
                if 'already a list member' in str(e):
                    messages.info(request, 'You are already subscribed.')
                else:
                    messages.error(request, f'An error occurred: {e}')
            return redirect('subscribe')
    else:
        form = SubscribeForm()
    return render(request, 'coderedcms/website/pages/subscribe.html', {'form': form})

