from django.shortcuts import render
from .forms import ContactForm

def home(request):
    context = {
        'page_title': 'الصفحة الرئيسية',
        'welcome_message': 'مرحبًا بكم في أمانة منطقة القصيم',
        'description': 'نسعى لتقديم أفضل الخدمات للمواطنين والمقيمين في منطقة القصيم'
    }
    return render(request, 'pages/home.html', context)

def report(request):
    context = {
        'page_title': 'التقارير',
        'reports': [
            {
                'title': 'تقرير الخدمات البلدية',
                'date': '2025-11-15',
                'description': 'تقرير شامل عن الخدمات البلدية المقدمة خلال الربع الأخير'
            },
            {
                'title': 'تقرير المشاريع التطويرية',
                'date': '2025-11-10',
                'description': 'نظرة عامة على المشاريع التطويرية الجارية في المنطقة'
            },
            {
                'title': 'تقرير النظافة والبيئة',
                'date': '2025-11-05',
                'description': 'تقرير حول مبادرات النظافة والحفاظ على البيئة'
            }
        ]
    }
    return render(request, 'pages/report.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return render(request, 'pages/contact.html', {
                'page_title': 'اتصل بنا',
                'form_submitted': True,
                'form': ContactForm()
            })

    return render(request, 'pages/contact.html', {
        'page_title': 'اتصل بنا',
        'form': form
    })

