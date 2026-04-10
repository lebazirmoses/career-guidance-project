from django.contrib import admin
from .models import TraitVector, Career

@admin.register(TraitVector)
class TraitVectorAdmin(admin.ModelAdmin):
    list_display = ('user', 'logical_reasoning', 'numerical_aptitude', 'confidence_score')

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'min_education')