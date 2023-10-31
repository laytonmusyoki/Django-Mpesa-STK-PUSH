from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0759352129'
    amount = 1
    account_reference = 'LaytonSoftwares'
    transaction_desc = 'Description'
    callback_url = 'https://mydomain.com/path'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        print(data)
        return HttpResponse("STK push in django")