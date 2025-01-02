from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from .forms import ClientLoginForm
from website.models import Product
from cart.cart import Cart  # Update this import
from django.contrib import messages
from .forms import SubscribeForm
from .services.mailchimp_service import MailchimpService

class ClientLoginView(View):
    template_name = 'coderedcms/pages/client_login.html'
    
    def get(self, request):
        form = ClientLoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Change 'dashboard' to your desired redirect URL
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, self.template_name, {'form': form})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=int(request.POST.get('quantity', 1)))
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

from django.contrib import messages
from django.shortcuts import render, redirect
from perspective.forms import SubscribeForm  # Ensure this import is correct
from perspective.services.mailchimp_service import MailchimpService  # Ensure this import is correct

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