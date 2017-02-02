import json
my_lis=[1,2,3,4,5]
my_dict={'name':'hari'}
my_str='asm tech'
f= open('ankit1w.txt','w')
json.dump(my_lis,f)
json.dump(my_dict,f)
json.dump(my_str,f)
f.close()
f=open('ankit1w.txt','r')
my_list=json.load(f)
