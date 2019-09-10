from django.views.generic.base import View
from django.shortcuts import render,redirect

class Home(View):

    def get(self, request):

        pass
        return render(request, template_name='index.html')

class Show(View):

    def get(self, request):
        data = {'new':"添加内容"}
        return render(request, "show_1.html", context=data)