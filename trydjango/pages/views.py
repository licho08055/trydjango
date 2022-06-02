from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
 

def home_view(request):
    return render(request, 'pages/home.html', {} )


def contact_view(request):
      return render(request, 'pages/contact.html', {} )


def about_view(request):
    context = {
        'text': 'This is about us',
        'number': 123,
        'list': [ 111,222, 768 ]
    }
    return render(request, 'pages/about.html', context )



def social_view(request):
         return render(request, 'pages/social.html', {} )
     
def see_view(request):
    return render(request, 'pages/see.html', {'see': 'Do what you see'})
     
     
 
