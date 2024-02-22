from django.shortcuts import render
from .forms import LogoForm
from .utils import add_logo_to_pdf

def add_logo_view(request):
    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            logo = request.FILES['logo']
            output_pdf_path = f'media/pdfs/output_{pdf_file.name.split(".")[0]}.pdf'

            try:
                add_logo_to_pdf(pdf_file, output_pdf_path, logo)
                return render(request, 'result.html', {'output_pdf_path': output_pdf_path})
            except Exception as e:
                error_message = f"Error: {e}"
                return render(request, 'error.html', {'error_message': error_message})
    else:
        form = LogoForm()

    return render(request, 'add_logo.html', {'form': form})
