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

5) install the dependencies listed in pyproject.toml

`poetry install`

6) test if the package was installed under the current environment

`python -c "import ranboardom as rb; rb.board(10, 10, 'o')"`

7) to build the package use the following command in the root directory:

`poetry build`

8) this creates a folder called dist/ with the wheel and sdist, either can be used to install the package using

`cd dist`
`pip install ranboardom-0.1.0-py3-none-any.whl`

9) we need to add TestPyPI to the list of repositories poetry knows abouy (only needed when publishing dummy or test releases)

`poetry config repositories.test-pypi https://test.pypi.org/legacy/`

10) publish the built package to TestPyPi (this requries a token, which can be generated following 

[this guide](https://py-pkgs.org/02-setup#register-for-a-pypi-account-and-get-an-authentication-token))
`poetry publish -r test-pypi -u __token__ -p TOKEN_COMES_HERE`

The repository is uploaded under [here](https://test.pypi.org/project/ranboardom/)

11) installing the package should be possible from any device and environment (to tell pip to search also on test pypi, we need the following flags):

```shell
pip install --index-url https://test.pypi.org/simple/ \
--extra-index-url https://pypi.org/simple \
ranboardom
```

`--extra-index-url` is used to let pip know that not all dependencies are located under test pypi, but rather look for them under pypi

## Useful references

Guide for packaging your code:

`https://py-pkgs.org/03-how-to-package-a-python#packaging-your-code`
