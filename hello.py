#!/usr/bin/env python
import os
import json
import sys


from pprint import pprint
import urlparse

from templates import login_page



eVars = dict(os.environ)
contentLength = eVars['CONTENT_LENGTH']
cookie = eVars['HTTP_COOKIE']

username = "test"
password = "test"
logged_in = False

if cookie == 'logged-in=True':
  logged_in = True
elif contentLength:
  bytesToRead = int(contentLength)
  content = sys.stdin.read(bytesToRead)
  params = urlparse.parse_qs(content)

  if params['username'][0] == username and params['password'][0] == password:
    print "Hi,", username
    print "Set-Cookie: logged-in=True"
    logged_in = True

print 

if not logged_in:
  print r"""
      <h1> Welcome! </h1>
      <form method="POST" action="hello.py">
          <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
          <label> <span>Password:</span> <input type="password" name="password"></label>
          <button type="submit"> Login! </button>
      </form>
      """
else:
  print "Hi,", username




