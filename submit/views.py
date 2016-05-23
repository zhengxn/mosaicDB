from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from .forms import UploadFileForm
from django.template.loader import get_template
from .dbutil import insert, var, pub, ind, insert

def submit(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            type = form.cleaned_data['choice_field']
            if type == 'var':
                message = var(request.FILES['file'])
            elif type == 'pub':
                message = pub(request.FILES['file'])
            elif type == 'ind':
			    message = ind(request.FILES['file'])
            else:
                message = insert(request.FILES['file'])
#            file=insert(request.FILES['file'])
            return HttpResponse(message)
    else:
        form = UploadFileForm()
    if not request.user.is_authenticated():
        return render_to_response('submission_user.html')
    return render_to_response('submission.html',{'form':form},context_instance=RequestContext(request))

def read_file(f):
    file = ''
    num = 0
    for chunk in f.chunks():
        for line in chunk.split('\n'):
            if len(line.split()) > 0:
                ind, varid, gene, chrom, start, end, met, dis = line.split()
                file += ind
            else:
                continue
    return file
#    with open('example','wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)
#    return 'yes'
