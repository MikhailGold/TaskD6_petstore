from django.db import models
from django.core import validators
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Animal(models.Model):
    animaltype = models.CharField(max_length=15, unique=True, verbose_name='Вид животного')
    animaltype_slug = models.SlugField(max_length=15, verbose_name='Вид животного для URL')
    animalphoto = models.ImageField(upload_to='animals_photos', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.animalType
    
    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'

class AnimalBreed(models.Model):
    breed = models.CharField(max_length = 64, unique=True, verbose_name='Порода')
    breed_slug = models.SlugField(max_length=64, null=True, blank=True, default=None, verbose_name='Порода животного для URL')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animal_breed', default=None, verbose_name='Вид животного')
    breedphoto = models.ImageField(upload_to='breed_photos', blank=True, verbose_name='Фото породы')


    def __str__(self):
        return f'{self.breed} ({self.animal})'

    class Meta:
        verbose_name = 'Порода животного'
        verbose_name_plural = 'Породы животных'

class Pet(models.Model):
    LOCATION = (
        (True, 'В приюте'),
        (False, 'Вне приюта')
    )

    POL_ANIMAL = (
        ('m', 'Мальчик'),
        ('f', 'Девочка')
    )

    nickname = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.ForeignKey(AnimalBreed, on_delete=models.CASCADE, related_name='pet_breed', default=None, verbose_name='Порода')
    age = models.IntegerField(validators=[validators.MaxValueValidator(30)], verbose_name='Возраст')
    pol = models.CharField(choices=POL_ANIMAL, max_length=1, verbose_name='Пол', null=True, default='m')
    description = models.TextField(default=None, verbose_name='Описание')
    date_registration = models.DateTimeField(default=timezone.now, verbose_name='Данные регистрации')
    petphoto = models.ImageField(upload_to='pets_photos', blank=True, verbose_name='Фото питомца')
    holdplace = models.BooleanField(choices=LOCATION, default=True, verbose_name='Местонахождение')


    def __str__(self):
        return f'{self.breed} - кличка {self.nickname}'

    
    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

