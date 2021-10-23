import setuptools

with open('docs/pypi.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='autofaker',
    version='0.1.0',
    url='https://github.com/christianhelle/autofaker',
    license='MIT License',
    license_files=["LICENSE"],
    author='Christian Helle',
    author_email='christian.helle@outlook.com',
    description='Python library designed to minimize the setup/arrange phase of your unit tests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['pandas', 'pyspark', 'faker'],
    entry_points={
        'console_scripts': [
            'python3=autofaker.alias:python3',
        ],
    },
)
