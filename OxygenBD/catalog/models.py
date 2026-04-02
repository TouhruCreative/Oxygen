from django.db import models

"""
Model architecture

Category
 ├── name (CharField)
 ├── parent (FK → Category, null=True)

"""
# TODO complete parent
class Category(models.Model):

    name = models.CharField()
    parent = None
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("c")

    def str(self):
        return self.name