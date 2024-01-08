from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from chat.models import ChatRoom
from products.models import Products, ProductCategory


class NewChatRoom(View):

    def get(self, request, *args, **kwargs):
        product = Products.objects.get(slug=self.kwargs.get('product'))
        seller = product.owner

        if request.user.is_authenticated:
            conversation = ChatRoom.objects.filter(product=product, members__in=[request.user, seller])
            if conversation:

                return redirect('chat_detail', conversation[0].id)
            else:
                chat_room = ChatRoom.objects.create(product=product)
                chat_room.members.set([request.user, seller])

                return redirect('chat_detail', chat_room.id)


class ChatRoomDetail(DetailView):
    model = ChatRoom
    template_name = 'chat/chat_room.html'
    pk_url_kwarg = 'room'
    context_object_name = 'conversation'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['room_name'] = ChatRoom.objects.get(id=self.kwargs.get('room'))
        return context


class DeleteChatRoom(View):

    def get(self, request, *args, **kwargs):
        chat = ChatRoom.objects.filter(id=self.kwargs.get('chat_id'))
        chat.delete()

        return redirect('inbox')
