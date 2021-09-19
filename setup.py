import setuptools

setuptools.setup(
    name="django-show-source-code",
    version="0.0.4",
    author="Ian Jones",
    description="Django app to show source code and templates in a bootstrap modal",
    url="https://github.com/jonesim/show-src-code",
    include_package_data = True,
    packages=['show_src_code'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['django-ajax-helpers', 'django-nested-modals'],
)
