import firebase_admin
import json
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .fusioncharts import FusionCharts
from .models import skill,work,project,education,article,product
from .forms import ContactForm
from firebase_admin import credentials
from firebase_admin import db
from django.core.mail import EmailMessage
from django.core import serializers


# Create your views here.
# cred = credentials.Certificate('/home/oussama/key.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://reseau-c2687.firebaseio.com'
# })


def home(request):
    skills=skill.objects.all
    projects=project.objects.all
    educations=education.objects.all
    articles=article.objects.all
    works=work.objects.all
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']+"\nSent from :"+from_email
            try:
                send_mail(subject, message, 'admin@oussamaahmed.info', ['oussama-ah@hotmail.fr'], fail_silently=False)
                send_mail('Please do not reply', 'Your mail was sent successfully.\nI will contact you very soon.\n Oussama AHMED.',
                          'admin@oussamaahmed.info', [from_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,"blog/index.html",locals())

def watchArticle(request, slug):
    Article = get_object_or_404(article, slug=slug)
    return render(request,'blog/blog-single.html',{'p' : Article})
def redirectToProject(request):
    return HttpResponse('sucess')

def watchProject(request,slug):
   Project = get_object_or_404(project, slug=slug)
   if(slug=='network-project'):
       data=product.objects.all()

       #product1=product(id=1,titre="product 1",creationDate="Fri Apr 06 2018 17:20:02 GMT+0100 (CET)",quantity=5422220)
       #product2=product(id=2,titre="product 1",creationDate="Fri Apr 06 2018 17:20:02 GMT+0100 (CET)",quantity=5422220)
       product1=product.objects.get(id=1)
       product2=product.objects.get(id=2)
       #print(product1.quantity)
       #print(product2.quantity)

       # Create an object for the column2d chart using the FusionCharts class constructor
       column2d = FusionCharts("column2d", "ex1", "600", "500", "chart-1", "json",
                               # The data is passed as a string in the `dataSource` as parameter.
                               """{  
                                      "chart": {  
                                         "caption":"Productivity",
                                         "subCaption":"Number of products produced this week",
                                         "numberPrefix":"",
                                         "theme":"ocean"
                                      },
                                      "data": [  
                                           {"label":"Product number 1", "value":"""+str(product1.quantity)+"""},
                                           {"label":"Product number 2", "value":"""+str(product2.quantity)+"""},
                                           {"label":"Product number 3", "value":"2"},
                                           {"label":"Product number 4", "value":"8"},
                                          
                                       ]
                                   }""")

       # returning complete JavaScript and HTML code,
       # which is used to generate chart in the browsers.
       return render(request, 'blog/NetworkProject.html', {'output': column2d.render(), 'p': Project, 'data': data})

       #return render(request,'blog/NetworkProject.html',locals())
   return render(request, 'blog/poject-single.html', {'p': Project})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# def emailView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 email = EmailMessage(
#                     subject=subject,
#                     body=message,
#                     from_email='admin@oussamaahmed.info',
#                     to=['oussama-ah@hotmail.fr'],
#                     #reply_to=['user@example.com'],
#                     headers={'Content-Type': 'text/plain'},
#                 )
#                 email.send()
#                 #send_mail(subject, message, from_email, ['oussama-ah@hotmail.fr'], fail_silently=False,)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "blog/index.html", {'form': form})

def ReadFromFirebase():
    root=db.reference('Production/Product/productID')
    #print(root.get())
    return root.get()

@csrf_exempt
def readFromJson(request):
    if request.method=='POST':
            print("post request ")
            received_json_data = json.loads(request.body)
            if received_json_data['auth']=='12345':
              p=product(id=received_json_data['id'],titre=received_json_data['titre'],creationDate=received_json_data['time'],quantity=received_json_data['quantity'])
              p.save()
              return StreamingHttpResponse('it was post request: '+str(received_json_data))
            return StreamingHttpResponse('Authentification Error!')
    return StreamingHttpResponse('it was GET request')

