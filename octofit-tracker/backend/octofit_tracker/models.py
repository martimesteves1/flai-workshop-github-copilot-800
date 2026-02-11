from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    distance = models.FloatField(null=True, blank=True)  # in km
    date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.date}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100)
    team_name = models.CharField(max_length=200)
    total_calories = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    total_distance = models.FloatField(default=0.0)
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user_name} - Rank {self.rank}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    instructions = models.TextField()

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
