import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# b'FIXME SET WITH: $ python3 -c "import os; print(os.urandom(24))" '
# Secret key for encrypting cookies
SECRET_KEY = b'Fss\x96J\x7fr..fT<\xee\xdc\xbd\xe4Z\x1f\xac\xf7 H\xc8\x0b'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
SONGVOTING_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = SONGVOTING_ROOT/'var'/'songvoting.sqlite3'