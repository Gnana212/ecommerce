from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
  
  
class OrderView(View):
  
    def get(self, request):
        user = request.session.get('user')
        orders = Order.get_orders_by_user(user)
        print(orders)
        return render(request, 'ecom.csv', {'orders': orders})
