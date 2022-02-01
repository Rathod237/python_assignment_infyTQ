def find_common_characters(msg1,msg2):    
    result=[]
    string=''
    if(len(msg1)<len(msg2)):
        for i in msg1:
            i.strip()
            if i in msg2:
                result.append(i)
    elif len(msg1)==len(msg2): 
        for i in msg2: 
            if(i in msg1): 
                result.append(i)
    else:
        for i in msg2: 
            if(i in msg1): 
                result.append(i)
       
    for i in result:
        string+=i                                
    if len(string)>0:
       return string
    else:
        return -1   
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)  
       