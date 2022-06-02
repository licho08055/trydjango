from django.urls import path
from blogs.views import (
    my_fbv,
    CourseView,
    CourseListView,
    MyList,
    CourseCreate,
    CourseUpdate,
    CourseDelete,
    )  
app_name = 'blogs'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
   #path('', my_fbv, name='fbv'),
   
   
   path('create/', CourseCreate.as_view(), name='course-create' ),
   path('<int:id>/', CourseView.as_view(), name='course-detail'),
   path('<int:id>/update', CourseUpdate.as_view(), name='course-update'),
   path('<int:id>/delete/',  CourseDelete.as_view(), name='course-delete'),
   
   
   
   
    
]
