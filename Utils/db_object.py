from databases import Database

from Utils.constants import DB_PRODUCTION, DB_URL, IS_LOAD_TEST, IS_PRODUCTION, TESTING, TEST_URL

if TESTING or IS_LOAD_TEST:
    db = Database(TEST_URL)
elif IS_PRODUCTION:
    db = Database(DB_PRODUCTION)
else:
    db = Database(DB_URL)
