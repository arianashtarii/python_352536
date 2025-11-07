#Regular Expression ---> regex ----> re ----->import re
import re



#re.match("olgoo","matn")
#print(re.match(r"^[a-zA-Z\s]{3,30}$","matn"))
print(re.match(r"^[a-zA-Z\s]{3,30}$","alireza")) #accepted
# a or f or h or m accepted in string
print(re.match(r"[afhm]","a")) #accepted
print(re.match(r"[afhm]","b")) #Not accepted #None
print(re.match("[a-z]","1")) #Not accepted #None
print(re.match("[1-4]","1")) #accepted
print(re.match("[1-4]","7")) #Not accepted #None
