from django.http import JsonResponse as res
from .models import Vood
from .serializer import VoodSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def vood_list(req):
    # req.method=="POST"
    voods=Vood.objects.all()
    serializer=VoodSerializer(voods, many=True)
    return Response({"voods":serializer.data})

@api_view(['POST'])
def add_vood(req):
    serializer= VoodSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"error":{"message":"Data not valid"}}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vood_detail(req, id):
    try:
        vood= Vood.objects.get(pk=id)
        serializer= VoodSerializer(vood)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Vood.DoesNotExist:
        return Response({"error":{"message":"Not found"}}, status=status.HTTP_404_NOT_FOUND)