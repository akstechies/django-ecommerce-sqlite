from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from products.models import Product
from user_cart.models import CartItem
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def cart_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    context = {'cart_items': cart_items}
    return render(request, 'profile.html', context)
        
    
def add_to_cart_ajax(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        try:
            product = get_object_or_404(Product, pk=product_id)
            user = request.user

            # Check if the product is already in the cart for the user
            cart_item, created = CartItem.objects.get_or_create(product=product, user=user)

            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return JsonResponse({'message': 'Item added to cart successfully'})
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)
    return JsonResponse({'message': 'Invalid request'}, status=400)

def remove_from_cart_ajax(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        try:
            product = Product.objects.get(pk=product_id)
            user = request.user

            # Check if the product is in the cart
            try:
                cart_item = CartItem.objects.get(product=product, user=user)

                if cart_item.quantity == 1 or 'delete' in request.POST:
                    cart_item.delete()
                else:
                    cart_item.quantity -= 1
                    cart_item.save()

                return JsonResponse({'message': 'Item removed from cart successfully'})
            except CartItem.DoesNotExist:
                return JsonResponse({'message': 'Item not found in cart'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)

    return JsonResponse({'message': 'Invalid request'}, status=400)
