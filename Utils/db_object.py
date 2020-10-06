from Utils.constants import DB_URL, IS_LOAD_TEST, TESTING, TEST_URL
from databases import Database

if TESTING or IS_LOAD_TEST:
    db = Database(TEST_URL)
else:
    db = Database(DB_URL)
