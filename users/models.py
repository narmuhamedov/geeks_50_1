from django.db import models
from django.contrib.auth.models import User

child_club = "Детский клуб"
teenager_club = "Подростковый клуб"
adult_club = "Взрослый клуб"

class CustomUser(User):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    phone_number = models.CharField(max_length=20)
    #Для обработки middlewares
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=10, choices=GENDER, default="Male")
    club = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.age < 7:
            self.club = "Ваш возраст должен быть больше 7"
        elif self.age >= 7 and self.age < 12:
            self.club = child_club
        elif self.age >= 12 and self.age < 18:
            self.club = teenager_club
        elif self.age >= 18 and self.age < 45:
            self.club = adult_club
        else:
            self.club = "Ваш возраст слишком высокий извините!"
        super().save(*args, **kwargs)