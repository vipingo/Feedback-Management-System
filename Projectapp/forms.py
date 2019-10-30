from django import forms
from Projectapp.models import Relief_Status,Criticality,Feedback,Hospital_Master,Ratings,Ongc_Doc_Master,Relation,Ongc_Employee_Master
from django.contrib.auth.models import User
from Projectapp.models import UserProfileInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('employee_id','profile_pic')




class FeedbackForm(forms.Form):
    Date=forms.DateTimeField(widget=forms.DateInput(attrs={'class':'datepicker'}),input_formats=['%Y-%m-%d'],required=True)
    Doctor_Id=forms.ModelChoiceField(queryset=Ongc_Doc_Master.objects.all().order_by('doc_id'))
    Employee_Id=forms.IntegerField()
    Patient_Name=forms.CharField(widget=forms.TextInput, required=True, max_length=50)
    Relation=forms.ModelChoiceField(queryset=Relation.objects.all().order_by('Relation'))
    Primary_Diagnosis=forms.CharField(widget=forms.TextInput, required=True, max_length=100)
    Criticality=forms.ModelChoiceField(queryset=Criticality.objects.all().order_by('criticality'))
    Stay_Expected=forms.IntegerField()
    Hospital_Name=forms.ModelChoiceField(queryset=Hospital_Master.objects.all().order_by('Hospital_name'))
    Date_of_Issue=forms.DateTimeField(widget=forms.DateInput(attrs={'class':'datepicker'}),input_formats=['%Y-%m-%d'])


    Admission_Date=forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}),input_formats=['%Y-%m-%d'],required=True)
    Discharge_On=forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}),input_formats=['%Y-%m-%d'],required=True)
    Relief_Status=forms.ModelChoiceField(queryset=Relief_Status.objects.all().order_by('status'))
    Diagnosis_by_Hospital=forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Admin_Doctor=forms.CharField(widget=forms.TextInput, required=True, max_length=100)
    Post_hospital_treatment_visit_frequency=forms.CharField(widget=forms.TextInput, required=True , max_length=100)

    Services_Reception = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Reception_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Services_Doctorduty = forms.CharField(widget=forms.TextInput, required=True , max_length=10)
    Doctorduty_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Services_Bloodbank = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Bloodbank_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    OT_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    OT_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Services_Nursingcare = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Nursingcare_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    OPD_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    OPD_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Pharmacy_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Pharmacy_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Pharmacy_Services_Supply_to_room = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Labservices_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Labservices_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Housekeeping_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Housekeeping_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Security_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Security_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Discharge_Formality_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Discharge_Formality_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Overall_satisfaction_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Overall_satisfaction_Rating = forms.ModelChoiceField(queryset=Ratings.objects.all().order_by('rating'))
    Why_to_choose_this_hospital = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Why_not_to_choose_this_hospital = forms.CharField(widget=forms.TextInput, required=True , max_length=100)
    Doctor_Feedback_Services = forms.CharField(widget=forms.TextInput, required=True , max_length=100)





