from setuptools import setup, find_packages
import os



version = '0.1.0dev'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('cuppystatic', 'test_adminlte.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='cuppystatic',
    version=version,
    description="Fanstatic packaging of adminlte and other resources for Cuppy cms",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Ephraim Anierobi',
    author_email='ephraimanierobi@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.bootstrap',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'cuppystatic = cuppystatic:library',
            ],
        },
    )
