from django.shortcuts import render


# Страница "О проекте"
def about(request):
    return render(request, 'pages/about.html')


# Страница "Правила использования"
def rules(request):
    return render(request, 'pages/rules.html')