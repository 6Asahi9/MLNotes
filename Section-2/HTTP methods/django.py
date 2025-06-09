from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST

@require_GET
def get_item(request):
    return HttpResponse("GET request received")

@require_POST
def add_item(request):
    name = request.POST.get('name')
    qty = request.POST.get('qty')
    return HttpResponse(f"Added {qty} of {name}")
