import warnings
import os
from importlib import import_module

packages = ['sklearn', 'nibabel', 'numpy',
            'matplotlib', 'skbold']

warnings.filterwarnings("ignore")

for package in packages:
    try:
        import_module(package)
        print('%s was succesfully installed!' % package)

    except ImportError:
        print('\nCould not find package %s' % package)
        cmd = "pip install %s" % package
        print('Install %s using the command: %s\n' % (package, cmd))
