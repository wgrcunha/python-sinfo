import urllib

url = None

def apacheinfo():
    data = {}
    if not url:
        return data
    try:
        response = urllib.urlopen(url).read()
    except Exception, e:
        print "Can't open apache status url: %s" % url
    else:
        for line in [ line.strip().split(":") for line in response.split("\n") ]:
            if len(line) == 2:
                data[line[0]] = line[1].strip()
    return data

ALL = [ apacheinfo ]
