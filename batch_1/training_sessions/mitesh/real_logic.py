class CallBack:

    def __init__(self):
        print("This is constructor....")


    def getSiteMap(self, path):
        l = []
        l.append(HttpRequest(8080,"pb-prd.com", "post {} "))
        l.append(HttpRequest(8081,"pb-qa.com", "post {} "))
        l.append(HttpRequest(8082,"pb-dev.com", "post {} "))
        return l


class HttpRequest:

    def __init__(self, port,host,request):
        self.port = port
        self.host = host
        self.request = request


    def getPort(self):
        return self.port

    def getHost(self):
        return self.host

    def getRequest(self):
        return self.request


class Burp:

    def registerCallback(self, callBack):
        l = callBack.getSiteMap("path")

        for item in l:
            print("Host: " + str(l.getHost()))



l = [HttpRequest(8080,"pb-prd.com", "post {} "), HttpRequest(8080,"pb-prd.com", "post {} ")]

for s in l:
    print(s.getHost() + "-- " + str(s.getPort()))
