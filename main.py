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
import webapp2
from caesar import encrypt
import cgi

form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar Code</title>
    </head>
    <body>
        <form method = "post">
                <label for="rotation"><b>Rotate by:</b></label>
                    <input type = "text" name ="rotation" value = "%(rotation)s"
                        style="height: 20px; width: 50px"/>
                <br>
                <p><label for="message"><b>Secret Message</b></label></p>
                    <textarea name="text" style="height: 100px; width: 400px">%(text)s
                    </textarea>
                <br>
                <p><input type = "submit" value = "Submit"></p>
            <div>
        </form>
    </body>
</html>
    """
def escape_html(s):
        return cgi.escape(s, quote = True)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, rotation="", text=""):
        self.response.out.write(form % {"rotation": rotation,
                                        "text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_rot = int(escape_html(self.request.get("rotation")))
        user_msg = escape_html(self.request.get("text"))
        result = encrypt(user_msg, user_rot)
        self.write_form(user_rot, result)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
