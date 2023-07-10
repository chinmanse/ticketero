#!/bin/bash
echo $1
mkdir -p $1
cd $1

touch main.py
mkdir -p controllers
cd controllers
touch __init__.py
cd ..
mkdir -p middlewares
cd middlewares
touch __init__.py
cd ..
mkdir -p models
cd models
touch __init__.py
cd ..
mkdir -p requests
cd requests
touch __init__.py
cd ..
mkdir -p services
cd services
touch __init__.py
cd ..
mkdir -p tests
cd tests
touch __init__.py
cd ..
mkdir -p utils
cd utils
touch __init__.py
cd ..
mkdir -p routes
cd routes
touch __init__.py
cd ..