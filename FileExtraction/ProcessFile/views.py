################################################################################################################
# reference :- https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb #
# https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application                                                                                                             #
# https://realpython.com/django-setup/                                                                                                             #
# https://github.com/ShubhamBansal1997/token-authentication-django/blob/master/myproject/myproject/urls.py     #
################################################################################################################

import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http.response import JsonResponse
#from rest_framework.permissions import IsAuthenticated

#################################

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print("!!!!!!!!! inside-login-function !!!!!!!!!!")
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

#################################
@csrf_exempt
@api_view(["POST"])
def extract_json(request):
    #permission_classes = (IsAuthenticated,)
    #print("@#$@#@$@#$" , IsAuthenticated , "!!!!!" , permission_classes)
    file_raw = request.POST.get("name") + '.csv'  if request.POST.get("name") else "myfile.csv"
    print("!!!!!!!!!!!!!!!!" ,file_raw )
    #df = pd.read_csv("file_raw.csv")
    #print(df.show())

    files = request.FILES.getlist("file")
    print("#####", files)

    docx = []
    fs = FileSystemStorage()
    docx_urls = []

    for _file in files:
        print("inside for loop 1111 ")
        if _file.name.endswith('.csv') or _file.name.endswith('.CSV'):
            docx.append(_file)
            doc_name = fs.save(_file.name, _file)
            doc_path = os.path.join(settings.MEDIA_ROOT, doc_name)
            if os.path.exists(doc_path):
                docx_urls.append(doc_path)

    for url in docx_urls:
        print("inside for loop 2222")
        print("@$$$$$$$" , url)

    dataFrame_raw = pd.read_csv(url)
    #print(dataFrame_raw)



    ######### send data to rest #########

    js = dataFrame_raw.to_json()
    #print(js, "$$$$$$$$")

    columns = list(dataFrame_raw.columns.values)
    print(columns)

    ############
    data = []
    for _, row in dataFrame_raw.iterrows():
        temp = {}
        for col in columns:
            temp[col] = row[col]
        data.append(temp)

    try:
        return JsonResponse({
            "columns": columns,
            "data": data
        }, status=200)
        print("we got success !!!!")
    except Exception as e:
        print("!@!@!@" , e)
        return JsonResponse({"error": "error converting file"}, status =500)

