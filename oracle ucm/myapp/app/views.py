from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import UploadedFile, ProcessDetail
# import requests

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            # Trigger Oracle Fusion UCM process
            response = trigger_ucm_process(uploaded_file.file.path)
            if response['status'] == 'error':
                ProcessDetail.objects.create(
                    request_id=response['request_id'],
                    file_name=uploaded_file.file.name,
                    process_id=response['process_id'],
                    status='error',
                    error_message=response['error_message']
                )
            else:
                ProcessDetail.objects.create(
                    request_id=response['request_id'],
                    file_name=uploaded_file.file.name,
                    process_id=response['process_id'],
                    status='success'
                )
            return redirect('process_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def process_list(request):
    processes = ProcessDetail.objects.all()
    return render(request, 'process_list.html', {'processes': processes})

def trigger_ucm_process(file_path):
    # Replace with actual API call to Oracle Fusion UCM
    # Mock response for illustration
    response = {
        'request_id': '12345',
        'process_id': '67890',
        'status': 'error',
        'error_message': 'Sample error message'
    }
    return response
