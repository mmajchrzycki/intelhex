#!/usr/bin/python

# Copyright (c) 2008, Alexander Belchenko
# All rights reserved.
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided
# that the following conditions are met:
#
# * Redistributions of source code must retain
#   the above copyright notice, this list of conditions
#   and the following disclaimer.
# * Redistributions in binary form must reproduce
#   the above copyright notice, this list of conditions
#   and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the author nor the names
#   of its contributors may be used to endorse
#   or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Setup script for IntelHex."""

from distutils.core import setup

cmdclass = {}

try:
    from extras.test import test
except ImportError:
    pass
else:
    cmdclass['test'] = test


setup(name='intelhex',
      version='1.0',

      scripts=[
        'scripts/bin2hex.py',
        'scripts/hex2bin.py',
        'scripts/hex2dump.py',
        'scripts/hexmerge.py',
        ],
      packages=['intelhex'],
      cmdclass=cmdclass,

      author='Alexander Belchenko',
      author_email='bialix@ukr.net',
      url='http://www.bialix.com/intelhex/',

      description='Intel HEX file format reader and convertor',
      keywords='Intel HEX hex2bin HEX8',
      license='BSD',
      classifiers = [
        'Classifier: Development Status :: 5 - Production/Stable',
        'Classifier: Environment :: Console',
        'Classifier: Intended Audience :: Developers',
        'Classifier: Intended Audience :: Telecommunications Industry',
        'Classifier: License :: OSI Approved :: BSD License',
        'Classifier: Operating System :: OS Independent',
        'Classifier: Programming Language :: Python',
        'Classifier: Topic :: Scientific/Engineering',
        'Classifier: Topic :: Software Development :: Embedded Systems',
        'Classifier: Topic :: Utilities',
      ],
)

