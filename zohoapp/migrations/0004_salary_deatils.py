# Generated by Django 4.2.8 on 2023-12-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0003_remove_payroll_placeofsupply'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary_deatils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_mail', models.EmailField(max_length=254)),
                ('employee_id', models.CharField(blank=True, max_length=20, null=True)),
                ('Desigination', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_salary', models.IntegerField(blank=True, null=True)),
                ('employee_joindate', models.DateField(blank=True, null=True)),
                ('employee_salarydate', models.DateField(blank=True, null=True)),
                ('employee_month', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_holiday', models.IntegerField(blank=True, null=True)),
                ('employee_workingday', models.IntegerField(blank=True, null=True)),
                ('employee_year', models.IntegerField(blank=True, null=True)),
                ('employee_leave', models.IntegerField(blank=True, null=True)),
                ('employee_casual_leave', models.IntegerField(blank=True, null=True)),
                ('employee_basicsalary', models.IntegerField(blank=True, null=True)),
                ('employee_Allowance', models.IntegerField(blank=True, null=True)),
                ('employee_HRA', models.IntegerField(blank=True, null=True)),
                ('employee_otherall', models.IntegerField(blank=True, null=True)),
                ('employee_Bonus', models.IntegerField(blank=True, null=True)),
                ('employee_Tsalary', models.IntegerField(blank=True, null=True)),
                ('employee_discription', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
