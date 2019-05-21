from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from uploader.models import Document
from uploader.forms import DocumentForm


def upload(request):
    """Return a page with a file upload form"""

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'File successfully uploaded.')

            return redirect('upload')
    else:
        form = DocumentForm()

    return render(request, 'uploader.html', {'form': form})


def files_list(request):
    """Return a list of existing files"""

    now = timezone.now()
    documents = Document.objects.filter(end_date__gt=now)
    return render(request, 'files_list.html', {'documents': documents})


def file_life_time(request, pk):
    """Return the lifetime of the file"""

    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.save()

    return render(request, 'file_life_time.html', {'document': document})


def delete_file(request, pk):
    """Return to the files list after deleting the file"""

    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()

        messages.success(request, 'File successfully deleted.')

    return redirect('files_list')


def file_not_exist(request, pk):
    """Return page 404 for non-existent file"""

    document = Document.objects.get(pk=pk)
    document.save()

    return render(request, 'file_not_exist.html', {'document': document})
