s="A python script"
print (s[0])
print(s[2:7])
print (s[:8])
print (s[8:])
print (s[2:999])
message= 'Document "cv.doc" was printed on printer: Xerox'
print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp=message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

print("nok")
fdd