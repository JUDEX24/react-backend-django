from django.http import JsonResponse
from .models import Customer
from .serializers import CustomerSerializer


def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({"customers": serializer.data})


def customer(request, id):
    data = Customer.objects.get(pk=id)
    serializer = CustomerSerializer(data)
    return JsonResponse({"customer": serializer.data})
