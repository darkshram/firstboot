#!/usr/bin/python2

from distutils.core import setup
from glob import *
import os

data_files = [('/usr/sbin', ['progs/firstboot']),
              ('/usr/share/firstboot/themes/default',
               glob('themes/default/*.png')),
              ('/usr/share/firstboot/modules', glob('modules/*.py')),
              ('/etc/rc.d/init.d', glob('sysvinit/firstboot'))]

# add the firstboot start script for s390 architectures
if os.uname()[4].startswith('s390'):
    data_files.append(('/etc/profile.d', ['scripts/firstboot.sh']))
    data_files.append(('/etc/profile.d', ['scripts/firstboot.csh']))

setup(name='firstboot', version='2017.12.06',
      description='Post-installation configuration utility',
      author='Joel Barrios', author_email='darkshram@gmail.com',
      url='https://github.com/darkshram/firstboot',
      data_files=data_files,
      packages=['firstboot'])
