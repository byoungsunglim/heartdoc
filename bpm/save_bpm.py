import pymongo
import json
import requests
import math
from bson import json_util, ObjectId
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from heartdoc.settings import BASE_DIR
import datetime

@api_view(["POST"])
# class recommendation_place:
def save_bpm(request):
        client = pymongo.MongoClient("mongodb+srv://admin:Lbs95101417!@cluster0-hs3ep.gcp.mongodb.net/test?retryWrites=true")
        mydb = client.heartdoc

        userdb = mydb["user"]

        if userdb.find_one({"name": request["name"], "age": request["age"]}) == None:
                userdb.insert_one({"name": request["name"], "age": request["age"], "bpm_results": [{"avgBPM": request["avgBPM"], "updated_time": datetime.date.today().strftime("%B %d, %Y")}]})
        else:
                userdb.update_one({"name": request["name"], "age": request["age"]}, {"&push": {"bpm_results": [{"avgBPM": request["avgBPM"], "updated_time": datetime.date.today().strftime("%B %d, %Y")}]}})