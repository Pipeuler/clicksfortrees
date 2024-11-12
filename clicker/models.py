
from django.db import models
from django.contrib.auth.models import User

class TreeType(models.Model):
    name = models.CharField(max_length=100)
    skin_image = models.ImageField(upload_to='skins/')  # Imagen de la skin

    def __str__(self):
        return self.name

class Planting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree_type = models.ForeignKey(TreeType, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} planted {self.tree_type.name}"

class Reward(models.Model):
    tree_type = models.ForeignKey(TreeType, on_delete=models.CASCADE)
    required_plantings = models.PositiveIntegerField()  # Ej. 100 plantaciones para desbloquear
    unlocked_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"Reward for {self.required_plantings} plantings of {self.tree_type.name}"

