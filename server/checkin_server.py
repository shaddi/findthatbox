import json

import webapp2

from google.appengine.ext import db

class Machine(db.Model):
    uuid = db.StringProperty()
    last_ip = db.StringProperty()
    last_priv_ip = db.StringProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class Checkin(webapp2.RequestHandler):
    def get(self, mid):
        machine = Machine(key_name=mid)
        machine.uuid = mid
        machine.last_ip = str(self.request.remote_addr)
        machine.last_priv_ip = str(self.request.get('private_ip'))
        machine.put()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(self.request.remote_addr)

class Status(webapp2.RequestHandler):
    def get(self, mid=None):
        q = Machine.all()
        self.response.headers['Content-Type'] = 'application/json'

        if mid:
            q.filter("uuid =", mid)

        resp = []
        for machine in q:
            resp.append({"machine": machine.uuid, "time": str(machine.timestamp), "public_ip": machine.last_ip, "private_ip": machine.last_priv_ip})

        print resp

        self.response.out.write(json.dumps(resp))


app = webapp2.WSGIApplication([
    ('/checkin/(.*)', Checkin),
    ('/status', Status),
    ('/status/(.*)', Status),
    ], debug=True)
