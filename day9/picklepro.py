import pickle
my_lis=[1,2,3,4,5]
my_dict={'name':'hari'}
my_str='asm tech'
f= open('ankit.txt','w')
pickle.dump(my_lis,f)
pickle.dump(my_dict,f)
pickle.dump(my_str,f)
f.close()

