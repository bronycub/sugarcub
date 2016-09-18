from django.shortcuts               import render
from django.core.urlresolvers       import reverse_lazy
from django.views.generic.edit      import CreateView, UpdateView
from el_pagination.views            import AjaxListView
from django.http                    import HttpResponse
from django.shortcuts               import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
import json

def medias_category(request):

    return render(request, 'medias_category.html')
