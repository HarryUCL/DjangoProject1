from home import views
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('' , views.index, name='index'),
    path('baidu' , views.baidu, name ='baidu'),
    path('info', views.info, name='info'),
    path('if', views.if_view, name='if'),
    path('for',views.for_view, name='for'),
    path('with',views.with_view, name='with'),
    path('url', views.url_view, name='url'),
    path('book/<book_id>',views.book_detail, name='book_detail'),
    path('greet',views.filter_view, name='filter'),
    path('template/form', views.template_form, name='template_form'),
    path('sta',views.static_view, name='static_view')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)