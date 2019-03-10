"""
@user:Do丶
@time:2018/11/14 16:12
"""

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body='<h1>Index</h1>'.encode(), content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# from aiohttp import web
#
# routes = web.RouteTableDef()
#
#
# @routes.get('/')
# async def index(request):
#     await asyncio.sleep(2)
#     return web.json_response({
#         'name': 'index'
#     })
#
#
# @routes.get('/about')
# async def about(request):
#     await asyncio.sleep(0.5)
#     return web.Response(text="<h1>about us</h1>")
#
#
# def init():
#     app = web.Application()
#     app.add_routes(routes)
#     web.run_app(app)
# init()
