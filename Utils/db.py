import nest_asyncio
from Utils.constants import DB_ADMIN, DB_HOST, DB_NAME, DB_PASSWORD
from databases import Database

nest_asyncio.apply()


async def connect_db():
    db = Database(f'postgresql://{DB_HOST}/{DB_NAME}?user={DB_ADMIN}&password={DB_PASSWORD}')
    await db.connect()
    print('DB connected.')
    return db


async def disconnect_db(db):
    await db.disconnect()
    print("DB disconnected")


async def execute(query, is_many, values):
    db = await connect_db()
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)
    await disconnect_db(db)


async def fetch(query, is_one, values=None):
    db = await connect_db()
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    await disconnect_db(db)
    return out

# query = "insert into food values(:name, :address, :cuisine, :votes, :description, :url, :created_at, :covid_factor, " \
#         ":district) "
#
# values = {"name": "L'oro di Napoli", "address": "Laan van Meerdervoort 543",
#           "cuisine": "Italian", "votes": 0, "description": None, "url": "https://www.lorodinapoli-denhaag.nl/",
#           "created_at": datetime.datetime.now(), "covid_factor": "Moderate risk", "district": "Segbroek"}
#
#
# query2 = 'insert into users values(:username, :password, :is_active, :created_at, :role)'
#
# values2 = {"username": "test", "password": "pass", "is_active": True, "created_at": datetime.datetime.now(), "role": "admin"}
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(execute(query2, False, values2))
