from rest_framework.views import APIView
from rest_framework import generics
from app.services.mlb_service import MlbStatsService
from app.models import DjangoAppModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE, TYPE_INTEGER
import os
from django.core.serializers.json import DjangoJSONEncoder
import json


class MlbAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("text", in_=IN_FORM, type="string", description="request for chatgpt", required=True),
        ]
    )
    def post(self, request):

        text = request.data["text"]
        service = MlbStatsService()

        entry = service.stats(text)
        
        model_object = DjangoAppModel.objects.create(entry=entry, user="temp_user")

        return HttpResponse(entry, content_type="text/plain")
