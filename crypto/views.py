from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,EOS,BCH,LTC,XLM,ADA,USDT,MIOTA&tsyms=USD,EUR")
	price = json.loads(price_request.content)
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request,'home.html',{'api':api, 'price':price })


def prices(request):

	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote =quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
	
		return render(request,'prices.html',{ 'quote':quote ,'crypto':crypto})
	else:
		non="Enter crypto currency to be searched...."
		return render(request,'prices.html',{'non':non})