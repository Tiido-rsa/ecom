from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def accept(request):
    
    if request.method == 'POST':
        name        = request.POST.get('name', '')
        email       = request.POST.get('email', '')
        phone       = request.POST.get('phone', '')
        summary     = request.POST.get('summary', '')
        degree      = request.POST.get('degree', '')
        university  = request.POST.get('university', '')
        school      = request.POST.get('school', '')
        experience  = request.POST.get('experience', '')
        skills      = request.POST.get('skills', '')
        
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, university=university, school=school, experience=experience, skills=skills)
        profile.save()

        return redirect(request.path)

    return render(request, 'pdf/accept.html')


def resume(request, id):
    profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'profile': profile})
       
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    # Try to use wkhtmltopdf path from settings if provided
    wkhtml_path = getattr(settings, 'WKHTMLTOPDF_CMD', None)
    config = None
    if wkhtml_path:
        try:
            config = pdfkit.configuration(wkhtmltopdf=wkhtml_path)
        except Exception:
            config = None

    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename="resume.pdf"
    context = {'profile': profile}
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

def list(request):
    profiles = Profile.objects.all()
    
    context = {'profiles': profiles}
    return render(request, 'pdf/list.html', context)