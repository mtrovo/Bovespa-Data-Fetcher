#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db

import models

import logging

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('RONALDO!')


class WatchedCompaniesHandler(webapp.RequestHandler):
  def get(self):
    data = {}
    data['watched'] = db.GqlQuery("SELECT * from WatchedCompany ORDER BY company").fetch(100 )
    data['companies'] = db.GqlQuery("SELECT * from Company ORDER BY code")\
    .fetch(100)

    self.response.out.write(template.render('templates/watched.html', data))
  
  def post(self):
    sels = self.request.get_all('selected')
    self.response.out.write(sels)
#    self.response.out.write(repr(self.request.POST))

def main():
  mappings = []
  mappings.append(('/', MainHandler))
  mappings.append(('/watched', WatchedCompaniesHandler))
  logging.info(repr(mappings))
  application = webapp.WSGIApplication(mappings,
                                       debug=True)
  util.run_wsgi_app(application)



if __name__ == '__main__':
  main()
