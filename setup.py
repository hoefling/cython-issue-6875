from setuptools import Distribution, Extension, setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([Extension("*", ["spam.py"])], language_level=3, compiler_directives={"linetrace": True}),
    options={"build_ext": {"define": "CYTHON_TRACE"}},
)
