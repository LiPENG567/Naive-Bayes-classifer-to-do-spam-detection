import os
import math
import sys

# read the nbmodel.txt
input = open('nbmodel.txt', 'r', encoding="latin1")
l1 = input.readline().replace('\n','').replace('\r','')
l1 = l1.split()
P_ham = float(l1[1])
N_ham = int(l1[2])
ham_non = float(l1[3])

l2 = input.readline().replace('\n','').replace('\r','')
l2 = l2.split()
P_spam = float(l2[1])
N_spam = int(l2[2])
spam_non = float(l2[3])

dis_t = N_ham + N_spam # number of unique voc

print(P_ham,P_spam)
print(N_ham,N_spam)

ham_prop_dic = {}
ham_prop_soomth = {}

i = 1
while i <= int(N_ham):
    N_line = input.readline().replace('\n','').replace('\r','')
    N_line = N_line.split()
    ham_prop_dic[N_line[0]] = float(N_line[1])
    ham_prop_soomth[N_line[0]] = float(N_line[2])
    i+=1


spam_prop_dic = {}
spam_prop_soomth = {}
i = 1
while i <= int(N_spam):
    N_line = input.readline().replace('\n','').replace('\r','')
    N_line = N_line.split()
    spam_prop_dic[N_line[0]] = float(N_line[1])
    spam_prop_soomth[N_line[0]] = float(N_line[2])
    i+=1


#print(spam_prop_dic)

class_out = {}

# ham_num=0
#rootdir = sys.argv[1]
#rootdir =rootdir[:-1]
rootdir = '/Users/zailipeng/Desktop/my_research/Important_information/books/CS/csci544/HW1/SpamorHam/dev'
for subdir, dirs, files in os.walk(rootdir):
    for file in dirs:
        filepath = subdir + os.sep + file
        for filename in os.listdir(filepath):
            if filename.endswith(".txt"):
#                print(filename)
                corp = {}
                p_ham_class = math.log10(P_ham)             
                p_spam_class = math.log10(P_spam)
                print(p_spam_class)
                input = open(os.path.join(filepath, filename), 'r',encoding="latin1")
                for line in input:
                    lines = line.split()
                    for wordss in lines:
                        if wordss not in corp:
                            corp[wordss] =1
                        else:
                            corp[wordss] +=1
                if all(i in ham_prop_dic for i in corp) == False or all(i in spam_prop_dic for i in corp) == False:
                    for words in corp:
#                        print(words)
                        if words not in ham_prop_dic:
                            new_ham_prop_dic = ham_non
                        else:
#                            b = (ham_prop_dic[words]).as_integer_ratio()
                            new_ham_prop_dic = ham_prop_soomth[words]
                        p_ham_class += (math.log10(new_ham_prop_dic))*corp[words]
#                        print(corp[words])
                        
                        if words not in spam_prop_dic:
                            new_spam_prop_dic = spam_non
                        else:
#                            b = (spam_prop_dic[words]).as_integer_ratio()
                            new_spam_prop_dic = spam_prop_soomth[words]
                        p_spam_class += (math.log10(new_spam_prop_dic))*corp[words]
#                        print(p_spam_class)                        
                        
                else:
                    for words in corp:
                        p_ham_class += (math.log10(ham_prop_dic[words]))*corp[words]
                        p_spam_class += (math.log10(spam_prop_dic[words]))*corp[words]
                
#                flag == True:
#                    for wod in corpus:
#                        p_ham_class += math.log10(ham_prop_dic[words])
                        
                        

                
#print(corpus)
                        
#                        if words in ham_prop_dic:
#                            p_ham_class += math.log10(ham_prop_dic[words])
#                        if words not in ham_prop_dic:
#                            p_ham_class += math.log10(ham_prop_dic[words])
##                            p_ham_class *= ham_prop_dic[words]
#                        if words in spam_prop_dic:
##                            p_spam_class *= spam_prop_dic[words]
#                            p_spam_class += math.log10(spam_prop_dic[words])
#                        if words in spam_prop_dic:
#                            p_spam_class += math.log10(spam_prop_dic[words])
                            
#                print(p_ham_class,p_spam_class)
                        
                if p_ham_class > p_spam_class:
                    class_out[filepath+os.sep+filename] = 'ham'
                else:
                    class_out[filepath+os.sep+filename] = 'spam'
#print(class_out)
                

filename = 'nboutput.txt'
with open(filename,'w',encoding='latin1') as zaili:
	for key, value in class_out.items():
		zaili.write(str(value)+"\t"+str(key)+'\n')
#  
