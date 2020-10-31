from datetime import date, datetime, timedelta
from django.contrib import messages
#from django.http import JsonResponse
from django.shortcuts import render
#from django.views.generic import View
from .forms import TickerForm
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from stock.stock_api_call import stock_api_call
# from rest_framework import authentication, permissions

# Create your views here.
def home(request):
    args = {}
    if request.method == "POST":
        form = TickerForm(request.POST)
        args['form'] = form
        if form.is_valid():
            ticker = form.cleaned_data.get('ticker').upper()
            print(ticker)
            args['ticker'] = ticker
            try:
                data = stock_api_call(ticker)
                args.update(data)
            except:
                messages.error(request, "Please enter a valid ticker symbol.")

    else:
        form = TickerForm()
        args['form'] = form

    return render(request, 'stock/home.html', args)


class StockData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
# ///////////////TEST DATA//////////////////////////////////////////////////
        data = {
            "labels": ["2020-08-31", "2020-09-01", "2020-09-02", "2020-09-03", "2020-09-04"],
            "default": [110,140,90,100,130],
            "maxiPri": 40,
            "buy": 90,
            "sell": 130,
            "buy_date": "Day 3",
            "sell_date": "Day 5"
        }
        return Response(data)
