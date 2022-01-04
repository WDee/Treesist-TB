from setuptools import setup
from Cython.Build import cythonize

setup(
    name='new best splitter',
    ext_modules=cythonize(["new_splitter.pyx", '_utils.pyx'], 
                          compiler_directives={'language_level' : "3"}),
    install_requires=['cython', 'numpy'],
    zip_safe=False,
)


