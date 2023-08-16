from django.shortcuts import render, redirect
from .forms import OrderItemForm
from django.db.models import Sum
from .models import Order, OrderItem

def user_order(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order, _ = Order.objects.get_or_create(user_name=request.user.username)
            order_item.order = order
            order_item.save()
            return redirect('user_order')
    else:
        form = OrderItemForm()
    
    user_orders = OrderItem.objects.filter(order__user_name=request.user.username)
    
    context = {'form': form, 'user_orders': user_orders}
    return render(request, 'user_order.html', context)


def admin_dashboard(request):
    item_summaries = OrderItem.objects.values('item_name').annotate(total_quantity=Sum('quantity'))
    context = {'item_summaries': item_summaries}
    return render(request, 'admin_dashboard.html', context)

def delete_order_item(request, item_id):
    item = OrderItem.objects.get(id=item_id)
    if item.order.user_name == request.user.username:
        item.delete()
    return redirect('user_order')

