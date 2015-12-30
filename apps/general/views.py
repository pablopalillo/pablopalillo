from django.shortcuts import render_to_response
from django.views.generic import TemplateView

def indexSimple(request):
    return render_to_response('general/indexSimple.html')

class index2(TemplateView):
    template_name = "general/index2.html"
