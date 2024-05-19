# First steps

**GitHub**:

- Create a [new repository](https://github.com/new) with the name `flash_cards`.
- Enable the **doc** generation in the repository:
  - Settings -> Pages -> Source: Github Actions

**Local**:

- Initialize the repository:

```shell
git init --initial-branch=main
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:CIvanPiMa/flash_cards.git
git push -u origin main
```

- Use and push a development branch:

```shell
BRANCH_NAME=feat/initial_project_release
git checkout -b ${BRANCH_NAME}
git add .
git commit -m "feat: Add initial project structure"
git push --set-upstream origin ${BRANCH_NAME}
```

- Install the [pre-commit](https://pre-commit.com/#install) hooks:

```shell
pre-commit install --install-hooks --hook-type commit-msg
```

---

# Flash Cards

Tkinter UI to generate flash cards to study differents topics (right now languages)

- [Docs](https://civanpima.github.io/flash_cards/flash_cards.html).

## Installation

```shell
pip install flash_cards
```

## Usage

...TBD

## Contributing

Once cloned the repo, install the pre-commit hooks:

```shell
pre-commit install --install-hooks
```

Install the library (in a virtual environment) as an editable package with the development dependencies:

```shell
pip install -e ".[dev]"
```

### Documentation

- This library uses the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format for the docstrings.
- To generate the documentation, run:

```shell
pdoc src/flash_cards --mermaid --docformat numpy
```

### Testing

To run the tests:

```shell
pytest
```

new
