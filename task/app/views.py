from django.shortcuts import render,redirect
import requests
from .models import UserData
# Create your views here.

def home(request):
    
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category=happiness'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'mgppbbSLEXTr4afM8PhzVQ==ou1v5SbINLnvlVce'})
    # if response.status_code == requests.codes.ok:
    return render(request, 'index.html', {'quotes' : response.json()[0] })
        # print(response.text)
    # else:
    #     return render(request,'index.html',context={'quotes':"Error fetching quote"})

        # print("Error:", response.status_code, response.text)
    
def submit_form(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    user_data = UserData(name=name, email=email)
    if not name or not email:
        return redirect('home')
        
    return render(request, 'display_submit.html',{'user_data':user_data})

def display_list(request):
    list=UserData.objects.all()
    return render(request,'display_list.html',{'list':list})