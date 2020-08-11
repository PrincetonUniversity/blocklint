import setuptools


setuptools.setup(
    name='blocklint',
    version="0.0.1",
    description='Lint for blocklisted words',
    python_requires='>=2.7',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'blocklint=blocklint.main:main',
        ],
    },
)
