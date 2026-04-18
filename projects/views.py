from django.shortcuts import render
from .models import Project # This should be correct already

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


from .forms import ContactForm # Add this to your imports

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # For now, we'll just print it to the terminal. 
            # Later you can set up real email sending!
            print(f"New message from {form.cleaned_data['name']}: {form.cleaned_data['message']}")
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})



def journey_view(request):
    return render(request, 'journey.html')



from .models import Project, ContactMessage # Add ContactMessage to imports

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # This line saves the message to your database!
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})