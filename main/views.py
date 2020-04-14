from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.utils import timezone
from .models import Provider, Requester, OrderRequest
from.forms import CreateNewProvider,CreateNewRequest

# Create your views here.
def index(response, id):
    request = get_object_or_404(OrderRequest, pk=id)
    return render(response,'main/list.html',{'request':request})

def home(response):
    completed_requests = OrderRequest.objects.filter(complete=True)
    open_requests = OrderRequest.objects.filter(complete=False).order_by('-datePublished')[:5]
    current_providers = Provider.objects.all()
    current_requesters = Requester.objects.all()
    context = {'completed_requests': completed_requests,
               'open_requests': open_requests,
               'current_providers': current_providers,
               'current_requesters': current_requesters}
    return render(response, 'main/home.html', context)

def create(response):
    if response.method == "POST":
        form = CreateNewRequest(response.POST)
        if form.is_valid():
            requester = form.cleaned_data["requester"]
            provider = form.cleaned_data["provider"]
            quantity = form.cleaned_data["quantity"]
            datePublished = timezone.now()
            newRequest = OrderRequest(requester=requester,provider=provider,quantity=quantity,datePublished=datePublished,complete=False)
            newRequest.save()
            print("Created new Request")
            return HttpResponseRedirect("/%i" % newRequest.id)
    else:
        form = CreateNewRequest() # todo CHANGE TO ORDER
    return render(response, 'main/create.html', {'form':form,'creationType':"request"})

def assign(assembled_request, request_id):
    print("ASSIGNED!")
    oRequest = OrderRequest.objects.get(pk=request_id)
    oRequest.provider = Provider.objects.get(pk=1)
    oRequest.save()
    return HttpResponseRedirect("/"+str(request_id))

def unassign(assembled_request, request_id):
    print("UN-ASSIGNED!")
    oRequest = OrderRequest.objects.get(pk=request_id)
    oRequest.provider = None
    oRequest.save()
    return HttpResponseRedirect("/"+str(request_id))

def complete(assembled_request, request_id):
    print("COMPLETED")
    oRequest = OrderRequest.objects.get(pk=request_id)
    oRequest.changeCompletion()
    oRequest.save()
    return HttpResponseRedirect("/" + str(request_id))

def uncomplete(assembled_request, request_id):
    print("UN-COMPLETED")
    oRequest = OrderRequest.objects.get(pk=request_id)
    oRequest.changeCompletion()
    oRequest.save()
    return HttpResponseRedirect("/" + str(request_id))