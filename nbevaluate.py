# read the nboutput.txt
import sys
pre_ham = 0
pre_spam = 0

true_ham = 0
true_spam = 0

pre_cor_ham = 0
pre_cor_spam = 0

rec_cor_ham = 0
rec_cor_spam = 0
#filename = sys.argv[1]
#input = open('filename', 'r', encoding="latin1")
input = open('nboutput.txt', 'r', encoding="latin1")
#print(input)
for line in input:
    lines = line.split('\t')
    pre = lines[0]
    path = lines[1]
    if pre == 'ham':
        pre_ham += 1
    if pre == 'spam':
        pre_spam += 1
        
    if path.count('ham')>1:
        true_ham += 1
    if path.count('spam')>1:
        true_spam += 1
        
    if pre == 'ham' and path.count('ham')>1:
        pre_cor_ham += 1
        
    if pre == 'spam' and path.count('spam')>1:
        pre_cor_spam += 1
    
        
#print(pre_cor_ham)

print(true_ham,true_spam)
print(pre_ham,pre_spam)

precision_ham = pre_cor_ham / pre_ham
recall_ham = pre_cor_ham / true_ham 
F1_ham = 2*precision_ham*recall_ham/(precision_ham+recall_ham)

precision_spam = pre_cor_spam / pre_spam
recall_spam = pre_cor_spam / true_spam 
F1_spam = 2*precision_spam*recall_spam/(precision_spam+recall_spam)

print(precision_ham,recall_ham,F1_ham)
print(precision_spam,recall_spam,F1_spam)


