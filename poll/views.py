from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

"""def index(request):
    question_list = Question.objects.order_by('pub_date')[:5]

    context = {'question_list': question_list}
    return render(request, 'index.html', context)"""

"""def detail(request, pk):
    question = get_object_or_404(Question , pk=pk)

    context = {'question': question}
    return render(request, 'detail.html', context)"""

def vote(request, pk):
    # Grab the object and if the object doesnt exist raise an Error
    question = get_object_or_404(Question, pk=pk)
    try:
        # Collect the selected choice from the form
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        context = {'question':question, 'error_message': "You didn't select a choice."}
        return render(request, 'vote.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('result', args=(question.id,)))



"""def results(request, pk):
    question = get_object_or_404(Question, pk=pk)

    context = {'question': question}
    return render(request, 'result.html', context)"""


# Generic View
"""
Something about Generic view is that they have pre-defined functions to do certain things
that would have taken 7 - 8 lines of code, an example is the "ListView" and "DetailView" and there are more
"""
class index(generic.ListView):
    # We are telling the view to use the template specified belows
    template_name = 'index.html'
    # This is the same as the context in the function view
    context_object_name = 'question_list'

    # An helper function that will get the latest questions and it must be get_Queryset
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class detail(generic.DetailView):
    model = Question
    template_name = 'detail.html'

class result(generic.DetailView):
    model = Question
    template_name = 'result.html'