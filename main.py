from http.server import HTTPServer
from socketserver import ThreadingMixIn
from requestHandler import RequestHandler
from myRequests import subscribe, unsubscribe
import utitls
import time
# import sys
import traceback
import questInfo


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass

def startWebServer():
    # ip = utitls.configJson().get('serverIP')
    port = utitls.configJson().get('serverPort')
    server = ThreadedHTTPServer(('', int(port)), RequestHandler)
    utitls.myLogger('WebServerStarted, Listening on localhost:%s' % port)
    # sys.stderr = open('logfile.txt', 'a+', 1)
    server.serve_forever()
    return server.shutdown()


def Async_subscribeTheList(isSubscribe):
    utitls.runFuncAsyncThread(subscribeTheList_sync, (isSubscribe,))
def subscribeTheList_sync(isSubscribe):
    subscribeList = utitls.configJson().get('subscribeList')
    ip = utitls.configJson().get('serverIP')
    port = utitls.configJson().get('serverPort')
    for item in subscribeList:
        tmp_subscribeId = item.get('youtubeChannelId', "")
        if tmp_subscribeId != "":
            port = '' if port == '80' else ':' + port
            tmp_callback_url = 'http://' + ip + port + '/subscribe'
            if isSubscribe:
                time.sleep(1)   #wait the server start preparing
                subscribe(tmp_callback_url, tmp_subscribeId)
            else:
                unsubscribe(tmp_callback_url, tmp_subscribeId)



def main():
    try:
        #init the quest list
        questInfo.initQuestList()
        Async_subscribeTheList(True)
        startWebServer()

    except Exception as e:
        utitls.myLogger(traceback.format_exc())
        utitls.myLogger(str(e))

if __name__ == "__main__":
    try:
        while True:
            main()
            utitls.myLogger('RESTART WERSERVER')
            time.sleep(5)
    except KeyboardInterrupt:
        # subscribeTheList_sync(False)
        utitls.myLogger('Running END-------------------------\n')
