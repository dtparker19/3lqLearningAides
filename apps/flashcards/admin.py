from django.contrib import admin
from .models import FlashCard

from import_export import resources
from .models import FlashCard

class FlashCardResource(resources.ModelResource):

    class Meta:
        model = FlashCard



# Register your models here.
admin.site.register(FlashCard)
