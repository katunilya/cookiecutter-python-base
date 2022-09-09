# Cookiecutter Python Base

Simplistic Python3.9 project with some basic development setup.

To create a new project run:

```sh
cookiecutter https://gitlab.com/ds.team/general/cookiecutter-python-base
```

## For Developers

- Create virtual environment for Python3.9:

```sh
python3.9 -m venv .venv
```

- For VS Code useres: Select Interpreter

- Install dependencies with `poetry`:

```sh
poetry install
```

- After installing dependencies we recommend updating their versions:

```sh
poetry update
```

- For testing purposes VS Code task "Test" was configured (cleans tests folder
  from previous tests and generates new project with default parameters)
