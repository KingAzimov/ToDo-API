from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from rest_framework.views import APIView
from .serializers import *

class PlansAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        plans = Plan.objects.filter(user=request.user)
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)
    def post(self, request):
        plan = request.data
        serializer = PlanSerializer(data=plan)
        if serializer.is_valid():
            serializer.save(user=request.user)
            natija={"Succes":"True",
                    "New plan":serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class PlanAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def delete(self, request, pk):
        plan = Plan.objects.get(id=pk)
        plan.delete()
        return Response({"Deleted"})

    def put(self, request, pk):
        plan = Plan.objects.get(id=pk)
        data=request.data
        serializer = PlanSerializer(plan, data=data)
        if serializer.is_valid():
            serializer.save()
            natija={"Succes":"True",
                    "Changed data":serializer.data}
            return Response(natija)
        return Response({"Succes":"False", "detail":serializer.errors})