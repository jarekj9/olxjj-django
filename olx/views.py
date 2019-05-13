from django.shortcuts import render
from django.http import HttpResponse
from .olxjj import *
import pprint

#for auth:
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

	if request.method == 'POST':
		url = request.POST['link']
		search_type = request.POST['search_type']
		
		if search_type == "words":
			words = request.POST['words'].split(" ")
			html_data=[]
			olx_output=OLXJJ(url).get_links_with_word("or",words)
			
			data=""
			for key in olx_output:
				data+=key+"\n"
				data+=str(olx_output.get(key))+"\n"
				data+="\n\n"
			
			vars = {'data':data}
			return render(request, 'olx/output_word_search.html', vars)
		
		if search_type == "prices":
			data=""
			price_data=OLXJJ(url).get_all_prices()
			for item in price_data:
				data+=item+" : "+str(price_data.get(item))+"\n"
			
			vars = {'data':data}
			return render(request, 'olx/output_word_search.html', vars)
		
		
		
	else: 
		vars={}
		return render(request, 'olx/index.html', vars)
	
