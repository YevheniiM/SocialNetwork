from django.conf.urls import include, url

urlpatterns = [
    url(r'^auth/?', include('rest_framework.urls'))
]
