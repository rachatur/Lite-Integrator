from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProcessDetail(models.Model):
    request_id = models.CharField(max_length=100)
    file_name = models.CharField(max_length=255)
    process_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
