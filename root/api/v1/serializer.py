from rest_framework import serializers
from root.models import *

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['title']

class SpecialServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialService
        fields = ['title' , 'description']

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['name' , 'skill' , 'facebook' , 'x' , 'linkedin']


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = ['name' , 'description' , 'status']



class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['title']



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['name']

