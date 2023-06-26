from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ScrapingTask, Notification, Pricing, UserSubscription

'''
Renders the home page
'''
def home(request):
    return render(request, 'home.html')

'''
Renders the dashboard page
This page shows the user's scraping tasks and notifications.
'''
@login_required
def dashboard(request):
    tasks = ScrapingTask.objects.filter(user=request.user)
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'notifications': notifications
    })

'''
Renders a form for creating a new scraping task. 
In the future, this view will handle the form submission and create a new ScrapingTask object.
'''
@login_required
def create_task(request):
    # TODO: handle form submission to create new task
    # For now, just render an empty form
    return render(request, 'create_task.html')

'''
Renders a page for viewing a specific scraping task. 
This page could show the status, result, and other details of the task.
'''
@login_required
def view_task(request, task_id):
    task = ScrapingTask.objects.get(id=task_id)
    # ensure task belongs to logged in user
    if task.user != request.user:
        return HttpResponseForbidden()
    return render(request, 'view_task.html', {'task': task})

'''
Renders a page that shows the pricing plans
'''
def pricing(request):
    pricing_plans: Pricing.objects.all()
    return render(request, 'pricing.html', {'pricing_plans': pricing_plans})

'''
Renders a form for subscribing to a pricing plan.
In the future, this view will handle the form submission 
and create a new UserSubscription object.
'''
@login_required
def subscribe(request, pricing_id):
    # TODO: handle the form submission to create a new subscription
    # For now, just render an empty form
    return render(request, 'subscribe.html')