from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class RestaurantProfile(SingletonModel):
    name = models.CharField(max_length=128, blank=True)
    logo = models.ImageField(upload_to="logo", blank=True)
    about_us = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    # opening_hours = models.ManyToManyField("OpeningHour", blank=True)

    def __str__(self) -> str:
        return f"{self.name} Profile"

    class Meta:
        verbose_name_plural = "Profiles"


class OpeningHour(models.Model):
    DAYS = (
        (0, "Senin"),
        (1, "Selasa"),
        (2, "Rabu"),
        (3, "Kamis"),
        (4, "Jumat"),
        (5, "Sabtu"),
        (6, "Minggu"),
    )
    day = models.PositiveSmallIntegerField(choices=DAYS, unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        ordering = ("day",)

    def __str__(self):
        return f"{self.get_day_display()}: {self.opening_time} - {self.closing_time}"


class RestaurantFAQ(models.Model):
    question = models.CharField(max_length=128)
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name_plural = "FAQs"
