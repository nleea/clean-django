from django.apps import AppConfig


class ExchangeRateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.infrastructure.orm.db.exchange_rate"
    label = "exchange_rate"
    verbose_name = "Exchange Rate"


class ProviderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.infrastructure.orm.db.provider"
    label = "provider"
    verbose_name = "Provider"
