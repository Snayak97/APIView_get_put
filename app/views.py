from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializes import *

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductCurd(APIView):
    def get(self,request,Pid):
        # PQS=Product.objects.get(Pid=request.data['Pid'])
        # PJSD=ProductMS(PQS)


        PQS=Product.objects.all()
        PJSD=ProductMS(PQS,many=True)
        return Response(PJSD.data)
    

    def post(self,request,Pid):
       PMSD=ProductMS(data=request.data) 
       if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is created'})
       else:
        return Response({'Failed':'Product is not created'})

    def put(self,request,Pid):
       Pid=request.data['Pid']
       PO=Product.objects.get(Pid=Pid)
       POD=ProductMS(PO,data=request.data)
       if POD.is_valid():
            POD.save()
            return Response({'message':'Product is Update'})
       else:
        return Response({'Failed':'Product is not Update'})

    def patch(self,request,Pid):
       Pid=request.data['Pid']
       PO=Product.objects.get(Pid=Pid)
       POD=ProductMS(PO,data=request.data,partial=True)
       if POD.is_valid():
            POD.save()
            return Response({'message':'Product is Update'})
       else:
        return Response({'Failed':'Product is not Update'})
    
    def delete(self,request,Pid):
       PO=Product.objects.get(Pid=Pid)
       PO.delete()
       return Response({'Mesage':'Delete sucessfully'})
