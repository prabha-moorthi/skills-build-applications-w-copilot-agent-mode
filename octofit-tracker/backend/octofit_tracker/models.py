from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='_id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.email} - {self.type}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='_id')
    score = models.IntegerField()
    rank = models.IntegerField()
    def __str__(self):
        return f"{self.user.email} - {self.rank}"