from django import forms
from django.shortcuts import render, redirect
#from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from.models import Post
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError


# Create your views here.
#@csrf_protect
@csrf_exempt
def article_list(request):
    # if request post come
    if request.method == 'POST':
        try: 
            post = Post(
                first=request.POST['first'],
                last=request.POST['last'],
                phone_number=request.POST['phone_number'],
                email=request.POST['email'],
                social_media=request.POST['social_media']
            )
            # Save them to the database
            post.save()
            # After saving them show
            context={
                'post':post
            }
        except IntegrityError as e:
            context={'error':"its already exissts"}
            return render(request,'articles/article_list.html',{'post':post})
            #Getting our list template
        return render(request, 'articles/show_list.html', context)
    else:
        # If the register is not true
        # return the register template
        template = loader.get_template('articles/article_list.html')
    return HttpResponse(template.render())


@csrf_exempt
def show_list(request):
    if request.method == 'POST':
        trainer = Trainer(
            venues=request.POST['venues'],
            trained=request.POST['trained'],
            male=request.POST['male'],
            female=request.POST['female'],
            report=request.POST['report'],
            recommendation=request.POST['recommendation'],
            post_id=request.POST['post_id']
        )
        trainer.save()
        return render(request, 'articles/show_list.html', {'post':post, 'trainer':trainer})
    else:
        trainers = Trainer.objects.filter(post_id=post.id).order_by('date')
        return render(request, 'articles/show_list.html', {'post':post, 'trainers':trainers})
