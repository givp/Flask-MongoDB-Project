import sys
flaskfirst = "/mnt/hgfs/winwww/flaskr"
if not flaskfirst in sys.path:
    sys.path.insert(0, flaskfirst)

sys.stdout = sys.stderr

from myapp import app
application = app
