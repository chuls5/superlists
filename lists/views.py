from django.shortcuts import render

def home_page(request):
    new_item_text = ''
    if request.method == "POST":
        new_item_text = request.POST.get('item_text', '')

    return render(request, 'home.html', {'new_item_text': new_item_text})
