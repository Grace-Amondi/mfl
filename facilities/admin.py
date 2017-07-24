from django.contrib import admin

from facilities.models import Officer,OfficerContact,FacilityOfficer,Facility,Owner,OwnerType,KephLevel,\
    FacilityRegulationStatus,FacilityService,FacilityApproval,FacilityContact,FacilityDepartment,FacilityExportExcelMaterialView,FacilityLevelChangeReason,FacilityStatus,FacilityOperationState,FacilityUnit,FacilityUnitRegulation,FacilityUpdates,FacilityUpgrade,FacilityType,FacilityServiceRating

admin.site.register(Officer)
admin.site.register(OfficerContact)
admin.site.register(FacilityOfficer)
admin.site.register(Facility)
admin.site.register(Owner)
admin.site.register(OwnerType)
admin.site.register(KephLevel)
admin.site.register(FacilityService)
admin.site.register(FacilityApproval)
admin.site.register(FacilityContact)
admin.site.register(FacilityDepartment)
admin.site.register(FacilityExportExcelMaterialView)
admin.site.register(FacilityLevelChangeReason)
admin.site.register(FacilityStatus)
admin.site.register(FacilityOperationState)
admin.site.register(FacilityUnit)
admin.site.register(FacilityUpgrade)
admin.site.register(FacilityUpdates)
admin.site.register(FacilityRegulationStatus)






