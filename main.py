#!/usr/bin/python
import web
from TokenToUrl import TokenToUrl 
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        url = "http://locahost:8080/" + web.ctx.fullpath
        t = TokenToUrl()
        t.generate(url)
        return t.getToken()

if __name__ == "__main__":
    app.run()
