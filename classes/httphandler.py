import urllib2
import re

class HTTPHandler:
	#Functions
	def contentParser(self,tag, attr, value, end_value, content):
		tag_attr_value = '<'+tag
		if attr != None:
			tag_attr_value += ' ' + attr
		else:
			tag_attr_value += '>'
		if value != None:
			tag_attr_value = tag_attr_value + '="' + value
			if end_value == True:
				tag_attr_value = tag_attr_value + '"'
		#print '\nCONTENT EXPRESSION:',tag_attr_value,'\n'
		i = 0
		content_array = []
		for s in re.finditer(tag_attr_value,content):
			start = s.start()
			end = s.end()
			s = s.string
			startPos = s.find('>',start)
			stopPos = s.find('</'+tag,startPos+1)
			#print start,end,startPos, stopPos
			c = content[startPos+1:stopPos]
			#print c
			content_array.append(c)
		return content_array

		
	def valueParser(self,tag, attr, value, end_value, content):
		tag_attr_value = tag
		if attr != None:
			tag_attr_value += ' ' + attr
		if value != None:
			tag_attr_value = tag_attr_value + '="' + value
			if end_value == True:
				tag_attr_value = tag_attr_value + '"'
		#print '\nCONTENT EXPRESSION:',tag_attr_value,'\n'
		i = 0
		value_array = []
		for s in re.finditer(tag_attr_value,content):
			start = s.start()
			end = s.end()
			s = s.string
			startPos = s.find('"',start)
			stopPos = s.find('"',startPos+1)
			#print start,end,startPos, stopPos
			v = content[startPos+1:stopPos]
			#print c
			value_array.append(v)
		return value_array

	def tagParser(self,tag, attr, value, end_value, content):
		tag_attr_value = tag
		if attr != None:
			tag_attr_value += ' ' + attr
		if value != None:
			tag_attr_value = tag_attr_value + '="' + value
			if end_value == True:
				tag_attr_value = tag_attr_value + '"'
		#print '\nTAG EXPRESSION:',tag_attr_value,'\n'
		i = 0
		tags_content = []
		for s in re.finditer(tag_attr_value,content):
			start = s.start()
			end = s.end()
			s = s.string
			startPos = s.find('"',start)
			stopPos = s.find('</'+tag+'>',startPos+1)
			#print start,end,startPos, stopPos
			tag_content = content[startPos+1:stopPos]
			#print tag_content
			tags_content.append(tag_content)
		return tags_content
		
	def downloadFile(self,url,fname):		
		response = self.HTTPRequest(url)
		print "File:",fname
		file = open(fname,"w");
		file.write(response);
		file.close();

	def HTTPRequest(self,url):
		req = urllib2.Request(url, headers={'User-Agent' : "Different Browser"})
		con = urllib2.urlopen(req)
		response = con.read()
		return response
