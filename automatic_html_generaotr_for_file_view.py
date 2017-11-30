import os

path ="/mnt/64220DD6220DADDC/Story Books/Humayun Ahmed"

dirList=os.listdir(path)
htmlop="<html"
bodyop="<body style=\"background-color:#e6f2ff\">"
bodycls="</body>"
htmlcls="</html>"
header="<h2><u>EICT-2017<br>List of papers</u></h2>"
style= "<ul style=\"list-style-type:disc\">"
listop="<li>"
listclose="</li>"
newline="\n"
headop="<head>"
headcls="</head>"
title = "<title>EICT-2017</title>"
with open("EICT-2017.html", "w") as f:
#print "<html>"
    f.write(htmlop+newline)
    f.write(headop+newline)
    f.write(title+newline)
    f.write(headcls+newline)
    # print "<body>"
    f.write(bodyop+newline)
    # print "<ul style=\"list-style-type:circle\">"
    f.write(style+newline)
    # print "<h2>List of papers</h2>"
    f.write(header+newline)
    for path, subdirs, files in os.walk(path):
        for filename in files:
            temp=path + "/" +filename
            #print temp
            temp1="<a href=\""+temp+ "\"  target=\"_blank\">" + filename + "</a> <br>"
            # print "\t <li>"+temp1+"</li>"
            temp2="\t"+listop+temp1+listclose
            f.write(temp2+newline)
    # print "</body>"
    f.write(bodycls+newline)
    # print "</html>"
    f.write(htmlcls+newline)