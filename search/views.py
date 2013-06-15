from django.shortcuts import render_to_response
from django.template.context import RequestContext
from property.models import Property, City
from realestate.settings import MEDIA_URL

def searchView(request):
    pass

def searchResult(request):
    if request.POST:
        searchQ = request.POST.copy()
        if request.POST['buyorlet'] == "Rent":
            searchQ['buyorlet'] = "LE"
    
        results = Property.objects.filter(city_id__name__iexact=searchQ['search_term'])
        results = results.filter(price__gte=searchQ['price_from']).filter(price__lte=searchQ['price_to'])
        results = results.filter(rooms__gte=searchQ['no_of_rooms'])
        
        if searchQ['buyorlet'] == "LE":
            results = results.filter(sale_type__iexact=searchQ['buyorlet'])
        
        return render_to_response(  'search/index.htm', 
                                    {'search_results' : results, 
                                     'media_url' : MEDIA_URL}, 
                                    context_instance=RequestContext(request)
                                  )
    else:
        results = []
        return render_to_response(  'search/index.htm', 
                                    {'search_results' : results, 
                                     'media_url' : MEDIA_URL},  
                                    context_instance=RequestContext(request)
                                  )