import os
import sys

ham_dic = {}
ham_num=0
#rootdir = sys.argv[1]
#rootdir =rootdir[:-1]
kk = 0
rootdir = '/Users/zailipeng/Desktop/my_research/Important_information/books/CS/csci544/HW1/SpamorHam/train'
for subdir, dirs, files in os.walk(rootdir):
    for file in dirs:
        filepath = subdir + os.sep + file

        if filepath.endswith("ham"):
            	for filename in os.listdir(filepath):
            		if filename.endswith(".txt"):
        	        		input = open(os.path.join(filepath, filename), 'r',encoding="latin1")
        	        		for line in input:
        
        	        			# lines = line.strip('\r')
        	        			lines = line.split()
        	        			# print(line)
        	        			for words in lines:
        	        				ham_num += 1
        	        				# print(words)
        		        			if words not in ham_dic:
        		        				ham_dic[words] = 1
        	        				else:
        	        					ham_dic[words] += 1

print(kk)
spam_dic = {}
spam_num=0
mm = 0
#rootdir = sys.argv[1]
rootdir = '/Users/zailipeng/Desktop/my_research/Important_information/books/CS/csci544/HW1/SpamorHam/train'
for subdir, dirs, files in os.walk(rootdir):
    for file in dirs:
        filepath = subdir + os.sep + file

        if filepath.endswith("spam"):
            	for filename in os.listdir(filepath):
            		if filename.endswith(".txt"):
#                    mm+=1
        	        		input = open(os.path.join(filepath, filename), 'r',encoding="latin1")
        	        		for line in input:
        
        	        			# lines = line.strip('\r')
        	        			lines = line.split()
        	        			# print(line)
        	        			for words in lines:
        	        				spam_num += 1
        	        				# print(words)
        		        			if words not in spam_dic:
        		        				spam_dic[words] = 1
        	        				else:
        	        					spam_dic[words] += 1
    

#print(spam_dic)
#print(ham_num,spam_num)
print(mm)                                

# calculate the prob of each token in ham 
dis_t = len(ham_dic) + len(spam_dic)      

ham_prop_dic = {}
ham_soomth = {}
for key, value in ham_dic.items():
    ham_prop_dic[key] = value/ham_num
    ham_soomth[key] = (value+1)/(ham_num+dis_t)

    
spam_prop_dic = {}
spam_soomth = {}
for key, value in spam_dic.items():
    spam_prop_dic[key] = value/spam_num
    spam_soomth[key] = (value+1)/(spam_num+dis_t)


P_spam = spam_num/(spam_num+ham_num)
P_ham = ham_num/(spam_num+ham_num)


ham_non = 1/(ham_num+dis_t)
spam_non = 1/(spam_num+dis_t)

# store all parameters in the nbmodel.txt 
filename = 'nbmodel.txt'
with open(filename,'w',encoding='latin1') as zaili:
	zaili.write("P_ham"+" "+str(P_ham)+ " "+ str(len(ham_prop_dic))+" "+str(ham_non)+ '\n')
	zaili.write("P_spam"+" "+str(P_spam)+ " "+ str(len(spam_prop_dic))+" "+str(spam_non)+ '\n')
	for key, value in ham_prop_dic.items():
		zaili.write(str(key)+" "+str(value)+" "+ str(ham_soomth[key])+'\n')

	for key, value in spam_prop_dic.items():
		zaili.write(str(key)+" "+str(value)+" "+ str(spam_soomth[key])+'\n')














