from django.db import models
from datetime import datetime as dt
from django.conf import settings
from django.contrib.auth.models import User

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
class Post(models.Model):

    title = models.CharField(
        verbose_name="Заголовок", 
        max_length=30,
        blank=False,  
    )

    description = models.TextField(
        verbose_name="Описание",  
    )

    photo_before = models.ImageField(
        verbose_name="Фото до",
        upload_to="photos_for_posts/",
        blank=True,  
    )

    photo_after = models.ImageField(
        verbose_name="Фото после",
        upload_to="photos_for_posts/",
        blank=True,  
    )

    cover_photo = models.ImageField(
        verbose_name="Обложка",
        upload_to="photos_for_posts/",
        blank=True,  
    )

    latitude = models.FloatField(
        verbose_name="Широта",
        blank=True,
        null=True
    )

    longitude = models.FloatField(
        verbose_name="Долгота",
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        'Command',
        verbose_name="Команда создателей",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def save(self, *args, **kwargs):
        if not self.cover_photo:
            self.cover_photo = self.photo_after or self.photo_before
        super().save(*args, **kwargs)

class Person(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=50,
        blank=False,
    )
    specialization = models.CharField(
        verbose_name="Специализация/группа",
        max_length=50,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to="photos_for_people/",
        blank=False,
    )

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return self.name

class Command(models.Model):
    command_name = models.CharField(
        verbose_name="Название команды",
        max_length=32,
        blank=False,
    )
    members = models.ManyToManyField(
        Person,
        verbose_name="Участники",
        blank=False,
        related_name="commands"
    )
    team_photo = models.ImageField(
        verbose_name="Фотография команды",
        upload_to="photos_for_teams/",
        blank=True,
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return self.command_name

    def save(self, *args, **kwargs):
        if self.pk is None: 
            super().save(*args, **kwargs)
        if self.members.count() > 6:
            raise ValueError("Команда не может содержать более 6 участников")
        super().save(*args, **kwargs)

class Questions(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=40,
        blank=False,
    )

    phone_number = models.CharField(
        verbose_name="Номер телефона",
        max_length=11,
        blank=False,
    )

    question = models.TextField(
        verbose_name="Вопрос",
        max_length=1000,
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    
    def __str__(self):
        return self.question


