import asyncio
import sys

import orm
from models import User


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='test77',email='test77@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)