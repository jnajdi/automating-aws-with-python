#!/bin/sh
pyflakes webotron/
pycodestyle webotron/
pydocstyle webotron/
pylint webotron/

