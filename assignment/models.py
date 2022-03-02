from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Kid(models.Model):
    name = models.CharField("Kid Name", max_length=20)
    age = models.IntegerField("Kid Age")
    phone = models.CharField("Parent Phone Number", max_length=12)
    email = models.EmailField("Parent Email Address")
    def __str__(self):
        return self.name


class Image(models.Model):
    VEG = "Veg"
    UNKNOWN = "Unknown"
    FRUIT = "Fruit"
    GRAIN = "Grain"
    PROTEIN = "Protein"
    DAIRY = "Dairy"
    CONFECTIONARY = "Confectionary"

    FOOD_CHOICES = (
        ("1", VEG),
        ("2", FRUIT),
        ("3", GRAIN),
        ("4", PROTEIN),
        ("5", DAIRY),
        ("6", CONFECTIONARY),
        ("7", UNKNOWN),
    )

    kid = models.ForeignKey(
        Kid,
        on_delete=models.CASCADE,
    )
    url = models.URLField("Image URL")
    created_on = models.DateTimeField("Created On", auto_now_add=True)
    updated_on = models.DateTimeField("Updated On", auto_now=True)
    is_approved = models.BooleanField("Is Approved")
    approved_by = models.CharField("Approved by", max_length=20)
    food_group = models.CharField(
        "Food Group", max_length=20, choices=FOOD_CHOICES, default="1"
    )

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        if self.food_group == "7":
            send_mail(
                "Unknown Food Image Detected",
                f"The image {self.url} does not contain food.",
                settings.EMAIL_HOST_USER,
                [self.kid.email],
                fail_silently=False,
            )
        def __str__(self):
            return self.food_group
