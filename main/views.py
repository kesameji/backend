from django.shortcuts import render
import requests
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
from django.http import HttpResponse

@login_required
@permission_required('main.index_viewer', raise_exception=True)
def index(request):
    current_url = request.build_absolute_uri()
    url = current_url + '/api/v1/landing'

    response_http = requests.get(url)
    response_dict = json.loads(response_http.content)

    total_responses = len(response_dict.keys())
    responses = response_dict.values()

    data = {
        'title':'Landing - Dashboard',
        'total_responses': total_responses,
        'responses': responses,
    }
    #return HttpResponse("Hello, World!")
    #return render(request, 'main/base.html')
    return render(request, 'main/index.html', data)