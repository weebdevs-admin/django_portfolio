from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.




class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    

    def get_context_data(self, **kwargs):

        
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['home'] = Home.objects.all()
        context['skill'] = Skill.objects.all()
        context['abaut']= Abaut.objects.all()
        context['timeline']= Timeline.objects.all()
        context['work']= Work.objects.all()
        context['blog']= Blog.objects.all()
        context['contact']= Contact.objects.all()
        return context

