import os

from django.core import serializers
from django.http import HttpResponseForbidden,HttpResponse,JsonResponse
from django.shortcuts import render

from .models import AP

#View to take in data from photon
def POST(request):

    #Ensure that the data is being POSTed
    if(request.method == 'POST'):

        #Ensure that it's our device that is sending data
        if(request.POST['coreid'] == os.environ["deviceID"]):

            #Do we know this AP already? If not, create it
            ap = AP.objects.get_or_create(BSSID=request.POST['BSSID'])

            #Update RSSI
            ap.RSSI = request.POST['RSSI']

            #Return all good
            return HttpResponse(status=200)

        #Response forbidden
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()

#View to give data back to users
def GET(request):

    #Ensure that we are GETting
    if(request.method == 'GET'):

        #Get the 10 strongest aps we have and serialize them to JSON
        data = serializers.serialize('json', AP.objects.order_by('RSSI')[:10], fields=('BSSID', 'RSSI'))

        #Return the data
        return JsonResponse(data)

    #Response forbidden
    else:
        return HttpResponseForbidden