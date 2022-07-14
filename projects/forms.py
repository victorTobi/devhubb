
from django.forms import ModelForm
from .models import Project, Review
from django import forms


#user needed input to create project on the create-project page
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image' , 'description',
         'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

#adding class="input" to ProjectForm so styles can be applied to the loop
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
        labels = {
            'value': 'Place your Vote',
            'body': 'Add your comment with your vote'
        }
        


    #adding class="input" to ReviewForm so styles can be applied to the loop
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})