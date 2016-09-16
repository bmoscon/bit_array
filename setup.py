from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import six
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level='DEBUG')

        # import here, cause outside the eggs aren't loaded
        import pytest

        args = [self.pytest_args] if isinstance(self.pytest_args, six.string_types) else list(self.pytest_args)
        errno = pytest.main(args)
        sys.exit(errno)

setup(
    name="bit_array",
    version="0.1.0",
    author="Bryant Moscon",
    author_email="bmoscon@gmail.com",
    description=("Pure Python Bit Array"),
    license="XFree86",
    keywords=["bitarray"],
    url="https://github.com/bmoscon/bit_array",
    packages=find_packages(),
    long_description='Pure Python BitArray',
    cmdclass={'test': PyTest},
    setup_requires=[],
    install_requires=[],
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: XFree86",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Topic :: Software Development :: Libraries",
    ],
)
