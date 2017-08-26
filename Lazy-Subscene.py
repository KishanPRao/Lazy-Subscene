#Created on 06 August, 2016.

#h1 = httplib.HTTPConnection('http://subscene.com/subtitles/title?q=ss&l=')
#url = "https://www.iana.org/domains/reserved"
#urllib2.urlopen("http://subscene.com/subtitles/title?q=ss&l=")
#URLS

#Imports
import sys
import os
import zipfile
import rarfile
from urllib2 import HTTPError
from classes.httphandler import HTTPHandler

class Subscene:
	def getSubtitle(self,filename):
		has_run = False
		print "Get Subtitle for",filename
		handler = HTTPHandler()
		#Remove extension
		f=os.path.splitext(filename)[0]
		f=f.replace(' ','.')
		url = "http://subscene.com/subtitles/release?q="
		url = url + f
		try:
			response = handler.HTTPRequest(url)
		except HTTPError as e:
			print e.read()


		'''
		file = open("Subscene-Txt.txt","w");
		file.write(response);
		file.close();
		'''
		directory =""

		tag_content_array = handler.tagParser('a', 'href', '/subtitles', False, response)
		user_array = handler.contentParser('a','href','/u',False,response)
		hi_array = handler.valueParser('td','class','a4',False,response)
		for index,hi in enumerate(hi_array):
			if hi == 'a41':
				hi_array[index]='HI'
			else:
				hi_array[index]=''

		#Remove elements if by HI
		tmp_hi = hi_array
		for index,hi in enumerate(tmp_hi):
			if HI == 'b':
				break
			if HI == 't' and hi != 'HI':
				del hi_array[index]
				del tag_content_array[index]
				del user_array[index]
			if HI == 'f' and hi == 'HI':
				del hi_array[index]
				del tag_content_array[index]
				del user_array[index]


		'''
		for hi in hi_array:
			print '\t-HI:'+hi+'\n'
		for user in user_array:
			print '\t-USER:'+user.strip()+'\n'
		'''
		#print len(tag_content_array)
		name_array = []
		for index,content in enumerate(tag_content_array):
			#print '-'+content.strip()+'\n-'
			link = content[0:content.find('"',0)];
			#print '\t-'+link+'\n'
			for item in handler.contentParser('span',None,None,False,content):
				name_array.append(item)
			content_array = handler.contentParser('span', 'class', 'l r '+icon, False, content)
			for c in content_array:
				c = c.strip()
				#print '\t-'+c+'\n'
				if c == LANG:
					url = "http://subscene.com"+link
					resp = handler.HTTPRequest(url)
					value_array = handler.valueParser('a', 'href', '/subtitle/download', False, resp)
					for value in value_array:
						if has_run == False:
							if DIR == 'fsub':
								directory = f + '/'
								if not os.path.exists(directory):
									os.makedirs(directory)
								os.rename(filename,directory+filename)
							if DIR == 'sub':
								directory = f + '/'
								if not os.path.exists(directory):
									os.makedirs(directory)
							has_run = True
						fname = name_array[index].strip()+"-"+user_array[index].strip()
						if(hi_array[index]!=''):
							fname+='-HI'
						fname+='.zip'
						fname = directory + fname
						#print fname
						url = "http://subscene.com"+value
						handler.downloadFile(url,fname)
						if EXTRACT:
							try:
								fh = open(fname, 'rb')
								z = zipfile.ZipFile(fh)
								for name in z.namelist():
									z.extract(name, directory)
								fh.close()
								os.remove(fname)
							except Exception as e:
								print str(e)
								if str(e) == "File is not a zip file":
									print "Using RarFile"
									#fh = open(fname, 'rb')
									z = rarfile.RarFile(fname)
									#for name in z.namelist():
									#	z.extract(name, directory)
									z.extractall()
									fh.close()
									os.remove(fname)


def assert_args(val,opts):
	for opt in opts:
		if val == opt:
			return True
	return False

def invalid_opts():
	print '*******Invalid Option*******'
	print 'Possible options:\ndir=fsub|sub(default none)\nhi=t|f|b(default)\nsub=1|*(default)\nlang=English(default)\nex=t(default)|f\npos=t|f(default)\nLast argument:Filename or a(default)'
	sys.exit(0)

	'''
	'''

#Start
#print 'START\n'
#Default values
current_file = ""
HI = 'b'
DIR = ''
SUB = '*'
LANG = 'English'
FILE = 'a'
EXTRACT = True
POSITIVE = False
icon = 'positive-icon'
#Process arguments
eles = len(sys.argv)
#print eles
for index,arg in enumerate(sys.argv):
	#print arg
	if index == 0:
		current_file = arg
	elif arg[0:5] == '-help':
		print "***************"
		print "The heightened sense of laziness is common, but it can also lead to great things!\n"
		print "Instructions to use Lazy-Subscene:"
		print "-dir->For directory operations. fsub->Place both subtitles & the file in a separate folder. sub->Place the subtitles in a separate folder."
		print "-hi->Search for Hearing Impaired subtitles. t->True. f->False. Both-> Include both in the results."
		print "-sub->Mention the number of subtitles to download. *->All the ones found. [Currently not available]."
		print "-lang->The language of the subtitle."
		print "-ex->Extract the zipped file. t->True. f-> False."
		print "-pos->Positive labeled subtitles. t->True. f->False."
		print "-Last argument->This should be mentioned only in the end, or not at all. filename. Or a->Includes all the files in the current directory."
		print "-help->To display the instructions."
		print "***************"
		sys.exit(0)
	elif arg[0:3] == '-hi':
		#print arg[3:len(arg)]
		if(assert_args(arg[4:len(arg)],['t','f','b'])):
			HI = arg[4:len(arg)]
		else:
			invalid_opts()
	elif arg[0:4] == '-dir':
		#print arg[4:len(arg)]
		if(assert_args(arg[5:len(arg)],['fsub','sub'])):
			DIR = arg[5:len(arg)]
		else:
			invalid_opts()
	elif arg[0:4] == '-sub':
		#print arg[4:len(arg)]
		if(assert_args(arg[5:len(arg)],['1','*'])):
			SUB = arg[5:len(arg)]
		else:
			invalid_opts()
	elif arg[0:5] == '-lang':
		#print arg[5:len(arg)]
		if(assert_args(arg[6:len(arg)],['English'])):
			LANG = arg[6:len(arg)]
		else:
			invalid_opts()
	elif arg[0:3] == '-ex':
		#print arg[3:len(arg)]
		if(assert_args(arg[4:len(arg)],['t','f'])):
			if arg[4:len(arg)] == 't':
				EXTRACT = True
		else:
			invalid_opts()
	elif arg[0:4] == '-pos':
		#print arg[4:len(arg)]
		if(assert_args(arg[5:len(arg)],['t','f'])):
			if arg[5:len(arg)] == 'f':
				POSITIVE = False
				icon = 'neutral-icon'
		else:
			invalid_opts()
	elif index == eles-1:
		#print arg
		if arg == 'a':
			pass
		elif arg != 'a':
			FILE = arg
		else:
			invalid_opts()
	else:
		invalid_opts()

mypath = os.getcwd()
s = Subscene()
if FILE == 'a':
	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	print onlyfiles
	for one_file in onlyfiles:
		if one_file != current_file:
			s.getSubtitle(one_file)
else:
	s.getSubtitle(FILE)


#l r positive-icon
#/subtitle/download?
#<td class="a1">
