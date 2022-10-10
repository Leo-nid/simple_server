from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logger = logging.getLogger()

hostName = "0.0.0.0"
serverPort = 8888

class MyServer(BaseHTTPRequestHandler):
  def error_response(self, code, message):
    rslt_msg = f"{code}: {message}"
    self.send_response(code)
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Content-type", "text/plain")
    self.send_header("Content-Length", len(rslt_msg))
    self.end_headers()
    self.wfile.write(bytes(rslt_msg, "utf-8"))
    
  def do_GET(self):
    logger.debug(f"GET request with path {self.pth}")
    self.error_response(404, "Page not found")

  def do_POST(self):
    logger.debug(f"POST request with path {self.pth}")
    content_length = int(self.headers["Content-Length"])
    post_data = self.rfile.read(content_length)
    if self.path == "/sort":
      try:
        numbers = [int(s) for s in post_data.split()]
      except ValueError:
        self.error_response(400, "Message should contains only integer numbers separated by spaces")
        return
      result = ' '.join(map(str, sorted(numbers))) + '\n'
      self.send_response(200)
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Content-type", "text/plain")
      self.send_header("Content-Length", len(result))
      self.end_headers()
      self.wfile.write(bytes(result, "utf-8"))
      
      return
    self.error_response(404, "Page not found")
    

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    logger.info("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logger.info("Server stopped.")