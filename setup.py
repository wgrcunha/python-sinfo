#!/usr/bin/python
from distutils.core import setup

setup(name='sinfo',
      version='0.0-4',
      description='Python system info',
      author='Francisco Freire',
      author_email='wgrcunha@gmail.com',
      url='',
      packages=['sinfo'],
      package_dir = {                      
                        'sinfo': 'src/lib',
                    },
      data_files=[
            ('/etc/init.d', ['src/init/sinfo']),
            ('/usr/sbin', ['src/sbin/python-sinfo']),
            ('/etc', ['src/conf/sinfo.cfg']),
        ]
     )
