from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import LeadsForm
from .models import Leads
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LeadsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LeadsForm()

    leads = Leads.objects.all()

    paginator = Paginator(leads, 2) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj' : page_obj
    }
    return render(request, 'index.html', context)