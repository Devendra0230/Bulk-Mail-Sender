from django.contrib import admin
from .models import receiverFileModel,senderFileModel

# Register your models here.
@admin.register(senderFileModel)
class senderRegister(admin.ModelAdmin):
      list_display=[
            'id', 'file','esp','port', 'author'
      ]

@admin.register(receiverFileModel)
class receiverRegister(admin.ModelAdmin):
      list_display=[
            'id','file','author'
      ]
