import webapp2
from models import _Timestamp, _Delay

class SetHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Setting!')
        params = self.request.get_all('datetime')
        if params:
            timestamp = long(params[0])
            print 'saving {}'.format(timestamp)
            _Timestamp.Save(timestamp)

class GetHandler(webapp2.RequestHandler):
    def get(self):
        timestamp = _Timestamp.Get()
        if timestamp:
            print 'got timestamp: {}'.format(timestamp)
            self.response.write('datetime={}\n'.format(timestamp.datetime))

        delay = _Delay.Get()
        if delay:
            print 'got delay: {}'.format(delay)
            self.response.write('delay={}\n'.format(delay.seconds))

app = webapp2.WSGIApplication([
    ('/settarget', SetHandler),
    ('/gettarget', GetHandler)
], debug=True)
