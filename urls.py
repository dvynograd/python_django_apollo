from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from knowledgeBase.models import Memo, Article, Faq, Library
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',    
    
    (r'^$', 'knowledgeBase.views.index'),                                           
                       

    (r'^article/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Article
    )),                                               
    (r'^article/$', ListView.as_view(
        model=Article,
    )),

    (r'^faq/$', ListView.as_view(
        model=Faq,
    )),

    (r'^library/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Library
    )),                                               
    (r'^library/$', ListView.as_view(
        model=Library,
    )),
                       
    (r'^memos/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Memo
    )),                                               
    (r'^memos/$', ListView.as_view(
        model=Memo,
    )),               
                       
    (r'^admin/', include(admin.site.urls)),                       

)
