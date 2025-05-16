from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "Welcome to LaunchBase"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": (page_qs.count() / qs.count()) * 100 if qs.count() > 0 else 0,
    }
    
    PageVisit.objects.create(path = request.path)
    return render(request, 'home.html', my_context)
