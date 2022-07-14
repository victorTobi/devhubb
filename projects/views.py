from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects


#multiple project view (project feed)
def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = { 'projects':projects, 'search_query':search_query, 
             'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)


#single project view
def project(request,  pk):
   projectObj = Project.objects.get(id=pk)
   form = ReviewForm()

   if request.method == 'POST':
       form = ReviewForm(request.POST)
       review = form.save(commit=False)
       review.project = projectObj
       review.owner = request.user.profile
       review.save()
       
       projectObj.getVoteCount

       messages.success(request, 'Your review has been saved')
       return redirect('project', pk=projectObj.id)

   context = {'project':projectObj, 'form':form}
   return render(request, 'projects/single-project.html', context)


# view for creating new projects
# this view cannot be accessed if the user is not logged in
@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)



#view to edit projects
#cannot be viewed if user is not logged in
#unathenticated users will be redirected to login(decorator below)
@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')


    context = {'form': form}
    return render(request, "projects/project_form.html", context)



#view/function to delete projects
#cannot be used if user is not logged in
#decorator below redirects unauthentcated users to loginpage
@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)