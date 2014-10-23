import urllib2
import sys
import json
import datetime


def create_gist(exceptions, plugin_dump):
    contents = ''
    err_cnt = 0
    rule_cnt = 0
    for r, e in exceptions:
        if len(e):
            rule_cnt += 1
            contents += 'Exceptions in rule [{0}]\n'.format(r)
            for re in e:
                contents += '\tException: {0}\n'.format(re['exception'])
                contents += '\tResolution: {0}\n'.format(re['resolution'])
                contents += '\tType: {0}\n'.format(re['type'])
                err_cnt += 1

    contents += '\nPlugin structures:\n'

    for d, v in plugin_dump.items():
        contents += 'Plugin location: {0}\n'.format(d)
        contents += 'Files:\n{0}'.format(v)

    jsonObj=dict(
        description='Rule violations {0}, total errors {1} run on {2}'.format(rule_cnt, err_cnt, datetime.datetime.now()),
        public=True,
        files=dict(
            obsanity_error_report=dict(
                content=contents
            )
        )
    )
    jsonObj=json.dumps(jsonObj)

    data=urllib2.urlopen('https://api.github.com/gists',jsonObj)
    data=data.read()
    jsonResponseData=json.loads(data)
    return jsonResponseData['html_url']
