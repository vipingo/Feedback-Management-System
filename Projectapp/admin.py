from django.contrib import admin
from Projectapp.models import Relation,Ratings,Feedback,Criticality, Relief_Status, Ongc_Doc_Master,Ongc_Employee_Master,Hospital_doc_Master,Hospital_Speciality,Primary_Hospital_Diagnosis,Primary_Ongc_Diagnosis,Procedure_Diagnosis,Hospital_Master

# Register your models here.
admin.site.register(Ongc_Doc_Master)
admin.site.register(Ongc_Employee_Master)
admin.site.register(Hospital_doc_Master)
admin.site.register(Hospital_Speciality)
admin.site.register(Primary_Hospital_Diagnosis)
admin.site.register(Primary_Ongc_Diagnosis)
admin.site.register(Procedure_Diagnosis)
admin.site.register(Hospital_Master)
admin.site.register(Criticality)
admin.site.register(Relief_Status)
admin.site.register(Feedback)
admin.site.register(Ratings)
admin.site.register(Relation)