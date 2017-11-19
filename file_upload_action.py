#!/Python27/python
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

file_item = form['filename']

if file_item.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
	fn = os.path.basename(file_item.filename)
	open(fn, 'w').write(file_item.file.read())
	message = 'The file was uploaded successfully'
else:
	message = 'No file was uploaded'

print 'content-type:text/plain\r\n\r\n'
print message