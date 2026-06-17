from django.shortcuts import render
from .ai import ask_ai
import markdown

def chat(request):
    answer= ""
    
    if request.method == "POST":
        question = request.POST.get("question")
        #print("Question:", question)
        answer = markdown.markdown(ask_ai(question))
       # print("Answer:", answer)
        
        
    return render(request, "chat.html", {"answer": answer})

