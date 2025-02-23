import setuptools
import distutils.core

setuptools.setup(
    name='json-wmctrl',
    version="1.0.0",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='List X windows with json output',
    license='MIT',
    keywords='X, wmctrl, window manager',
    url='https://github.com/talwrii/json-wmctrl',
    packages=["json_wmctrl"],
    long_description=open('README.md').read(),
    install_requires=["Xlib"],
    entry_points={
        'console_scripts': ['json-wmctrl=json_wmctrl.main:main']
    },
)
