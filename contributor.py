"""
@user:Do丶
@time:2018/11/14 09:23
"""

def consumer():
    r = '0'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    e=c.send(None)
    print(e)#此值返回'0'
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)#r获得'1'
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)