#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]==l2[j]):
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+["*"]+l2
                return[True,l]
    l=l1+["*"]+l2        
    return [False,l]            


p1=input("Enter the name of Male: ")
p2=input("Enter the name of Female: ")
p1=p1.lower()
p2=p2.lower()
p1=p1.replace(" ","")
p2=p2.replace(" ","")
l1=list(p1)
l2=list(p2)
flag_match_found=True
while flag_match_found:
    ret_list=remove_matching_letter(l1,l2)
    a=ret_list[1]
    l1=a[:a.index("*")]
    l2=a[a.index("*")+1:]
    flag_match_found=ret_list[0]
count=len(l1)+len(l2)
result=["Friends","Love","Affection","Marriage","Enemies","Siblings"]
if(count<=6):
    print()
    print(p2.upper() +" and "+p1.upper() +" shares the bond of "+result[count-1]) 
else:
    b=(count%6)-1 
    print(p2.upper() +" and "+p1.upper() +" shares the bond of "+result[b])  


# In[ ]:





# In[ ]:





# In[ ]:




