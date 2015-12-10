import urllib
import urllib2
import xml.etree.ElementTree

# Input Variables
origin = '123 My Street, New York City USA'
destination = '345 Appointment Drive, New York City NY USA'
contact_phone = '2145551234@txt.att.net'
sender = 'myemail@example.com'
subject = 'Route Details'
hashcode = 'enter TextOnComplete hash code here' # See https://github.com/huksu/TextOnComplete
text_on_complete_url = 'enter TextOnComplete php URL here' # See https://github.com/huksu/TextOnComplete

# Actions
req = urllib2.Request('http://maps.googleapis.com/maps/api/directions/xml?origin=' + urllib.quote(origin) + '&destination=' + urllib.quote(destination))
response = urllib2.urlopen(req)
the_response = response.read()
e = xml.etree.ElementTree.fromstring(the_response)
summary = e.find('route').find('summary').text
duration = e.find('route').find('leg').find('duration').find('text').text
distance = e.find('route').find('leg').find('distance').find('text').text
start = e.find('route').find('leg').find('start_address').text
end = e.find('route').find('leg').find('end_address').text
message = 'Route from: \n' + start + '\nTo:\n' + end + '\n' + distance + '\nVia:\n' + summary + '\n' + duration
req = urllib2.Request(text_on_complete_url + '?hash=' + hashcode + '&to=' + contact_phone + '&from=' + sender + '&subject=' + urllib.quote(subject) + '&message=' + urllib.quote(message))
response = urllib2.urlopen(req)
print response.read()
