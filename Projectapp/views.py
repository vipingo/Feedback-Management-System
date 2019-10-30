from django.shortcuts import render, redirect
from django.http import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserProfileInfoForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from Projectapp.models import UserProfileInfo, Criticality, Relief_Status, Feedback,Ratings
from django.views.generic import View


# Create your views here.
def HomeView(request):
    return render(request, 'Homepage.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('/Projectapp/user_login/'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(('/Projectapp/Home/'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def FeedbackFormView(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Date = form.cleaned_data['Date']
            Doctor_Id = form.cleaned_data['Doctor_Id']
            Employee_Id = form.cleaned_data['Employee_Id']
            Patient_Name = form.cleaned_data['Patient_Name']
            Relation = form.cleaned_data['Relation']
            Primary_Diagnosis = form.cleaned_data['Primary_Diagnosis']
            Criticality = form.cleaned_data['Criticality']
            Stay_Expected = form.cleaned_data['Stay_Expected']
            Hospital_Name = form.cleaned_data['Hospital_Name']
            Date_of_Issue = form.cleaned_data['Date_of_Issue']
            Admission_Date = form.cleaned_data['Admission_Date']
            Discharge_On = form.cleaned_data['Discharge_On']
            Relief_Status = form.cleaned_data['Relief_Status']
            Diagnosis_by_Hospital = form.cleaned_data['Diagnosis_by_Hospital']
            Admin_Doctor = form.cleaned_data['Admin_Doctor']
            Post_hospital_treatment_visit_frequency = form.cleaned_data['Post_hospital_treatment_visit_frequency']
            Services_Reception = form.cleaned_data['Services_Reception']
            Reception_Rating = form.cleaned_data['Reception_Rating']
            Services_Doctorduty = form.cleaned_data['Services_Doctorduty']
            Doctorduty_Rating = form.cleaned_data['Doctorduty_Rating']
            Services_Bloodbank = form.cleaned_data['Services_Bloodbank']
            Bloodbank_Rating = form.cleaned_data['Bloodbank_Rating']
            OT_Services = form.cleaned_data['OT_Services']
            OT_Rating = form.cleaned_data['OT_Rating']
            Services_Nursingcare = form.cleaned_data['Services_Nursingcare']
            Nursingcare_Rating = form.cleaned_data['Nursingcare_Rating']
            OPD_Services = form.cleaned_data['OPD_Services']
            OPD_Rating = form.cleaned_data['OPD_Rating']
            Pharmacy_Services = form.cleaned_data['Pharmacy_Services']
            Pharmacy_Rating = form.cleaned_data['Pharmacy_Rating']
            Pharmacy_Services_Supply_to_room = form.cleaned_data['Pharmacy_Services_Supply_to_room']
            Labservices_Services = form.cleaned_data['Labservices_Services']
            Labservices_Rating = form.cleaned_data['Labservices_Rating']
            Housekeeping_Services = form.cleaned_data['Housekeeping_Services']
            Housekeeping_Rating = form.cleaned_data['Housekeeping_Rating']
            Security_Services = form.cleaned_data['Security_Services']
            Security_Rating = form.cleaned_data['Security_Rating']
            Discharge_Formality_Services = form.cleaned_data['Discharge_Formality_Services']
            Discharge_Formality_Rating = form.cleaned_data['Discharge_Formality_Rating']
            Overall_satisfaction_Services = form.cleaned_data['Overall_satisfaction_Services']
            Overall_satisfaction_Rating = form.cleaned_data['Overall_satisfaction_Rating']
            Why_to_choose_this_hospital = form.cleaned_data['Why_to_choose_this_hospital']
            Why_not_to_choose_this_hospital = form.cleaned_data['Why_not_to_choose_this_hospital']
            Doctor_Feedback_Services = form.cleaned_data['Doctor_Feedback_Services']

            form = Feedback(user=request.user, Date=Date, Doctor_Id=Doctor_Id, Employee_Id=Employee_Id,
                            Patient_Name=Patient_Name,
                            Relation=Relation, Primary_Diagnosis=Primary_Diagnosis, id_Criticality=Criticality,
                            Stay_Expected=Stay_Expected, Hospital_Name=Hospital_Name, Date_of_Issue=Date_of_Issue,
                            Admission_Date=Admission_Date, Discharge_On=Discharge_On, id_Relief_Status=Relief_Status,
                            Diagnosis_by_Hospital=Diagnosis_by_Hospital, Admin_Doctor=Admin_Doctor,
                            Post_hospital_treatment_visit_frequency=Post_hospital_treatment_visit_frequency,
                            Services_Reception=Services_Reception, #Reception_Rating=Reception_Rating,
                            Services_Doctorduty=Services_Doctorduty,
                            #Doctorduty_Rating=Doctorduty_Rating,
                            Services_Bloodbank=Services_Bloodbank,
                            #Bloodbank_Rating=Bloodbank_Rating,
                            OT_Services=OT_Services, #OT_Rating=OT_Rating,
                            Services_Nursingcare=Services_Nursingcare,
                            #Nursingcare_Rating=Nursingcare_Rating,
                            OPD_Services=OPD_Services, #OPD_Rating=OPD_Rating,
                            Pharmacy_Services=Pharmacy_Services,
                            #Pharmacy_Rating=Pharmacy_Rating,
                            Pharmacy_Services_Supply_to_room=Pharmacy_Services_Supply_to_room,
                            Labservices_Services=Labservices_Services, #Labservices_Rating=Labservices_Rating,
                            Housekeeping_Services=Housekeeping_Services,
                            #Housekeeping_Rating=Housekeeping_Rating,
                            Security_Services=Security_Services,
                            #Security_Rating=Security_Rating,
                            Discharge_Formality_Services=Discharge_Formality_Services,
                            #Discharge_Formality_Rating=Discharge_Formality_Rating,
                            Overall_satisfaction_Services=Overall_satisfaction_Services,
                            #Overall_satisfaction_Rating=Overall_satisfaction_Rating,
                            Why_to_choose_this_hospital=Why_to_choose_this_hospital,
                            Why_not_to_choose_this_hospital=Why_not_to_choose_this_hospital,
                            Doctor_Feedback_Services=Doctor_Feedback_Services)

            form.save()
            form.Reception_Rating.add(Reception_Rating)
            form.Doctorduty_Rating.add(Doctorduty_Rating)
            form.Bloodbank_Rating.add(Bloodbank_Rating)
            form.OT_Rating.add(OT_Rating)
            form.Nursingcare_Rating.add(Nursingcare_Rating)
            form.OPD_Rating.add(OPD_Rating)
            form.Pharmacy_Rating.add(Pharmacy_Rating)
            form.Labservices_Rating.add(Labservices_Rating)
            form.Housekeeping_Rating.add(Housekeeping_Rating)
            form.Security_Rating.add(Security_Rating)
            form.Discharge_Formality_Rating.add(Discharge_Formality_Rating)
            form.Overall_satisfaction_Rating.add(Overall_satisfaction_Rating)

            return HttpResponseRedirect('http://127.0.0.1:8000/Projectapp/index/')

    #else:
        #form = FeedbackForm()
    return render(request, 'Feedback.html', {'form': form})


def index(request):
    user = request.user
    feedback = Feedback.objects.filter(user=request.user)
    # print(feedback.Date)
    return render(request, "index.html", {'users': feedback})


def criticality(request):
    if request.method == 'POST':
        crity = Criticality()
        # print (request.POST)
        # print("Recived Value:", request.POST.get('criticality'))
        crity.criticality = request.POST.get('criticality')
        crity.save()

        return HttpResponse(''' <script type ="text/javascript">
                                   window.close();
                                   window.parent.location.href = "http://127.0.0.1:8000/Projectapp/Form/" ;

                                </script> ''')
    return render(request, "criticality.html", {'crity': Criticality})


def relief(request):
    if request.method == 'POST':
        rel = Relief_Status()
        rel.status = request.POST.get('status')
        rel.save()

        return HttpResponse(''' <script type ="text/javascript">
                                   window.close();
                                   window.parent.location.href = "http://127.0.0.1:8000/Projectapp/Form/" ;

                                </script> ''')
    return render(request, "status.html", {'rel': Relief_Status})


def contact(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Subject = request.POST['Subject']
        return HttpResponse('Thank you for asking your Query !')
    return render(request, 'contactpage.html')
