from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from apps.profiling.models import UserProfile, TraitVector

@receiver(post_save, sender=CustomUser)
def create_user_profile_and_traits(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        TraitVector.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile_and_traits(sender, instance, **kwargs):
    instance.profile.save()
    instance.trait_vector.save()