user=int(raw_input("enter a number"))
index=0
new=[]
while index<(user):
	user1=int(raw_input("enter a number"))
	if user1 not in new:
		new.append(user1)
	index=index+1
print new
