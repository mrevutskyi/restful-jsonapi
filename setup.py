import setuptools


setuptools.setup(
    name="restful-jsonapi",
    version="0.0.1",
    author="Maksym Revutskyi",
    author_email="maksym.revutskyi@gmail.com",
    description="A JSON:API builder for SQLAlchemy models",
    url="https://github.com/mrevutskyi/restful-jsonapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
