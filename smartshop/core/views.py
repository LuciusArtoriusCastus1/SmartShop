from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from chat.models import ChatRoom
from .forms import *
from .models import Cart
from .services import *
from products.models import Products, Rating, ProductCategory, Attachments, Like, Reviews, MadeIn, ManufactureYear, \
    RatingStar


class Index(ListView):
    model = Products
    template_name = 'core/index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['made_in'] = MadeIn.objects.all()
        context['manufacture_year'] = ManufactureYear.objects.all()
        context['rating'] = RatingStar.objects.all().order_by('-star')

        return context

    def get_queryset(self):
        return Products.objects.filter(amount__gte=1)


class DetailProduct(DetailView):
    model = Products
    template_name = 'core/prod_detail.html'
    slug_url_kwarg = 'item'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['attachments'] = Attachments.objects.filter(product__slug=self.kwargs.get('item'))

        if self.request.user.is_authenticated:
            try:
                context['your_rate'] = Rating.objects.get(product__slug=self.kwargs.get('item'), owner=self.request.user)
            except Rating.DoesNotExist:
                context['your_rate'] = None
        else:
            context['your_rate'] = None

        if self.request.user.is_authenticated:
            context['cart_added'] = Cart.objects.filter(owner=self.request.user, product__slug=self.kwargs.get('item'))

        product = Products.objects.get(slug=self.kwargs.get('item'))
        reviews = product.reviews_set.all()
        reviews_order = self.request.GET.get('order')
        if reviews_order == 'post_date':
            reviews = reviews.order_by('-post_date')
        elif reviews_order == 'likes':
            reviews = reviews.order_by('-likes')

        context['reviews'] = reviews

        if self.request.user.is_authenticated:
            likes = Like.objects.filter(owner=self.request.user, review__in=reviews, liked=True)
            liked_reviews = [like.review for like in likes if like.review in reviews]
            context['liked_reviews'] = liked_reviews

        return context


class DashBoard(ListView):
    model = Products
    template_name = 'core/dashboard.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()

        return context

    def get_queryset(self):
        return Products.objects.filter(amount__gte=1, owner=self.request.user)


class CartList(ListView):
    model = Products
    template_name = 'core/cart.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()

        return context

    def get_queryset(self):
        cart = Cart.objects.filter(owner=self.request.user)
        cart = [item.product.name for item in cart]
        return Products.objects.filter(name__in=cart)


class AddToCart(View):

    def get(self, request, *args, **kwargs):
        cart = Cart()
        cart.owner = self.request.user
        cart.product = Products.objects.get(slug=self.kwargs.get('item'))
        cart.save()

        return redirect('product_detail',  self.kwargs.get('item'))


class DeleteFromCart(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(product__slug=self.kwargs.get('item'))
        cart.delete()

        return redirect('product_detail', self.kwargs.get('item'))


class Inbox(ListView):
    model = ChatRoom
    template_name = 'core/inbox.html'
    context_object_name = 'chat_rooms'

    def get_queryset(self):
        return ChatRoom.objects.filter(members__in=[self.request.user])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()

        return context


class FilterProducts(ListView):
    model = Products
    template_name = 'core/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['made_in'] = MadeIn.objects.all()
        context['manufacture_year'] = ManufactureYear.objects.all()
        context['rating'] = RatingStar.objects.all().order_by('-star')
        context['cat_url'] = ''.join([f'category={x}&' for x in self.request.GET.getlist('category')])
        context['made_in_url'] = ''.join([f'country={x}&' for x in self.request.GET.getlist('country')])
        context['year_url'] = ''.join([f'year={x}&' for x in self.request.GET.getlist('year')])
        context['rate_url'] = ''.join([f'rate={x}&' for x in self.request.GET.getlist('rate')])
        context['min_price_url'] = ''.join([f'min_price={x}&' for x in self.request.GET.getlist('min_price')])
        context['max_price_url'] = ''.join([f'max_price={x}&' for x in self.request.GET.getlist('max_price')])
        context['query_url'] = ''.join([f'query={x}&' for x in self.request.GET.getlist('query')])
        context['order_url'] = ''.join([f'order={x}&' for x in self.request.GET.getlist('order')])
        return context

    def get_queryset(self):
        category = self.request.GET.getlist('category')
        country = self.request.GET.getlist('country')
        year = self.request.GET.getlist('year')
        rating = self.request.GET.getlist('rate')

        order = self.request.GET.get('order')

        query = self.request.GET.get('query')

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:

            min_price = min_price
        else:
            min_price = 0

        if max_price:
            max_price = max_price
        else:
            max_price = 999999

        products = Products.objects.all()

        products = products.filter(
            price__range=(min_price, max_price)
        )

        if category:
            products = products.filter(
                category__name__in=category
            )

        if country:
            products = products.filter(
                made_in__name__in=country
            )

        if year:
            products = products.filter(
                manufacture_year__name__in=year
            )

        if rating:
            products = filter_rate(products, rate_list=rating)
            print(products)

        if query:
            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        if order == 'post_date':
            products = products.order_by('-post_date')
        elif order == 'sold':
            products = products.order_by('-sold')
        elif order == 'price_cheap':
            products = products.order_by('price')
        elif order == 'price_exp':
            products = products.order_by('-price')
        elif order == 'rate':
            products = order_rate(products)

        return products

