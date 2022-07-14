from django.apps import AppConfig
from django.http import HttpResponse

def projects(request):
    return HttpResponse('here are our projects')

def project(request,  pk):
    return HttpResponse('single project' + ' ' + str(pk))


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'
