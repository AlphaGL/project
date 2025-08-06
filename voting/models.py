from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Position(models.Model):
    name = models.CharField(max_length=100)
    importance = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class StudentManager(BaseUserManager):
    def create_user(self, reg_number, full_name, password=None):
        if not reg_number:
            raise ValueError('The Registration Number must be set')
        student = self.model(reg_number=reg_number, full_name=full_name)
        student.set_password(password)  # Use set_password to handle hashing
        student.save(using=self._db)
        return student

    def create_superuser(self, reg_number, full_name, password=None):
        if not reg_number:
            raise ValueError('The Registration Number must be set')
        student = self.create_user(
            reg_number=reg_number,
            full_name=full_name,
            password=password
        )
        student.is_staff = True
        student.is_superuser = True
        student.save(using=self._db)
        return student

class Student(AbstractBaseUser):
    reg_number = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'reg_number'
    REQUIRED_FIELDS = ['full_name']

    objects = StudentManager()

    def __str__(self):
        return self.full_name

    def has_voted_for_position(self, position):
        return Vote.objects.filter(student=self, position=position).exists()

    def get_remaining_positions(self):
        voted_positions = Vote.objects.filter(student=self).values_list('position_id', flat=True)
        return Position.objects.exclude(id__in=voted_positions).order_by('importance')

class Contestant(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contestants/', default='default-contestant.jpg')

    def __str__(self):
        return f"{self.name} - {self.position.name}"


class Vote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'position'], name='unique_vote_per_position')
        ]

    def __str__(self):
        return f"{self.student.full_name} voted for {self.contestant.name} in {self.position.name}"

    @classmethod
    def validate_vote(cls, student, position):
        return cls.objects.filter(student=student, position=position).exists()