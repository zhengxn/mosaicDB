from django.contrib import admin
from .models import Variant, Varinfo, pubinfo, indinfo, geneinfo

admin.site.register(Variant)
admin.site.register(Varinfo)
admin.site.register(pubinfo)
admin.site.register(indinfo)
admin.site.register(geneinfo)
