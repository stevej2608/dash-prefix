import os

from setuptools import find_packages
from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

def _get_long_description():
    with open(os.path.join(HERE, "README.md")) as f:
        return f.read()

def _get_version():
    """ Get version by parsing _version programmatically """
    packages = ["dash_prefix"]
    version_ns = {}
    with open(
            os.path.join(HERE, packages[0], "_version.py")
    ) as f:
        exec(f.read(), {}, version_ns)
    version = version_ns["__version__"]
    return version


def _get_dependencies():
    """Parse requirements.txt and return a list of dependencies"""
    with open(os.path.join(HERE, "requirements.txt")) as f:
        requirements = f.read()

    result = []
    requirements = requirements.split('\n')
    for r in requirements:
        if r == '# setup.py - exclude':
            break
        if r == '' or r.startswith('#'):
            continue
        result.append(r)
    return result


setup(
    name="dash-prefix",
    version=_get_version(),
    url="https://github.com/stevej2608/dash-prefix",
    license='MIT',

    author="Steve Jones",
    author_email="jonesst608@gmail.com",

    description="Dash library for managing component IDs",
    long_description=_get_long_description(),
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests',)),
    include_package_data=True,

    install_requires=_get_dependencies(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
