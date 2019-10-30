from django.db import models
from django.contrib.auth.models import User




class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    employee_id = models.IntegerField(primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return str(self.user.username) + "---" + str(self.employee_id)





class Criticality(models.Model):
    id = models.AutoField(primary_key=True)
    criticality = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.criticality) if self.criticality else ''


class Ongc_Doc_Master(models.Model):
    id = models.AutoField(primary_key=True)
    doc_id = models.IntegerField()
    Doc_name = models.TextField()
    Location = models.TextField()
    From = models.DateField()
    To = models.DateField()
    def __str__(self):
        return str(self.doc_id)


class Ongc_Employee_Master(models.Model):
    id = models.AutoField(primary_key=True)
    Employee_id = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE, null=True,blank=True)
    emp_name = models.TextField()
    relation = models.TextField()
    location = models.TextField()
    From = models.DateField()
    To = models.DateField()

    def __str__(self):
        return str(self.Employee_id) + "----" + str(self.emp_name)


class Hospital_Master(models.Model):
    Hospital_id = models.AutoField(primary_key=True)
    Hospital_name = models.TextField()
    Address = models.TextField()
    Location = models.TextField()

    def __str__(self):
        return str(self.Hospital_name) + "-----" + str(self.Address)


class Hospital_Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    Speciality = models.TextField()
    Hospital_id = models.ForeignKey('Hospital_Master',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.Speciality) + "----" + str(self.Hospital_id)


class Hospital_doc_Master(models.Model):
    id = models.AutoField(primary_key=True)
    Hospital_doc_id = models.TextField()
    Hospital_doc_name = models.TextField()
    From = models.DateField()
    To = models.DateField()
    doc_speciality = models.TextField()

    def __str__(self):
        return  str(self.doc_speciality)


class Primary_Ongc_Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    Diagnosis = models.TextField()
    Doc_id = models.ForeignKey('Ongc_Doc_Master',on_delete=models.CASCADE,null=True,blank=True)
    Employee_id = models.IntegerField(unique=True)
    id_Criticality = models.ForeignKey(Criticality,on_delete=None)

    def __str__(self):
        return str(self.Employee_id.Diagnosis) + "----" + str(self.Doc_id)


class Primary_Hospital_Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    Doc_id = models.ForeignKey(Hospital_doc_Master,on_delete=models.CASCADE)
    Diagnosis = models.TextField()

    def __str__(self):
        return self.Diagnosis


class Procedure_Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    Patient_id = models.TextField(unique=True)
    Procedure_id = models.TextField()
    Diagnosis = models.TextField()

    def __str__(self):
        return str(self.Patient_id) + "----" + str(self.Diagnosis)


class Relief_Status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.status) if self.status else ''


class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=15)

    def __str__(self):
        return str(self.rating)

class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    Relation = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Relation)


class Feedback(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Date = models.DateField()
    Doctor_Id = models.ForeignKey(Ongc_Doc_Master,on_delete=models.CASCADE,null=True,blank=True)
    Employee_Id = models.IntegerField()
    Patient_Name = models.CharField(max_length=30)
    Relation = models.ForeignKey(Relation,on_delete=models.CASCADE,null=True,blank=True)
    Primary_Diagnosis = models.CharField( max_length=100)
    id_Criticality = models.ForeignKey(Criticality,on_delete=None)
    Stay_Expected = models.IntegerField()
    Hospital_Name = models.ForeignKey(Hospital_Master ,on_delete=models.CASCADE,null=True,blank=True)
    Date_of_Issue = models.DateTimeField()

    Admission_Date = models.DateField()
    Discharge_On = models.DateField()
    id_Relief_Status = models.ForeignKey(Relief_Status,on_delete=None)
    Diagnosis_by_Hospital = models.TextField()
    Admin_Doctor = models.CharField(max_length=100)
    Post_hospital_treatment_visit_frequency = models.CharField(max_length=30)

    Services_Reception = models.CharField( max_length=100)
    Reception_Rating = models.ManyToManyField(Ratings,related_name='Reception_Rating')
    Services_Doctorduty = models.CharField( max_length=100)
    Doctorduty_Rating = models.ManyToManyField(Ratings,related_name='Doctorduty_Rating')
    Services_Bloodbank = models.CharField( max_length=100)
    Bloodbank_Rating = models.ManyToManyField(Ratings,related_name='Bloodbank_Rating')
    OT_Services = models.CharField( max_length=100)
    OT_Rating = models.ManyToManyField(Ratings,related_name='OT_Rating')
    Services_Nursingcare = models.CharField( max_length=100)
    Nursingcare_Rating = models.ManyToManyField(Ratings,related_name='Nursingcare_Rating')
    OPD_Services = models.CharField( max_length=100)
    OPD_Rating = models.ManyToManyField(Ratings,related_name='OPD_Rating')
    Pharmacy_Services = models.CharField( max_length=100)
    Pharmacy_Rating = models.ManyToManyField(Ratings,related_name='Pharmacy_Rating')
    Pharmacy_Services_Supply_to_room = models.CharField( max_length=100)
    Labservices_Services = models.CharField( max_length=100)
    Labservices_Rating = models.ManyToManyField(Ratings,related_name='Labservices_Rating')
    Housekeeping_Services = models.CharField( max_length=100)
    Housekeeping_Rating = models.ManyToManyField(Ratings,related_name='Housekeeping_Rating')
    Security_Services = models.CharField( max_length=100)
    Security_Rating = models.ManyToManyField(Ratings,related_name='Security_Rating')
    Discharge_Formality_Services = models.CharField( max_length=100)
    Discharge_Formality_Rating = models.ManyToManyField(Ratings,related_name='Discharge_Formality_Rating')
    Overall_satisfaction_Services = models.CharField( max_length=100)
    Overall_satisfaction_Rating = models.ManyToManyField(Ratings, related_name='Overall_satisfaction_Rating')
    Why_to_choose_this_hospital = models.CharField( max_length=100)
    Why_not_to_choose_this_hospital = models.CharField( max_length=100)
    Doctor_Feedback_Services = models.CharField( max_length=100)

    def __str__(self):
        return str(self.Employee_Id) + "----" + str(self.Patient_Name) + "----" + str(self.Date)


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    Subject = models.CharField(max_length=500)

    def __str__(self):
        return str(self.Name)