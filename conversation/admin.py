from django.contrib import admin
from .models import Conversation, ConversatiionMessage

# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConversatiionMessage)

