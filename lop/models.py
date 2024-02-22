from django.db import models

class PDFFile(models.Model):
    pdf = models.FileField(upload_to='pdfs/')

class LogoImage(models.Model):
    logo = models.ImageField(upload_to='logos/')