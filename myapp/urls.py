from django.conf.urls import url
from myapp.views import list_view, detail_view, new_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^post/new/$', new_post, name="new_post"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html")),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"))
]

