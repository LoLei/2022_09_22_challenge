#!/bin/sh

black --check . &&
    mypy . &&
    python -m pytest
