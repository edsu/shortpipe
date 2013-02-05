from setuptools import setup

# for older pythons ...
requirements = ["requests"]
try:
    import multiprocessing
except:
    requirements.append("multiprocessing")

setup(
    name = 'shortpipe',
    version = '0.0.1',
    url = 'http://github.com/edsu/shortpipe',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    scripts = ['shortpipe'],
    description = 'unshorten urls on the command line',
    platforms = ['POSIX'],
    install_requires = requirements,
)
