<h1>Mathematical Function</h1>

## Index
- [Description](#description)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Getting started with Poetry and useful commands](#getting-started-with-poetry-and-useful-commands)
- [Configuration with IDE](#configuration-with-ide)
- [How to execute the project](#how-to-execute-the-project)
- [How to execute the Unit tests](#how-to-execute-the-unit-tests)

### Description
The aim of this project are:
- introduce the use of Poetry
- calculate the perimeter and area of some polygons (rectangle and square) based on the user input

### Architecture
The architecture of the project is the following:
<p align="center">
  <img src="img/architecture.png?raw=true" />
</p>

- _Polygon_ class with two abstract methods
- _Rectangle_ class with perimeter and area implementation
- _Square_ class for the square polygon

In the main there are two functions which they are called in according to the user input:
- calculation_for_rectangle
- calculation_for_square

### Requirements
- Python v3.10
- Poetry v1.8.2

### Getting started with Poetry and some useful commands

To install Poetry on Windows environment you should run the following command from PowerShell:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

$Env:Path += ";C:\Users\<USER>\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
```

You can check if poetry has been installed with the following command:
```bash
poetry --version
```

You can create a new project with the following command:
```bash
poetry new <project-name>
```
The command will create a new poetry project with a _pyproject.toml_. In order to add new dependencies you can run the following command:
```bash
poetry add <library-name>
poetry install
```

Official documentation: https://python-poetry.org/

### Configuration with IDE
If you want configure this project from Intellij IDEA you can follow the following [link](https://www.jetbrains.com/help/idea/poetry.html#poetry-env).

### How to execute the project

To execute the code:
```bash
poetry run script
#Enter a polygon ((1) --> rectangle, (2) --> square or (3) --> circle): 1
#Enter the base length: 3
#Enter the height length: 4
#The area of the rectangle is 12.0
#The perimeter of the rectangle is 14.0
```
After the run of _poetry run script_ you can enter the inputs that you want!

### How to execute the Unit tests
To execute the unit test:

```bash
poetry run test
```
If you want to know the coverage of the unit test you can run the command:
```bash
poetry run python -m coverage run -m unittest
poetry run python -m coverage report #html
```
