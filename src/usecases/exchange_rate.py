# coding: utf-8

import datetime
from typing import List

from src.domain.exchange_rate import CurrencyEntity, CurrencyExchangeRateEntity


class CurrencyInteractor:
    def __init__(self, currency_repo: object):
        self.currency_repo = currency_repo

    def get(self, code: str) -> CurrencyEntity:
        return self.currency_repo.get(code)

    def get_availables(self) -> List[CurrencyEntity]:
        return self.currency_repo.get_availables()

    def save(self, currency: CurrencyEntity):
        self.currency_repo.save(currency)

    def bulk_save(self, currencies: List[CurrencyEntity]):
        self.currency_repo.bulk_save(currencies)


class CurrencyExchangeRateInteractor:
    def __init__(self, exchange_rate_repo: object):
        self.exchange_rate_repo = exchange_rate_repo

    def get(
        self, source_currency: str, exchanged_currency: str, valuation_date: str
    ) -> CurrencyExchangeRateEntity:
        return self.exchange_rate_repo.get(
            source_currency, exchanged_currency, valuation_date
        )

    def get_latest(
        self, source_currency: str, exchanged_currency: str
    ) -> CurrencyExchangeRateEntity:
        today = datetime.date.today().strftime("%Y-%m-%d")
        return self.get(source_currency, exchanged_currency, today)

    def get_rate_series(
        self,
        source_currency: str,
        exchanged_currency: str,
        date_from: str,
        date_to: str,
    ) -> List[float]:
        return self.exchange_rate_repo.get_rate_series(
            source_currency, exchanged_currency, date_from, date_to
        )

    def get_time_series(
        self,
        source_currency: str,
        exchanged_currency: str,
        date_from: str,
        date_to: str,
    ) -> List[CurrencyExchangeRateEntity]:
        return self.exchange_rate_repo.get_time_series(
            source_currency, exchanged_currency, date_from, date_to
        )

    def save(self, exchange_rate: CurrencyExchangeRateEntity):
        self.exchange_rate_repo.save(exchange_rate)

    def bulk_save(self, exchange_rates: List[CurrencyExchangeRateEntity]):
        self.exchange_rate_repo.bulk_save(exchange_rates)
