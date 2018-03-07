balance=500
def atm(money,request):
	given=money-request
	available_cash=[100,50,10,5,4,3,2,1]
	if request<=0 or request>money:
		print  "you entered invalid number , or i cant give you all this money boi !!"
		return
	index=0	
	while request>0:
		if request>=available_cash[index]:
			print "Give",available_cash[index]
			request-=available_cash[index]
		else:
			index+=1
	return given		
			






			
