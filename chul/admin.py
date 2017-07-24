from django.contrib import admin

from chul.models import CHURating,CommunityHealthUnit,CHUService,ChuUpdateBuffer,CommunityHealthWorker

admin.site.register(CHURating)
admin.site.register(CommunityHealthWorker)
admin.site.register(CommunityHealthUnit)
admin.site.register(ChuUpdateBuffer)
admin.site.register(CHUService)
