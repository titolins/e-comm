import sys, os
sys.stdout = sys.stderr
sys.path.insert(0,'/var/www/e-comm')
os.chdir('/var/www/e-comm')
from project import app as application
