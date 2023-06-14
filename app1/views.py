from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from app1.serializers import *
from app1.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


class productcrud(APIView):

    def get(self,request,id):
        PQS=Product.objects.all()
        #PQS=Product.objects.get(id=id)
        PMD=productserializers(PQS,many=True)
        return Response(PMD.data)
    

    def post(self,request,id):
        PMSD=productserializers(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is created'})
        else:
            return Response({'failed':'product creation is failed'})
        



    def put(self,request,id):

        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=productserializers(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product updated'})
        else:
            return Response({'failed':'product is not updated'})


    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=productserializers(PO,data=request.data,partial=True)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product  is partially updated'})
        else:

            return Response({'failed':'product is not partially updated'})

       
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'success':'Product is deleted'})
        