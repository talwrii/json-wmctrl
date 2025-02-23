import setuptools
import distutils.core

setuptools.setup(
    name='json-wmctrl',
    version=0.1,
    author='Author',
    long_description_content_type='text/markdown',
    author_email='Email',
    description='',
    license='MIT',
    keywords='',
    url='',
    packages=["json_wmctrl"],
    long_description=open('README.md').read(),
    install_requires=["Xlib"],
    entry_points={
        'console_scripts': ['json-wmctrl=json_wmctrl.main:main']
    },
    classifiers=[
    ],
    test_suite='nose.collector'
)
