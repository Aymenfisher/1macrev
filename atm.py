money=500
def atm(request):
	available_cash=[100,50,10,5,4,3,2,1]
	given=money-request
	if request<=0 or request>money:
		print  "Please enter a valid value"
		return
	index=0	
	while request>0:
		if request>=available_cash[index]:
			print "Give",available_cash[index]
			request-=available_cash[index]
		else:
			index+=1		
atm(277)




			
