# Packaging python

This project serves as an example for building a python package and uploading to PyPi.

## Package usage

`import ranboardom as rb`

`rb.board()`

Which outputs something like this without any function arguments:

```{python}
[['e' '"' '*' '<' '*']
 ['*' '*' 'h' '*' '*']
 ['*' '*' 'o' '*' '*']
 ['7' '$' '*' '*' '*']
 ['*' 'w' '*' '*' '*']]
```

## Workflow for packaging

1) create a separate venv for poetry under the root_directory/venv for example
`python -m venv venv/packaging`

2) activate environment
`source venv/packaging/bin/activate`

3) install poetry, which will be used to build our code into a python package called ranboardom
`pip install -U pip setuptools`
`pip install poetry`

4) check installed version of poetry
`poetry --version`

5) install the dependencies listed in pyproject.toml and build the package
`poetry install`

6) test if the package was installed under the current environment
`python -c "import ranboardom as rb; rb.board(10, 10, 'o')"`

## Useful references

Guide for packaging your code:

`https://py-pkgs.org/03-how-to-package-a-python#packaging-your-code`
