from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# import os


class Student(models.Model):
    # Link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields for Student
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='students/images/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)  # Optional date of birth
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number
    enrolled_date = models.DateField(auto_now_add=True)  # Date when the student is added

    def __str__(self):
        return f"{self.user.username} ({self.user.first_name} {self.user.last_name})"

class Course(models.Model):
    # Fields for the Course model
    course_code = models.CharField(max_length=20, unique=True)  # Unique course code
    course_name = models.CharField(max_length=100)  # Name of the course
    course_description = models.TextField(blank=True)  # Optional description of the course

    def __str__(self):
        return f"{self.course_code}: {self.course_name}"

class Registered(models.Model):
    # ForeignKey linking to the User model (many-to-one relationship)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # ForeignKey linking to the Course model (many-to-one relationship)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    
    # Date and time when the registration occurred (optional)
    registered_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Ensure each user can only register once for a specific course

    def __str__(self):
        return f"{self.user.username} registered for {self.course.course_name}"