# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Gettings Started

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

- To add package or make package production one (packages for data science are
  in `dev` section) use:

```sh
poetry add <package>
```

- More about Poetry commands you can read on their [documentation
  page](https://python-poetry.org/docs/cli/).

- Do not forget to initialize `pre-commit` after installing dependencies:

```sh
pre-commit install
```

- If you face problems with installing `pre-commit` git hooks follow
  instructions provided by the tool - usually it's enough to execute:

```sh
pre-commit autoupdate
```
