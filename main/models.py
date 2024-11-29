from django.db import models
from django.core.validators import MinValueValidator


class Brand(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, unique=True)
    country = models.CharField(verbose_name='Country', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Phone(models.Model):
    brand = models.ForeignKey(Brand, verbose_name='Brand', on_delete=models.SET_NULL, null=True, related_name='phones')
    model = models.CharField(verbose_name='Model', max_length=255, unique=True)
    price = models.PositiveIntegerField(verbose_name='Price')
    color = models.CharField(verbose_name='Color', max_length=255)
    display_size = models.DecimalField(verbose_name='Display Size', max_digits=4, decimal_places=2, validators=[MinValueValidator(1)])
    made_in = models.CharField(verbose_name='Made In', max_length=255)
    is_available = models.BooleanField(verbose_name='Is Available', default=False)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'


