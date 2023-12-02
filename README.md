# _Forex - Django Clean Architecture_

This repository contains the code for Forex API backend. The application aims to provide information for all currencies, latests and historical time series exchange rates for currency pairs, currency conversion and time weighted rates calculation.

## Documentation

This project has been developed using [Django][django] and [Django Rest Framework][djangorestframework], with [Celery][celery] as background tasks runner, [Postgres][postgres] as relational database and [Redis][redis] as cache service.

Code structure implementation follows a [Clean Architecture][cleanarchitecture] approach, emphasizing on code readability, responsibility decoupling and unit testing.

For API backend endpoints documentation refer to the [forex yaml][swagger] file in the docs directory.
