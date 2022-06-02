from importlib.util import resolve_name
from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from .models import Blog
from .forms import BlogForm


class CourseDelete(View):
    template_name = 'blogs/blogs_delete.html'
    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Blog, id=id)
            return obj
    def get(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object']=obj
        return render(request, self.template_name, context)
    def post(self, request, id=None):
        context ={}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object']=None
            return redirect('blogs:course-list')
        return render(request, self.template_name, context)
        



class CourseUpdate(View):
    template_name = 'blogs/blogs_update.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Blog,id=id)
            return obj
    def get(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = BlogForm(instance=obj)
            context['object']=obj
            context['form']=form
        return render(request, self.template_name, context)
    def post(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = BlogForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
            context['object']=obj
            context['form']=form
        return render(request, self.template_name, context)



class CourseCreate(View): 
     template_name = 'blogs/blogs_create.html'
     def get(self, request):
         form = BlogForm()
         context ={'form':form}
         return render(request,  self.template_name, context)
     def post(self, request):
         form = BlogForm(request.POST)
         if form.is_valid():
             form.save()
             form = BlogForm()
         context = {'form':form}
         return render(request,  self.template_name, context)





class CourseListView(View):
       template_name = 'blogs/blogs_list.html'
       queryset = Blog.objects.all()
       def get_queryset(self):
           return self.queryset
       def get(self, request):
           return render(request, self.template_name, {'object_list':self.get_queryset()})
       
class MyList(CourseListView):
    queryset = Blog.objects.filter(id=1)
    






class CourseView(View): 
     template_name = 'blogs/blogs_detail.html'
     def get(self, request, id=None):
         context ={}
         if id is not None:
             obj = get_object_or_404(Blog, id=id)
             context['object']=obj
         return render(request,  self.template_name, context)
     
     


def my_fbv(request):
    print(request.method)
    return render(request, 'pages/about.html', {})

 




    
 
           
                         
