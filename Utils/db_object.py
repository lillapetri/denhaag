from Utils.constants import DB_URL, TESTING, TEST_URL
from databases import Database

url = TEST_URL if TESTING else DB_URL
db = Database(url)
