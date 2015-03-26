import os
from distutils.core import setup
from humod import __version__, __author__

CONFIG_FILES = [('/etc/ppp/peers', ['conf/humod'])]
try:
    os.stat('/etc/ppp/options')
except OSError:
    CONFIG_FILES = [('/etc/ppp/peers', ['conf/humod']),
                    ('/etc/ppp/options', ['conf/options'])]

setup(name='humod',
      version=__version__,
      packages=['humod'],
      description='Access SMS, GSM and 3G features of Huawei and '
                  'compatible modems via clean and pragmatic Python API',
      author='Slawek Ligus',
      author_email='root@ooz.ie',
      url='https://github.com/oozie/pyhumod',
      license='BSD',
      platforms=['Linux'],
      data_files=CONFIG_FILES,
      classifiers=['License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: POSIX',  
                   'Operating System :: POSIX :: Linux',
                   'Operating System :: MacOS :: MacOS X',
                   'Intended Audience :: Developers',
                   'Topic :: Communications',
                   'Topic :: Software Development :: Libraries'])
