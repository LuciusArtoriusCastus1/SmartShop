from django.urls import path

from products.views import *

urlpatterns = [
    path('add/<slug:cat>/', AddProduct.as_view(), name='add_product'),
    path('update/<slug:product>/<slug:cat>/', UpdateProduct.as_view(), name='update_product'),
    path('delete/<slug:product>/', DeleteProduct.as_view(), name='delete_product'),
    path('add/<slug:product>/attachments/', AddAttachments.as_view(), name='add_attachments'),
    path('set/up/<slug:product>/rating/', SetUpRate.as_view(), name='set_up_rate'),
    path('like/<int:review>/<slug:product>/review/', LikeView.as_view(), name='like'),
    path('add/<slug:product>/review/', AddReview.as_view(), name='add_review'),

]