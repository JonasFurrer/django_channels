from django.shortcuts import render

def sensor_view(request):

    return render(request, "sensor.html", {'sensor': '99'})