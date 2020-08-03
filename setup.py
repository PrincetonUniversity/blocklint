from setuptools import setup


setup(
    name='blocklint',
    description='Lint for blocklisted words',
    python_requires='>=2.7',
    entry_points={
        'console_scripts': [
            'blocklint=blocklint.main:main',
        ],
    },
)
