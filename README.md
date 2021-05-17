# python-tdd-unittest

This repository is for me to date my studies on tests and TDD (Test Driven Development), using the classes of the course below:

https://www.udemy.com/course/python-3-do-zero-ao-avancado/

## Requirements:
- Have version 3 of python installed on the notebook or pc.
- Create the virtual environment in the project folder and install the requirements:

Linux or Mac:

``` bash
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install requirements.txt
```

Windows:

``` console
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install requirements.txt
```
## Check code quality:
```console
flake8
```

## Perform unit test
To perform the unit test use the command below:

```console
python -m unittest src/tests/test02_calculator.py
```

## Tests coverage

```console
coverage run -m unittest src/tests/test02_calculator.py

```

![](https://github.com/lipegomes/python-tdd-unittest/blob/main/assets/pictures/coverage_run.png)

```console
coverage report -m src/tests/test02_calculator.py
```

![](https://github.com/lipegomes/python-tdd-unittest/blob/main/assets/pictures/coverage_report.png)

## References

- [unittest](https://docs.python.org/3/library/unittest.html)

- [doctest](https://docs.python.org/3/library/doctest.html)

## Tools used:

- [Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
