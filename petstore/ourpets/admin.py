from django.contrib import admin

# Register your models here.

from ourpets.models import Animal, AnimalBreed, Pet

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animaltype', 'animaltype_slug')
    prepopulated_fields = {'animaltype_slug': ('animaltype',)}
    ordering = ('animaltype',)


@admin.register(AnimalBreed)
class AnimalBreedAdmin(admin.ModelAdmin):
    list_display = ('animal', 'breed')
    ordering = ('animal', 'breed')
    raw_id_fields = ('animal',)
    prepopulated_fields = {'breed_slug': ('breed',)}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # list_display = ('name', 'breed')
    raw_id_fields = ('breed',)