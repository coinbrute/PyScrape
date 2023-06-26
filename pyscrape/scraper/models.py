from django.db import models
from django.contrib.auth.models import User

''' 
Represents a web scraping task. 

It's linked to a User, and includes the URL to scrape, 
the type of data to scrape, the schedule for the task, 
the status of the task (e.g., 'pending', 'running', 'complete', 'error'), 
and the result of the task.
'''
class ScrapingTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    data_type = models.CharField(max_length=200)
    schedule = models.DateTimeField()
    status = models.CharField(max_length=200, default='pending')
    result = models.TextField(blank=True)

'''
Represents a notification for a user. 

It's linked to a User, 
and includes the message of the notification, 
the date it was created, and whether it has been read.
'''
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    read = models.booleanField(default=False)

'''
Represents a pricing plan. 

It includes the name of the plan, 
the price, and the features included in the plan.
'''
class Pricing(models.Model):
    plan_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField()

'''
Represents a user's subscription to a pricing plan. 

It's linked to a User and a Pricing plan, 
and includes the start and end dates of the subscription.
'''
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()