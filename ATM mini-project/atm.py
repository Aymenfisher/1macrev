class ATM(object):
  def __init__(self,money,bank_name):
    self.money=money
    self.bank_name=bank_name
    self.withdrawals_list=[]
  def withdraw(self,request):
    print "Welcome to ",self.bank_name
    print "Current Balance ",self.money
    print "=================================="

    given=self.money-request
    available_cash=[100,50,10,5,4,3,2,1]
    if request<=0 or request>self.money:
      print "you entered invalid , or i cant give you all that money boi !!"
      print "=================================="
      return
    index=0
    while request>0:
      if request>=available_cash[index]:
        print "Give",available_cash[index]
        request-=available_cash[index]
      else:
        index+=1
    self.money=given
    self.withdrawals_list.append(request)
    print "=================================="
  def show_withdrawals(self):
    for withdrawal in self.withdrawals_list:
        print(withdrawal)  