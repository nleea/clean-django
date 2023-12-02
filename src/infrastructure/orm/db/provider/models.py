# coding: utf-8

from django.core.exceptions import ValidationError
from django.db import models

from src.infrastructure.clients.provider.utils import get_drivers_names
from src.domain.provider import ProviderEntity, ProviderSettingEntity
from src.infrastructure.orm.db.provider.constants import SETTING_TYPE_CHOICES


class Provider(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False, unique=True)
    driver = models.CharField(max_length=25, blank=False, null=False, unique=True)
    priority = models.PositiveSmallIntegerField(blank=False, null=False, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "provider"
        verbose_name_plural = "providers"
        ordering = ("priority",)

    def __str__(self) -> str:
        return ProviderEntity.to_string(self)

    def clean(self):
        if self.driver not in get_drivers_names():
            raise ValidationError({"driver": "Invalid driver name"})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class ProviderSetting(models.Model):
    provider = models.ForeignKey(
        Provider, db_index=True, on_delete=models.CASCADE, related_name="settings"
    )
    setting_type = models.CharField(max_length=10, choices=SETTING_TYPE_CHOICES)
    key = models.SlugField(max_length=64, blank=False, null=False)
    value = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "provider setting"
        verbose_name_plural = "provider settings"
        unique_together = ("provider", "key")

    def __str__(self) -> str:
        return ProviderSettingEntity.to_string(self)
