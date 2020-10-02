from Utils.constants import DB_ADMIN, DB_HOST, DB_NAME, DB_PASSWORD
from databases import Database

db = Database(f'postgresql://{DB_HOST}/{DB_NAME}?user={DB_ADMIN}&password={DB_PASSWORD}')
