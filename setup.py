from setuptools import setup, find_packages

setup(
    name='django-devserver-redux',
    version=".".join(map(str, __import__("devserver").__version__)),
    description='Drop-in replacement for Django\'s runserver',
    author='Yousuf Jawwad',
    author_email='yousuf@maher.pk',
    url='https://github.com/maherpk/django-devserver-redux',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    license="BSD",
)
