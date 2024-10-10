from django.db import models
import pandas as pd
import openpyxl

# Create your models here.
class Items(models.Model):

    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    
    def __str___(self):

        return self.name
    
class Users(models.Model):

    # id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    psw1 = models.CharField(max_length=200)
    
    def __str___(self):

        return self.uname

from django.core.files.storage import FileSystemStorage

class DocTitle(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='docs/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.document:  # Check if there is a document uploaded
            self.read_excel_and_create_students()

    def read_excel_and_create_students(self):
        wb = openpyxl.load_workbook(self.document.path)
        sheet = wb.active
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, age, grade = row  # Adjust according to your Excel structure
            # StudentDet.objects.create(doc_title=self, name=name, age=age, grade=grade)

            # Check if the student already exists
            StudentDet.objects.update_or_create(
                doc_title=self,
                name=name,
                defaults={'age': age, 'grade': grade}
            )
    
class StudentDet(models.Model):
    doc_title = models.ForeignKey(DocTitle, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=10)

    class Meta:
        unique_together = ('doc_title', 'name')  # Ensures unique name per document

    def __str__(self):
        return self.name


