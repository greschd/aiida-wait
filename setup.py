# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages

# Get the version number
with open('./aiida_wait/__init__.py') as f:
    match_expr = "__version__[^'\"]+(['\"])([^'\"]+)"
    version = re.search(match_expr, f.read()).group(2).strip()

if __name__ == '__main__':
    setup(
        name='aiida-wait',
        version=version,
        description='AiiDA Plugin for running wait',
        author='Dominik Gresch',
        author_email='greschd@gmx.ch',
        license='GPL',
        classifiers=[
            'Development Status :: 3 - Alpha', 'Environment :: Plugins',
            'Framework :: AiiDA', 'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Scientific/Engineering :: Physics'
        ],
        keywords='bandstructure aiida workflows',
        packages=find_packages(exclude=['aiida']),
        include_package_data=True,
        setup_requires=['reentry'],
        reentry_register=True,
        install_requires=[
            'aiida-core',
        ],
        extras_require={
            'dev': [
                'numpy', 'aiida-pytest', 'pytest', 'yapf', 'pre-commit',
                'prospector'
            ]
        },
        entry_points={
            'aiida.calculations': [
                'wait.wait = aiida_wait.calculations.wait:WaitCalculation',
            ],
            'aiida.parsers': [
                'wait.wait = aiida_wait.parsers.wait:WaitParser',
            ],
        },
    )
