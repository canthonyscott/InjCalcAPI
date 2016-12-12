from django.shortcuts import render
from django.views import View

# Create your views here.


# create a view to simply render a HTML page created with Angular2
class IndexView(View):

    def get(self, request):
        return render(request, 'GUI/index.html')
