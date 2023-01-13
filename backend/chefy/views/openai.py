from rest_framework.views import APIView
from rest_framework import generics
from chefy.serializers import MyProfileSerializers, MyProfileImageSerializers
from chefy.services.openai_service import openAiService
from chefy.models import ChefyRecipeModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE, TYPE_INTEGER
import os
from django.core.serializers.json import DjangoJSONEncoder
import json


class OPENAIAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("text", in_=IN_FORM, type="string", description="request for chatgpt", required=True),
        ]
    )
    def post(self, request):

        text = request.data["text"]
        service = openAiService()

        print("Fetching ChatGPT response")
        chatgpt_response = service.chat_gpt(f"{text}. Please include a list of ingridients instructions")
        print(f"Done fetching ChatGPT response: {chatgpt_response}")

        chefy_recipe = ChefyRecipeModel.objects.create(chat_gpt_response=chatgpt_response, user="temp_user")

        return HttpResponse(chatgpt_response, content_type="text/plain")
