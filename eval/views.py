from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone, translation
from .models import User
from .models import Evaluation
from .models import Criteria
from django.db.models import Q
from django.conf import settings

# child home page
def index(request):
    childs = User.objects.all().filter(user_type='C').order_by('-score')
    template = loader.get_template('index.html')
    context = {
        'childs' : childs,
        'redirect_to' : request.path,
    }
    return HttpResponse(template.render(context, request))

# evaluation form page
def evaluation(request , child_id, message=''):
    currentChild = get_object_or_404(User, id=child_id)
    # check if the request is post
    if 'criteria' in request.POST:
        try:
            currentCriteria = Criteria.objects.get(id=request.POST['criteria'])
        except (KeyError, Criteria.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'evaluation.html', {
                'child': currentCriteria,
                'error_message': "You didn't select a criteria.",
            })
        else:
            newEvaluation = Evaluation(child=currentChild, 
            score=currentCriteria.suggested_score, 
            criteria=currentCriteria, 
            criteria_category=currentCriteria.criteria_category, 
            created_at=timezone.now())
            currentChild.score += newEvaluation.score
            currentChild.save()
            newEvaluation.save()
            success_message = "Evaluation Done"
            return HttpResponseRedirect(reverse('eval:evaluation_message', args=(currentChild.id,success_message)))

    # if the request get
    else:
        criterias = Criteria.objects.all()
        template = loader.get_template('evaluation.html')
        context = {
            'child' : currentChild,
            'criterias' : criterias,
            'success_message' : message,
            'redirect_to' : request.path,
        }
        
        return HttpResponse(template.render(context, request))
    

# child details page
def childDetails(request, child_id, message=''):
    child = User.objects.all().filter(id=child_id)
    evaluations = Evaluation.objects.all().filter(child=child_id)
    if 'UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==' in request.path:
        template = loader.get_template('parent_child_detail.html')
        print ("Good")
    else:
        template = loader.get_template('child_detail.html')
    context = {
        'child' : child,
        'evaluations' : evaluations,
        'success_message' : message,
        'redirect_to' : request.path,
    }
    return HttpResponse(template.render(context, request))

# parent Index page
def parentIndex(request):
    childs = User.objects.all().filter(user_type='C').order_by('-score')
    template = loader.get_template('parent_index.html')
    context = {
        'childs' : childs,
        'redirect_to' : request.path,
    }
    return HttpResponse(template.render(context, request))


def score_calculator(child_ids):
    sum = 0
    child_evaluations =  Evaluation.objects.all().filter(child_id = child_ids)
    for evaluation in child_evaluations:
        sum += evaluation.score
    return sum

def evaluationDelete(request, evaluation_id):
    evaluation =  get_object_or_404(Evaluation, id=evaluation_id)
    old_score = evaluation.score
    child = User.objects.get(id=evaluation.child.id)
    evaluation.delete()
    child.score -= old_score
    child.save()
    success_message = "Evaluation deleted"
    return HttpResponseRedirect(reverse('eval:detail_parent_message', args=(child.id,success_message)))

def setLanguage(request):
    childs = User.objects.all().filter(user_type='C').order_by('-score')
    template = loader.get_template('index.html')
    context = {
        'childs' : childs,
    }
    user_language = request.POST['language']
    translation.activate(user_language)
    print (request.POST['next'])
    response = HttpResponseRedirect(request.POST['next'])
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
