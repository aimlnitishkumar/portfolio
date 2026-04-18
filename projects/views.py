from django.shortcuts import render
from .models import Project, ContactMessage
from .forms import ContactForm

from .models import Project, ContactMessage, GuestbookMessage # Add GuestbookMessage

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project_index.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def journey_view(request):
    return render(request, 'journey.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            return render(request, 'contact_success.html')
    return render(request, 'contact.html', {'form': form})





def guestbook_view(request):
    messages = GuestbookMessage.objects.all().order_by('-created_at') # Newest first
    if request.method == 'POST':
        author = request.POST.get('author')
        body = request.POST.get('body')
        if author and body:
            GuestbookMessage.objects.create(author=author, body=body)
            # After posting, we show the updated list
    
    return render(request, 'guestbook.html', {'messages': messages})