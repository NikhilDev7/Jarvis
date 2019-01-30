import os

def Format(file_name):
	f =open(file_name,'r')
	s = f.read()
	s = s.split('\n')
	return s[:-1]

# Gets all  .deskstop file_names
os.system('ls /usr/share/applications > App_List.txt')
Apps = Format('App_List.txt')

App_Dict = []
# Go through each file and find [(Name,Exec)]
for i in Apps:
	try:
		f = Format('/usr/share/applications/'+i)
		name = None
		Exec = None
		fg = 0
		for j in f:
			if fg==0:
				if 'Name=' in j:
					index = j.find('=')
					fg=1
					name = j[index+1:]
			if 'Exec=' in j:
				index = j.find('=')
				Exec = j[index+1:]
		# if fg==0:
		# 	for j in f:
		# 		if 'Name[en]' in j:
		# 			index = j.find('=')
		# 			name = j[index+1:]

		App_Dict.append((name,Exec))
	except:
		pass
print('[')
for i in App_Dict:
	print(i)
print(']')
