from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemCreateView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart, created = Cart.objects.get_or_create(user=request.user)

        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
            updated_serializer = self.get_serializer(cart_item)
            return Response(updated_serializer.data, status=status.HTTP_200_OK)
        else:
            serializer.validated_data['cart'] = cart
            serializer.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

