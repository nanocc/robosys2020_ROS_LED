#!/usr/bin/env python3

import rospy, os
import http.server, socketserver

def kill():
    os.system("kill -KILL " + str(os.getpid()))

if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))
    rospy.init_node("web")
    rospy.on_shutdown(kill)

    port = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    httpd.serve_forever()
