from rest_framework.decorators import api_view 
from rest_framework.response import Response
from root.models import Service , SpecialService , Skill , Team , Testimonial , ContactUs
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser , IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework import viewsets



class ServiceApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.all()


class SpecialServiceApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SpecialServiceSerializer

    def get_queryset(self):
        return SpecialService.objects.all()


class TeamApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Team.objects.all()
    


class TestimonialApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.all()




class ContactUsApiViewSet(viewsets.ModelViewSet):
    serializer_class = ContactUsSerializer

    def get_queryset(self):
        return ContactUs.objects.all()
    


class SkillApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.all()