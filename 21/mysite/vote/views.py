from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Question № " % question_id)

def results(request, question_id):
    response = "Results of question №."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting question № " % question_id)
