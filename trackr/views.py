import os

from django.core import serializers
from django.http import HttpResponseForbidden,HttpResponse,JsonResponse
from django.shortcuts import render

import json

from .models import AP

#View to take in data from photon
def POST(request):

    #Ensure that the data is being POSTed
    if(request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        #Ensure that it's our device that is sending data
        if(body['coreid'] == os.environ["deviceID"]):

            #Do we know this AP already? If not, create it
            ap = AP.objects.get_or_create(BSSID=body['BSSID'])

            #Update RSSI
            ap.RSSI = body['RSSI']

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