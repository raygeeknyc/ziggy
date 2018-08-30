import webapp2
from models import _Timestamp

class SetHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Setting!')
        params = self.request.get_all('timestamp')
        if params:
            timestamp = long(params[0])
            print 'saving {}'.format(timestamp)
            _Timestamp.Save(timestamp)

class GetHandler(webapp2.RequestHandler):
    def get(self):
        timestamp = _Timestamp.Get()
        if timestamp:
            print 'got timestamp: {}'.format(timestamp)
            self.response.write('datetime={}'.format(timestamp.datetime))

app = webapp2.WSGIApplication([
    ('/settarget', SetHandler),
    ('/gettarget', GetHandler)
], debug=True)

