from django.db import models

# FEATURE
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# STATS
class Stat(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# TESTIMONIAL
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


# FAQ
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.title
    
class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Development', 'Development'),
        ('Marketing', 'Marketing'),
        ('Design', 'Design'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    instructor = models.CharField(max_length=100)
    image = models.ImageField(upload_to='courses/')
    progress = models.IntegerField(default=0)
    lessons_completed = models.IntegerField(default=0)
    total_lessons = models.IntegerField(default=100)
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Completed', 'Completed')],
        default='Active'
    )

    def __str__(self):
        return self.title
    
class Participant(models.Model):
    image = models.ImageField(upload_to='participants/')

class Session(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    participants = models.ManyToManyField(Participant)