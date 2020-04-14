from django.contrib import admin

# Register your models here.
from .models import OrderRequest,Provider,Requester

admin.site.register(OrderRequest)
admin.site.register(Provider)
admin.site.register(Requester)