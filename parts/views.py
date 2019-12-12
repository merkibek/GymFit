from django.shortcuts import render, redirect
from .models import Applications, Client
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from datetime import datetime
from .models import Client, Attendance
from .serializers import ClientSerializer


class AttendanceView(ViewSet):
    def verify(self, request):
        if request.method == 'POST':
            print(request.data)
            if 'card_id' in request.data:
                try:
                    client = Client.objects.get(card_id=(request.data['card_id']))
                except:
                    return Response({"message": "No such person!"})

                date = datetime.now()
                if client.sub_status == 'CN':
                    return Response({"message": 'Client\'s subscription has expired!'})
                if client.pass_type == 'DY' and date.hour >= 16:
                    return Response({"message": 'Client has *Daily* pass, time out!'})
                if client.pass_type == 'EV' and date.hour < 17:
                    return Response({"message": 'Client has *Evening* pass. Time hasn\'t come yet'})

                attend = Attendance()
                attend.client = client
                attend.date_attended = date
                attend.save()
                return Response({"message": 'Successful!'})
            else:
                return Response({"message": "Error, empty content: card number!"})


class ClientView(APIView):
    def get(self, request):
        articles = Client.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ClientSerializer(articles, many=True)
        return Response({"clients": serializer.data})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def classes(request):
    return render(request, 'class.html')


def contact(request):
    return render(request, 'contact.html')


def trainers(request):
    return render(request, 'trainers.html')


def join_class(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    d = Applications.objects.create(name=name, email=email, phone=phone)
    d.save()
    response = redirect('/class.html')
    return response


def join_us(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    d = Applications.objects.create(name=name, email=email, phone=phone, message=message)
    d.save()
    response = redirect('/index.html')
    return response


def contact_us(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    d = Applications.objects.create(name=name, email=email, message=message)
    d.save()
    response = redirect('/contact.html')
    return response
