#!/bin/sh

cd /migrations &&
  poetry run alembic upgrade head
  cd /bpl-websocket-service &&
  poetry run pytest -vv -s tests --junitxml=/report/report.xml
