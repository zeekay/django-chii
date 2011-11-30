import os, sys
import chii

sys.path.insert(0, chii.config['django_chii'])
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
