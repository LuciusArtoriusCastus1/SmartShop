from django.db.models import F
from django.views import View

from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from products.models import Products, ProductCategory, Attachments, Like, Reviews


class AddProduct(CreateView):
    model = Products
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = self.kwargs.get('cat')
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_form_class(self):
        cat = self.kwargs.get('cat')

        if cat == "phone":
            return AddPhone
        elif cat == "laptop":
            return AddLaptop
        elif cat == "tablet":
            return AddTablet

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.category = ProductCategory.objects.get(slug=self.kwargs.get('cat'))
        product.save()
        return redirect('add_attachments', product.slug)


class UpdateProduct(UpdateView):
    model = Products
    slug_url_kwarg = 'product'
    template_name = 'products/update_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['cat'] = self.kwargs.get('cat')
        context['product'] = self.kwargs.get('product')
        return context

    def get_form_class(self):
        cat = self.kwargs.get('cat')

        if cat == "Phone":
            return UpdatePhone
        elif cat == "Laptop":
            return UpdateLaptop
        elif cat == "Tablet":
            return UpdateTablet

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.kwargs.get('product')])


class DeleteProduct(DeleteView):
    model = Products
    slug_url_kwarg = 'product'
    template_name = 'products/delete_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['product'] = self.kwargs.get('product')
        return context

    def get_success_url(self):
        return reverse_lazy('index')


class AddAttachments(FormView):
    form_class = AddAttachmentsForm
    template_name = 'products/add_attachments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['product'] = self.kwargs.get('product')
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["photo"]
        product = Products.objects.get(slug=self.kwargs.get('product'))
        print(files)
        for f in files:
            Attachments.objects.create(photo=f, product=product)

        return redirect('index')


class SetUpRate(FormView):
    form_class = RatingForm
    template_name = 'products/set_up_rating.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['product'] = self.kwargs.get('product')
        return context

    def form_valid(self, form):
        product = Products.objects.get(slug=self.kwargs.get('product'))
        owner = self.request.user
        Rating.objects.update_or_create(
            product=product,
            owner=owner,
            defaults={'rate': form.cleaned_data['rate']}
        )

        return redirect('product_detail', product.slug)


class LikeView(View):

    def get(self, request, *args, **kwargs):
        try:
            like = Like.objects.get(review__id=self.kwargs.get('review'), owner=request.user)
        except Like.DoesNotExist:
            like = None

        if like is None:
            Like.objects.create(review=Reviews.objects.get(id=self.kwargs.get('review')), owner=request.user, liked=True)
            Reviews.objects.filter(id=self.kwargs.get('review')).update(likes=F('likes') + 1)
        else:
            if like.liked:
                like.liked = False
                like.save()
                Reviews.objects.filter(id=self.kwargs.get('review')).update(likes=F('likes') - 1)
            else:
                like.liked = True
                like.save()
                Reviews.objects.filter(id=self.kwargs.get('review')).update(likes=F('likes') + 1)

        return redirect('product_detail', self.kwargs.get('product'))


class AddReview(CreateView):
    model = Reviews
    template_name = 'products/add_review.html'
    form_class = AddReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['product'] = self.kwargs.get('product')
        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        review.owner = self.request.user
        review.product = Products.objects.get(slug=self.kwargs.get('product'))
        review.save()

        return redirect('product_detail', self.kwargs.get('product'))

