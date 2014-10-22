import urllib2
import sys
import json
import datetime


def create_gist(exceptions):
    contents = ''
    err_cnt = 0
    for r, e in exceptions:
        if len(e):
            contents += 'Exceptions in rule [{0}]\n'.format(r)
            for re in e:
                contents += '\tException: {0}\n'.format(re['exception'])
                contents += '\tResolution: {0}\n'.format(re['resolution'])
                contents += '\tType: {0}\n'.format(re['type'])
                err_cnt += 1
    jsonObj=dict(
        description='Rule violations {0}, total errors {1} run on {2}'.format(len(exceptions), err_cnt, datetime.datetime.now()),
        public=True,
        files=dict(
            obsanity_error_report=dict(
                content=contents
            )
        )
    )
    jsonObj=json.dumps(jsonObj)

    #data=urllib2.urlopen('https://api.github.com/gists',jsonObj)
    #data=data.read()
    #    jsonResponseData=json.loads(data)
    # return jsonResponseData['html_url']
    return 'http://www.google.com'