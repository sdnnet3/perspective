from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from website.forms import SubscribeForm  # Ensure this import is correct
from website.services.mailchimp_service import MailchimpService  # Ensure this import is correct
from website.models import ImageProduct  # Ensure this import is correct

def product_list(request):
    products = ImageProduct.objects.all()
    return render(request, 'coderedcms/pages/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(ImageProduct, id=product_id)
    return render(request, 'coderedcms/pages/product_detail.html', {'product': product})

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
    return render(request, 'coderedcms/pages/subscribe.html', {'form': form})

