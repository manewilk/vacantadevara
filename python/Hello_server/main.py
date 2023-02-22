import cherrypy
html_header = \
"""
<html>
  <head>
    <title>Example of GET and POST</title>
  </head>
  <body>
"""

html_footer = \
"""
  </body>
</html>
"""

class GetPostMethods(object):

    @cherrypy.expose
    def index(self):
        html_body = \
"""
    <p>
    <form method="post" action="post_hello">
      <input type="text" value="" name="post_name"/>
      <button type="submit">POST Temperaturas in Celsius!</button>
    </form>
"""
        return html_header + html_body + html_footer

    @cherrypy.expose
    def post_hello(self, post_name):
        # if cherrypy.request.method == 'POST':
        post_name = float(post_name)*1.8 + 32
        html_body = "<p>Temperatura in Farenheit este %s!</p>" % post_name #NOTE This input IS NOT SANITIZED!!! 
        return html_header + html_body + html_footer
        

if __name__ == '__main__':
    conf = { '/': {}
    }
    cherrypy.quickstart(GetPostMethods(), '/', conf)