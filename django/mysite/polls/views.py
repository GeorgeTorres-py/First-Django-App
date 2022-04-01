from django.http import HttpResponse
from django.views import views

class MyViews(View):
  def get(self, request,*args, *kwargs):
  return HttpResponse('')
