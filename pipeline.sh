#!/bin/sh

# TODO: Use GitHub Actions

black --check . &&
    mypy . &&
    python -m pytest
