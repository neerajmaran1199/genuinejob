from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Post

from django.urls import reverse
# Create your views here.
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'gjs_app/home.html', {'posts': posts})
    

class PostCreateView(CreateView):
    model = Post
    fields = ['job_title','company_name','job_type','qualification','job_location','monthly_salary','hiring_process','job_description','company_website','about_company', 'last_date','work_from', 'apply_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('home-page')
 

class PostDetailView(DetailView):
    model = Post
    template_name = 'gjs_app/postdetail.html'


def contact(request):
    return render(request, 'gjs_app/contact.html')

def home2(request):
    return render(request, 'gjs_app/index1.html')