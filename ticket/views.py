from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
import requests
from .serializers import *
# Create your views here.
from .models import *
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect

make = PaymentLinks.objects.get(name='make').link
pay = PaymentLinks.objects.get(name='pay').link
check = PaymentLinks.objects.get(name='check').link
api_key = Terminal.objects.get(name='poolam').api_key
poolam = Terminal.objects.get(name='poolam')


class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usr = self.request.user
        user = Profile.objects.filter(user=usr)
        return user


class HallListView(ListAPIView):
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticated]
    queryset = Hall.objects.all()


class CheckBought(GenericAPIView):
    def post(self, request):
        id = self.request.data.get('id', None)

        if id:
            try:
                usr = User.objects.get(username=id)
            except:
                return Response('user does not exist')
            user = Profile.objects.get(user=usr)
            t = Ticket.objects.filter(profile=user)
            if t:
                return Response(False)

        return Response(True)

    # return Response({})


class SeatReserveView(CreateAPIView):
    serializer_class = SeatSerializer

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        #         [{seat_pk:usr},{pk_seat:usr}]

        a = self.request.data
        for i in a:
            for j in i:
                pass
        # TODO reserve tickets
        return Response({})


class BuyTicketView(CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        Hall.objects.all()
        # TODO
        pass


class SetInvoice(CreateAPIView):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = InvoiceSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        amount = data.get('amount')
        make_response = requests.post(make, data={"api_key": api_key, "amount": amount,
                                                  "return_url": "http%3A%2F%2Fapi.moarefe98.ir%2Fadmin%2F"})
        invoice_key = (make_response.json()["invoice_key"])
        status = (make_response.json()["status"])

        if status == 1:
            Invoice.objects.create(terminal=poolam, amount=amount, key=invoice_key, status='w',)
            # TODO PAY
        else:
            # TODO CANCEL
            pass

        return Response('done')


# TODO CHECK PAYMENT AND REDIRECT

# TODO SIGNUP

# TODO GET BLOCKS
# TODO RESERVE SEATS
# TODO ASSIGN SEATS AND CREATE TICKETS
# TODO SHOW TICKETS


# TODO CREATE BLACKLIST
