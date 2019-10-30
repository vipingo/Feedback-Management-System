# Generated by Django 2.1.7 on 2019-05-07 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Subject', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Criticality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('criticality', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Date', models.DateField()),
                ('Employee_Id', models.IntegerField()),
                ('Patient_Name', models.CharField(max_length=30)),
                ('Primary_Diagnosis', models.CharField(max_length=100)),
                ('Stay_Expected', models.IntegerField()),
                ('Date_of_Issue', models.DateTimeField()),
                ('Admission_Date', models.DateField()),
                ('Discharge_On', models.DateField()),
                ('Diagnosis_by_Hospital', models.TextField()),
                ('Admin_Doctor', models.CharField(max_length=100)),
                ('Post_hospital_treatment_visit_frequency', models.CharField(max_length=30)),
                ('Services_Reception', models.CharField(max_length=100)),
                ('Services_Doctorduty', models.CharField(max_length=100)),
                ('Services_Bloodbank', models.CharField(max_length=100)),
                ('OT_Services', models.CharField(max_length=100)),
                ('Services_Nursingcare', models.CharField(max_length=100)),
                ('OPD_Services', models.CharField(max_length=100)),
                ('Pharmacy_Services', models.CharField(max_length=100)),
                ('Pharmacy_Services_Supply_to_room', models.CharField(max_length=100)),
                ('Labservices_Services', models.CharField(max_length=100)),
                ('Housekeeping_Services', models.CharField(max_length=100)),
                ('Security_Services', models.CharField(max_length=100)),
                ('Discharge_Formality_Services', models.CharField(max_length=100)),
                ('Overall_satisfaction_Services', models.CharField(max_length=100)),
                ('Why_to_choose_this_hospital', models.CharField(max_length=100)),
                ('Why_not_to_choose_this_hospital', models.CharField(max_length=100)),
                ('Doctor_Feedback_Services', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_doc_Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Hospital_doc_id', models.TextField()),
                ('Hospital_doc_name', models.TextField()),
                ('From', models.DateField()),
                ('To', models.DateField()),
                ('doc_speciality', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Master',
            fields=[
                ('Hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hospital_name', models.TextField()),
                ('Address', models.TextField()),
                ('Location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Speciality', models.TextField()),
                ('Hospital_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Hospital_Master')),
            ],
        ),
        migrations.CreateModel(
            name='Ongc_Doc_Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_id', models.IntegerField()),
                ('Doc_name', models.TextField()),
                ('Location', models.TextField()),
                ('From', models.DateField()),
                ('To', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ongc_Employee_Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.TextField()),
                ('relation', models.TextField()),
                ('location', models.TextField()),
                ('From', models.DateField()),
                ('To', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Primary_Hospital_Diagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Diagnosis', models.TextField()),
                ('Doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Hospital_doc_Master')),
            ],
        ),
        migrations.CreateModel(
            name='Primary_Ongc_Diagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Diagnosis', models.TextField()),
                ('Employee_id', models.IntegerField(unique=True)),
                ('Doc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Ongc_Doc_Master')),
                ('id_Criticality', models.ForeignKey(on_delete=None, to='Projectapp.Criticality')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure_Diagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_id', models.TextField(unique=True)),
                ('Procedure_id', models.TextField()),
                ('Diagnosis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Relation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relief_Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ongc_employee_master',
            name='Employee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.UserProfileInfo'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Bloodbank_Rating',
            field=models.ManyToManyField(related_name='Bloodbank_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Discharge_Formality_Rating',
            field=models.ManyToManyField(related_name='Discharge_Formality_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Doctor_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Ongc_Doc_Master'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Doctorduty_Rating',
            field=models.ManyToManyField(related_name='Doctorduty_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Hospital_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Hospital_Master'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Housekeeping_Rating',
            field=models.ManyToManyField(related_name='Housekeeping_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Labservices_Rating',
            field=models.ManyToManyField(related_name='Labservices_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Nursingcare_Rating',
            field=models.ManyToManyField(related_name='Nursingcare_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='OPD_Rating',
            field=models.ManyToManyField(related_name='OPD_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='OT_Rating',
            field=models.ManyToManyField(related_name='OT_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Overall_satisfaction_Rating',
            field=models.ManyToManyField(related_name='Overall_satisfaction_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Pharmacy_Rating',
            field=models.ManyToManyField(related_name='Pharmacy_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Reception_Rating',
            field=models.ManyToManyField(related_name='Reception_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projectapp.Relation'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Security_Rating',
            field=models.ManyToManyField(related_name='Security_Rating', to='Projectapp.Ratings'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='id_Criticality',
            field=models.ForeignKey(on_delete=None, to='Projectapp.Criticality'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='id_Relief_Status',
            field=models.ForeignKey(on_delete=None, to='Projectapp.Relief_Status'),
        ),
    ]