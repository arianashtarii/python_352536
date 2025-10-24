import re

#from a to h and from 2 to 5 are accepted
#abcdefgh2345 are accepted
print(re.match("[a-h2-5]","7")) #Not Accepted
print(re.match("[a-h2-5]","a2")) #Accepted
print(re.match("aa[a-h]w","aacw")) #متنی که با دوتا آ شروع میشود و حرف سوم از آ تا اچ میتواند باشد و با دابلیو تمام میشود
#متنی را از کاربر بگیر که حرف اول از a تا h
#حرف دوم از 3 تا 5
#حرف آخر x باشد
print(re.match("[a-h][3-5]x","a3x")) #Accepted
print(re.match("[a-h][3-5]x","a7x")) #Not accepted

