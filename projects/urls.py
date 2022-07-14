from . import views
from django.urls import path


#urls in projects app 
#'project' loads 'projects/single-project.html' //\\ path takes in the primary-key/id of the project you are trying to view.
#'create-project' loads 'projects/project_form.html' TO CREATE NEW PROJECT!! .
#'update-project' loads 'projects/project_form.html' TO EDIT AN EXISTING PROJECT!! //\\ takes in primary-key/id of the instance to be edited.
#'delete-project' loads 'projects/delete_template.html' TO DELETE AN EXISTING PROJECT!! //\\ takes in primary-key/id of the instance.
urlpatterns =[
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    path('create-project/', views.createProject, name="create-project"),
    
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]