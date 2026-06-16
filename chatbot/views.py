from django.shortcuts import render
from .ai import ask_ai

def chat(request):
    answer=""
    
    if request.method == "POST":
        question = request.POST.get("question")
        answer = ask_ai(quetion)
        
    return render(request, "chat.html", {"answer": answer})

