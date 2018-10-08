import webapp2
import time
from models import _Timestamp, _Delay

TIMESTAMP_SET_LIFETIME_MINS = 3
_TIMESTAMP_SET_LIFETIME_SECS = TIMESTAMP_SET_LIFETIME_MINS  * 60

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
        target = _Timestamp.Get()
        if target:
            print 'got target: {}'.format(target)
            if (time.time() - target.when) > _TIMESTAMP_SET_LIFETIME_SECS:
                print 'target expired, returning current time'
                now = long(time.time())
                timestamp = now
            else:
                timestamp=target.datetime
        self.response.write('datetime={}\n'.format(timestamp))

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
