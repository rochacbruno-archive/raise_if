import setuptools

setuptools.setup(
    name="raise_if",
    version="0.1.4",
    url="https://github.com/rochacbruno/raise_if",

    author="Bruno Rocha",
    author_email="rochacbruno@gmail.com",

    description=(
        "Probably the small python package, only includes raise_if function"
    ),
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
