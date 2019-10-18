class transac():
  def Withdraw():
    get=int(input('(Withdraw)Enter Amount:'))
    global Amount
    if Amount<get:
      print('Sorry you exceed, your current amount is:',Amount)
    else:
      Amount-=get
      print('Thank you for withdrawal. Your current amount is',Amount)

  def Deposit():
    put=int(input('(Deposit)Enter Amount:'))
    global Amount
    if put<0:
      print('Please enter reasonable value')
    else:
      Amount+=put
      print('Thank you for depositing. Your current amount is',Amount)
Custname=input(str('Enter your name: '))
Amount=10000
print('Current Amount:',Amount)
while True:
  choice = input("[W]- Withdraw, [D]-Deposit, [E]-Exit Choose Transaction:")
  if choice == 'W': transac.Withdraw()
  elif choice == 'D': transac.Deposit()           
  elif choice =='E':          
    print("Thank you", Custname," See us again")
    exit()                
  else:
    print("<<<Not in the choices>>>")
    continue
