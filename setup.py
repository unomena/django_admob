from setuptools import setup, find_packages

setup(
    name='django_admob',
    version='0.1',
    description='AdMob Django Application',
    author='John Boxall',
    author_email='john@handimobility.ca',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
)
