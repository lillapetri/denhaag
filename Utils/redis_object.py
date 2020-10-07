import aioredis

from Utils.constants import IS_PRODUCTION, REDIS_URL_PRODUCTION, TESTING, TEST_REDIS_URL

redis = None


async def check_test_redis():
    global redis
    if IS_PRODUCTION:
        redis = await aioredis.create_redis_pool(REDIS_URL_PRODUCTION)

    if TESTING:
        redis = await aioredis.create_redis_pool(TEST_REDIS_URL)
