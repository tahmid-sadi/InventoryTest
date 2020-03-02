from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import StockList, Order
from .forms import OrderForm, StockListForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('stocklist')
    return render(request, 'accounts/register.html', {'form': form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'Admin':
                return redirect('stocklist')
            else:
                return redirect('orderspage')

        else:
            messages.error(request, 'Username or Password error.')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def stocklist(request):
    products = StockList.objects.all()
    return render(request, 'accounts/stocklist.html', {'products': products})


@login_required(login_url='login')
def orderspage(request):
    if request.user.username == 'Admin':
        orders = Order.objects.all()
    else:
        orders = request.user.order_set.all()
    return render(request, 'accounts/orderspage.html', {'orders': orders})


@login_required(login_url='login')
def createpage(request):
    form = OrderForm
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderspage')
    context = {'form': form}
    return render(request, 'accounts/createpage.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def productcreatepage(request):
    form = StockListForm
    if request.method == "POST":
        form = StockListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocklist')
    context = {'form': form}
    return render(request, 'accounts/productcreatepage.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')



