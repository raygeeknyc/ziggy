from google.appengine.ext import webapp2

class SetHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Setting!')
        set()

class SetHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Getting!')

app = webapp2.WSGIApplication([
    ('/set', SetHandler),
    ('/get/', GetHandler)
], debug=True)

def set():
  print("setting target datetime")
  timestamp = long(self.request.get_all("timestamp"))
  _Timestamp.Save(timestamp)
