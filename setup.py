# necessary to push to PyPI
# cf. https://packaging.python.org/tutorials/packaging-projects/

# python setup.py sdist
# then :
# twine upload --repository-url https://pypi.org/legacy/ dist/*


from setuptools import setup, find_packages
from distutils.util import convert_path

packages = find_packages()
module = packages[0]  # valid if only one package

meta_ns = {}
ver_path = convert_path(module + '/__meta__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), meta_ns)

name = meta_ns['__name__']
packages = packages
version = meta_ns['__version__']
description = meta_ns['__description__']
long_description = meta_ns['__long_description__']
author = meta_ns['__author__']
author_email = meta_ns['__author_email__']
url = meta_ns['__url__']
keywords = meta_ns['__keywords__']
license = meta_ns['__license__']
classifiers = meta_ns['__classifiers__']
include_package_data = meta_ns['__include_package_data__']
package_data = meta_ns['__package_data__']
zip_safe = meta_ns['__zip_safe__']
entry_points = meta_ns['__entry_points__']

# read requirements.txt
with open('requirements.txt', 'r') as f:
    content = f.read()
li_req = content.split('\n')
install_requires = [e.strip() for e in li_req if len(e)]

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    keywords=keywords,
    license=license,
    classifiers=classifiers,
    packages=packages,
    install_requires=install_requires,
    include_package_data=include_package_data,
    package_data=package_data,
    zip_safe=zip_safe,
    entry_points=entry_points
)
