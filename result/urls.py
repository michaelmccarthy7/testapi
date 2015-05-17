from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^results/$', 'task_list', name='task_list'),
)
