from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import skill,work,project,education,article
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def watchArticle(request, slug):
    Article = get_object_or_404(article, slug=slug)
    return render(request,'blog/blog-single.html',{'p' : Article})

def watchProject(request,slug):
   Project = get_object_or_404(project, slug=slug)
   return render(request, 'blog/poject-single.html', {'p': Project})

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

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

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
                send_mail('Please do not reply', 'Your mail is sent successfully.\nI will contact you very soon.\n Oussama AHMED.', 'admin@oussamaahmed.info', [from_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,"blog/index.html",locals())