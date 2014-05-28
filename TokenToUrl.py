#!/usr/bin/python
import redis
import hashlib
import time

'redis pool'
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

class TokenToUrl: 
    def __init__(self): 
        'a fix length string'
        self.token = ""
        'the real url'
        self.url = ""
    
    def generate(self, url): 
        'generate token for this url'
        self.url = url
        r = redis.Redis(connection_pool=pool)
        token = ""
        while True:
            u = url + str(time.time())
            token = hashlib.md5(u).hexdigest()
            if r.hset("tokens", token, url) == 1:
                break;
        self.token = token

    def getToken(self):
        return "http://smy2.cn/" + self.token

    def getURL(self):
        return self.url

