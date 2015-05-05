import os,sys,shutil,stat,time,pwd,grp
from stat import *
from time import *

class bcolors:
    blue = '\033[94m'
    end= '\033[0m'

command=raw_input(">>>")
command=command.split()
length=len(command)

def size(a):
	print os.stat(a)[6],

def permission(a):
	find=""
	p=oct(os.stat(a)[ST_MODE])[-3:]
	for i in range(0,3):
		if int(p[i])==7:
			t="rwx"
		elif int(p[i])==6:
			t="rw-"
		elif int(p[i])==4:
			t="r--"
		find=find+t
	print "-"+find,	

def links(a):
	p=os.stat(a)[ST_NLINK]
	print p,
	stat_info=os.stat(a)
	uid=pwd.getpwuid(stat_info.st_uid)[0]
	gid=grp.getgrgid(stat_info.st_gid)[0]
	print uid+" "+gid,

def time(a):
	a=os.stat(a)
	find=ctime(a.st_mtime)
	find=find[4:-8]
	print find,

if command[0]=="ls" and command[1]=="-l":
	directory=os.listdir("./")
	for files in sorted(directory,key=lambda s:s.lower()):
		permission(files)
		links(files)
		size(files)
		time(files)
		print files

elif command[0]=="ls":
	if length==1:
		if os.path.isdir("./"):
			directory=os.listdir("./")
			for files in sorted(directory,key=lambda s:s.lower()):
				if os.path.isdir(files):
					print bcolors.blue+files+" "+bcolors.end,
				else:
					print files+" ",
			print 
	else:		
		i=1
		while (i<length):
			try:
				if os.path.isdir("./"+command[i]):
					print command[i]+":"
					directory=os.listdir("./"+command[i])
					for files in sorted(directory,key=lambda s:s.lower()):
						if os.path.isdir("./"+command[i]+"/"+files):
							print bcolors.blue+files+" "+bcolors.end,
						else:
							print files+" ",
					print 
				elif os.path.isfile("./"+command[i]):
					print command[i]+":"
				else:
					print command[i]+" doesnt exist"	
			except Exception, e:
				print "unexceptional handling"
			i=i+1

if command[0]=="mv":
	if length==1:
		print "mv: missing file operand"
		print "Try 'mv --help' for more information."
	elif length==2:
		print "mv: missing destination file operand after `"+command[1]+"`"
		print "Try 'mv --help' for more information."
	else:
		i=1
		while(i<length-1):
			try:
				os.rename(command[i],command[length-1])
				if (os.path.isfile("./"+command[i])):
					os.remove("./"+command[i])
				elif(os.path.isdir("./"+command[i])):
					os.rmdir("./"+command[i])
			except Exception, e:
				print "Can't nove"+command[i]
			i=i+1

if command[0]=="cp":
	if length==1:
		print "cp: missing file operand"
		print "Try 'cp --help' for more information."
	else:
		i=1
		while(i<length-1):
			try:
				shutil.copy2("./"+command[i],"./"+command[length-1])	
			except Exception, e:
				print "Can't copy" + command[i]
			i=i+1

if command[0]=="rm":
	if length==1:
		print "rm: missing operand"
		print "Try 'rm --help' for more information."
	else:
		i=1
		while(i<length)-1:
			try:
				os.remove("./"+command[i])
			except Exception, e:
				print "File/Dir doesnt exist"+command[i]
			i=i+1
			
			
if command[0]=="dirstir":
	l=[]
	def function(a,name,count):
		global l
		way=os.path.abspath(a)
		count=count+1
		if os.path.isdir(way):
			l=l+[a]
			#print name+" "+str(count)
			for i in range(0,count):
				print "|",
			print "|"
			for i in range(0,count):
				print "|",
			print "#------Folder Name:"+name+"/------#"
			directory=os.listdir(way)
			if not directory:
				for i in range(0,count+4):
					print " ",
				print "(EMPTY FOLDER)"
			for i in sorted(directory,key=lambda s:s.lower()):
				function(a+"/"+i,i,count)
		else:
			l=l+[a]
			for i in range(0,count):
				print "|",
			print "|"
			for i in range(0,count):
				print "|",
			print "#-"+name

	current=os.getcwd()
	p=current.split("/")
	make=p[-1]
	function(current,make,count=-1)





