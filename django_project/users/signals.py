from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def resize_image(sender, instance, **kwargs):
    if instance.image_to:
        image = Image.open(instance.image_to.path)
        max_size = 1000  # максимальный размер картинки в пикселях
        if image.width > max_size or image.height > max_size:
            image.thumbnail((max_size, max_size))
            image.save(instance.image_to.path)
