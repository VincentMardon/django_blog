from django.conf.urls import patterns, include, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'accueil', name='accueil'),
    url(r'^(?P<slug>.+)$', 'lire_article', name='blog_lire'),
)
