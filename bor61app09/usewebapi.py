import webapp2
from google.appengine.api import urlfetch

urla = "https://php.radford.edu/~jcdavis/D2L/classes/it425/lectmat/webserv/tempws_api.php?temp="
urlb = "&scale="


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Create Form
        self.response.write('<html><body><h1>Use API example</h1>')
        self.response.write("""<hr><form method = "post">
        <table border = "1">
        <tr>
            <td height="100"><b>Enter degree :</b></td>
            <td><input type = "textarea" name = "deg"></input></td>
        </tr>
        <tr>
            <td height="100"><b>Convert from Celsius or Fahrenheit<br/>
                (Write 'C' or 'F' in uppercase only) :</b> </td>
            <td><input type = "textarea" name = "corf"></input></td>
        </tr>
        <tr>
            <td colspan = "2" height="100"><input type = "submit"></input></td>
        </tr>

        </table>     
        
        
        
        </form>""")
        self.response.write('</body></html>')

    def post(self):
        #get what the user entered in the FORM
        degree_entered = self.request.get('deg')
        corf_entered = self.request.get('corf')
        url = urla + degree_entered + urlb + corf_entered
        
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            #Print
            self.response.write('<html><body>')
            self.response.write('<b><h3>Conversion of '+ degree_entered + ' ' +
                                corf_entered+' :  %s </h3></b>'%str(result.content))
            self.response.write('</body></html>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
