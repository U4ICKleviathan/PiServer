import led_actions
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import urlparse
from pprint import pprint

led_actions.setup()

PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        request_path = self.path
        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        print(request_headers)
        print(self.rfile.read(length))
        print("<----- Request End -----\n")

        self.end_headers()
        # Send the html message
        self.wfile.write("Server Is Online")
        return


    def do_POST(self):
        command = "No Command Set"
        request_path = self.path
        # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self .rfile.read(length).decode('utf-8'))
        for key, value in post_data.iteritems():
            print "%s=%s" % (key, str(value))
            if 'command' in key:
                command = str(value)

        if 'blink' in command:
            print "BLINKING LED"
            led_actions.blink()
            self.send_response(200)
        elif 'fade' in command:
            print "FADING LED"
            led_actions.fade()
            self.send_response(200)
        else:
            print "COMMAND NOT RECOGNIZED"
            self.send_response(403)
        self.end_headers()

        # self.wfile.write('Client: %s\n' % str(self.client_address))
        # self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        # self.wfile.write('Path: %s\n' % self.path)
        # self.wfile.write('Form data:\n')
        #
        # for field in form.keys():
        #     field_item = form[field]
        #     if field_item.filename:
        #         # The field contains an uploaded file
        #         file_data = field_item.file.read()
        #         file_len = len(file_data)
        #         del file_data
        #         self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
        #                 (field, field_item.filename, file_len))
        #     else:
        #         # Regular form value
        #         self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return



def main():
    try:
        # Create a web server and define the handler to manage the
        # incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ', PORT_NUMBER
        # Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print "shutting down the server"
        server.socket.close()



if __name__ == "__main__":
    main()
