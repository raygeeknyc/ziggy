import webapp2
from models import _Timestamp, _Delay

class SetTargetHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Setting target!')
        params = self.request.get_all('datetime')
        if params:
            timestamp = long(params[0])
            print 'saving {}'.format(timestamp)
            _Timestamp.Save(timestamp)

class GetTargetHandler(webapp2.RequestHandler):
    def get(self):
        timestamp = _Timestamp.Get()
        if timestamp:
            print 'got timestamp: {}'.format(timestamp)
            self.response.write('datetime={}\n'.format(timestamp.datetime))

class GetDelayHandler(webapp2.RequestHandler):
    def get(self):
        delay = _Delay.Get()
        if delay:
            print 'got delay: {}'.format(delay)
            self.response.write('delay={}\n'.format(delay.ms))

app = webapp2.WSGIApplication([
    ('/settarget', SetTargetHandler),
    ('/gettarget', GetTargetHandler),
    ('/getdelay', GetDelayHandler)
], debug=True)
