from django.contrib import admin
from .models import *
from .forms import *
import openpyxl
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib import messages

# Register your models here.

admin.site.register(Items)
admin.site.register(Users)

class StudentInline(admin.TabularInline):
    model = StudentDet
    extra = 1  # Allows adding one more student by default

class DocTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [StudentInline]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'doc_title')
    search_fields = ('name',)

admin.site.register(StudentDet, StudentAdmin)


admin.site.register(DocTitle, DocTitleAdmin)