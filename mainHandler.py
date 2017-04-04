import urllib2
import json
import datetime
import csv
import time
from page import *
# from next_page import *
# from prev_page import *

from comma import *
from appData import *

# Since the code output in this notebook leaks the app_secret,
# it has been reset by the time you read this.



recent = {}
# scraping the most recent data


def getData (page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.8"
    node = "/" + page_id + "/posts"
    fields = "/?fields=message,picture"
    parameters = "&access_token=%s" % access_token

    url = base + node + fields + parameters
    # EAAEEMTLF8KQBAIqaTI8lEXQUQZC4xLPbTuFbgYfrcyZCWXFfNa8liNPuRthZAZB64gZBxJPqF4AtOgvVfxXbYYb5ZAaoOJK6wlp6KNMO0xIQUHBZAzit8iWcZBrpXbB1ZCbZCZBZCAKTZCy0GVm0oZCgqnwBZB7VasJYtar58kZD

    # retrieve data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    recent = {}
    data = json.loads(response.read())
    recent = json.dumps(data, indent =4, sort_keys=True)

    # printing the scraped data
    return recent


        # function call to get the data of next page
        # next_page()

        # function call to get the data of previous page
        # prev_page()

def next_page():
    next = recent['paging']['next']
    req = urllib2.Request(next)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    return data;





def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try:
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)
            print "Error for URL %s: %s" % (url, datetime.datetime.now())

    return response.read()
