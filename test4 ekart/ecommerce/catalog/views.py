from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Product

def product_list(request):
    ob_products = Product.objects.all()
    return render(request, 'product_list.html', {'products': ob_products})

def product_detail(request, pk):
    ob_product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

def home(request):
    return render(request, 'home.html')

def generate_pdf(request):
    template_path = 'pdf_template.html'
    context = {'name': 'User', 'message': 'Hello! This is your PDF.'}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="document.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response