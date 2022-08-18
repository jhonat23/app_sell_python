from setuptools import setup


setup(
    name='av',
    version='0.1',
    py_modules=['av'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        av=av:cli
    ''',
)