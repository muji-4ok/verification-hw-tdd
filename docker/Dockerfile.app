FROM python:3.11-alpine as bookstore-app-base

WORKDIR /app

COPY . /app/

FROM bookstore-app-base as bookstore-app-test

ENV PATH_TO_COVERAGE="/app/cov"
ENV PATH_TO_PROFILE="/app/prof"

RUN pip install --no-cache-dir -r requirements/dev.txt

CMD python -m pytest --cov-branch --cov libstore --cov-report "html:${PATH_TO_COVERAGE}" --profile --pstats-dir "${PATH_TO_PROFILE}"

FROM bookstore-app-base as bookstore-app-test-mypy

RUN pip install --no-cache-dir -r requirements/dev.txt

ENV PATH_TO_MYPY_RESULTS="/app/mypy"

CMD python -m mypy libstore --txt-report "${PATH_TO_MYPY_RESULTS}"
