from django.shortcuts import render
from .ai import ask_ai

def chat(request):
    answer=""
    
    if request.method == "POST":
        question = request.POST.get("question")
        #print("Question:", question)
        answer = ask_ai(question)
       # print("Answer:", answer)
        
        
    return render(request, "chat.html", {"answer": answer})

