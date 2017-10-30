options={
	'F':'find',
	'A':'add',
	'C':'change',
	'D':'delete',}
finder=['age','dept','eroll_date']
filepath = 'staff.txt'
out_file = 'staff_out.txt'
Staff_Msg = []

def input_choise():
	for i in options:
		print('%s  %s'%(i,options[i]))
	choi = input(">>Input option (F/A/C/D)?:").strip()
	option = options[choi]
	return option

def open_read(filepath):
	with open(filepath,'r') as fp:
		for line in fp:
			L = line.split(',')
			# print(L)
			staff = {'ID':L[0],'name':L[1],'age':L[2],'phone':L[3],'dept':L[4],'eroll_date':L[5]}
			# print(staff)
			Staff_Msg.append(staff)
	for i in Staff_Msg:
		print(i)

def find_msg():###输出的格式未修改
	for i in range(len(finder)):
		print('>>%s'%(finder[i]))
	choise = input(">>find by (age/dept/eroll_date):").strip()
	fator = input(">>term:").strip()
	if choise == 'age':
		for dic in Staff_Msg:
			if int(dic['age']) > int(fator):
				print(dic)
	elif choise == 'dept':
		for dic in Staff_Msg:
			if dic['dept'] == fator:
				print(dic)
	elif choise == 'eroll_date':
		for dic in Staff_Msg:
			if dic['eroll_date'][0:4] == fator:
				print(dic)
	else:
		print("wrong input or Not support!")

def add_msg():
	new_l = input('>>new staff infomation:"name age phone dept eroll_date:"\n>>').split(',')
	ID = len(Staff_Msg) + 1
	new_l.insert(0,ID) 
	print(new_l)
	# dic = {'ID':L[0],'name':L[1],'age':L[2],'phone':L[3],'dept':L[4],"eroll_date":L[5]}
	# Staff_Msg.append()
	msg = '%s,%s,%s,%s,%s,%s'\
	     %(new_l[0],new_l[1],new_l[2],new_l[3],new_l[4],new_l[5])
	with open(filepath,'a') as fp:
		fp.seek(2)
		fp.write('\n'+msg)

def change_msg():
	for dic in Staff_Msg:
		if dic["dept"] == 'IT':
			dic['dept'] = 'Market'
		print(dic)

def delete_msg():
	id_in = input(">>input delete ID:").strip()
	for dic in Staff_Msg:
		if dic['ID'] == id_in:
			Staff_Msg.remove(dic)
	for dic in Staff_Msg:
		if dic['ID'] > id_in:
			dic['ID'] = int(dic['ID']) - 1
	for i in Staff_Msg:
		print(i)

def output_msg(out_file):
	with open(out_file,'w') as fp:
		for dic in Staff_Msg:
			msg = '%s,%s,%s,%s,%s,%s'\
			%(dic['ID'],dic['name'],dic['age'],dic['phone'],dic['dept'],dic['eroll_date'])
			fp.write(msg)
	
open_read(filepath)
option = input_choise()
print(option)
if option == 'add':
	add_msg()
elif option == 'delete':
	delete_msg()
elif option == 'change':
	change_msg()
elif option == 'find':
	find_msg()
output_msg(out_file)
