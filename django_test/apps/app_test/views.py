from django.views.generic.base import View
from django.shortcuts import render,redirect

class Home(View):

    def get(self, request):

        pass
        return render(request, template_name='index.html')
