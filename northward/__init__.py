# Python
import os
import sys

__version__ = '0.1.0'

if len(sys.argv) >=2 and sys.argv[1] == 'migrate_northward':
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
