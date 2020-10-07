from Utils.constants import TESTING
from Utils.db_object import db


async def execute(query, is_many, values):
    if TESTING or db.connection() is None:
        await db.connect()
    if is_many:
        result = await db.execute_many(query=query, values=values)
    else:
        result = await db.execute(query=query, values=values)
    return result


async def fetch(query, is_one, values=None):
    if TESTING or db.connection() is None:
        await db.connect()
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is not None:
            out = dict(result)
        else:
            out = None
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
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
