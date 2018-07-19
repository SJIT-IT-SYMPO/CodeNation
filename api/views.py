from django.shortcuts import render
from accounts.models import UserProfile
from api.serializers import UserProfileSerializer
from rest_framework import mixins
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

# @csrf_exempt
# class UserPro(APIView):
# 	queryset = UserProfile.objects.all()
# 	serializer_class = UserProfileSerializer
# 	def post(self, request, format=None):
# 		serializer = UserProfileSerializer(data=request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# return self.create(request, *args, **kwargs)

@csrf_exempt
def user_data(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)