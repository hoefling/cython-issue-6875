# cython-issue-6875
Project that reproduces the issue https://github.com/cython/cython/issues/6785

### Reproduce

```sh
rm -rf __pycache__ build htmlcov *.egg-info eggs.cpython-*.so eggs.c
pip install --editable=.
coverage run -m pytest
coverage html
open htmlcov/index.html
```
