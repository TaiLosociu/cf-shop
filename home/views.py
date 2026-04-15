from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from products.models import Product, Category
from checkout.models import Order
from .auth_forms import CustomSignUpForm, CustomLoginForm

# Create your views here.


def index(request):
    """ A view to return to the home page """

    return render(request, 'home/index.html')


@require_http_methods(["GET", "POST"])
def auth_page(request):
    """ Custom authentication page for login and signup """
    
    if request.method == 'POST':
        # Determine if it's signup or login based on form submission
        if 'signup_submit' in request.POST:
            signup_form = CustomSignUpForm(request.POST)
            login_form = CustomLoginForm()
            
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                messages.success(request, f'Chào mừng {user.username}! Đăng ký thành công.')
                return redirect('home')
            else:
                # Display signup errors
                for field, errors in signup_form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        
        elif 'login_submit' in request.POST:
            login_form = CustomLoginForm(request=request, data=request.POST)
            signup_form = CustomSignUpForm()
            
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                messages.success(request, f'Chào mừng lại, {user.username}!')
                return redirect('home')
            else:
                # Display login errors
                for error in login_form.non_field_errors():
                    messages.error(request, error)
    else:
        signup_form = CustomSignUpForm()
        login_form = CustomLoginForm()
    
    context = {
        'signup_form': signup_form,
        'login_form': login_form,
    }
    
    return render(request, 'auth_page.html', context)


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin, login_url='account_login')
def admin_dashboard(request):
    """ Admin dashboard view """
    
    context = {
        'products_count': Product.objects.count(),
        'users_count': User.objects.count(),
        'orders_count': Order.objects.count(),
        'categories_count': Category.objects.count(),
    }
    
    return render(request, 'admin_dashboard.html', context)
