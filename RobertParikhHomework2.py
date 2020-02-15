#Robert Parikh
#Homework 2

#Part A

shortActing = ['Humulin', 'Novolin']
rapidActing = ['NovoLog', 'FlexPen', 'Fiasp', 'Apidra']
perscribed = input('What medication has the patient been prescribed \n>>')
if perscribed == 'Humulin':
    print('The patient is a diabetic')
elif perscribed == 'Novolin':
    print('The patient is a diabetic')
elif perscribed == 'Novolog':
    print('The patient is a diabetic')
elif perscribed == 'FlexPen':
    print('The patient is a diabetic')
elif perscribed == 'Fiasp':
    print('The patient is a diabetic')
elif perscribed == 'Apidra':
    print('The patient is a diabetic')
else:
    print('The patient is not a diabetic')
 

# Part B

offer = float(input('How much are you asking?\n>>'))
if offer >= 500:
    print('Sorry, that price is too high for me')
else:
    print('Ok, I would like to purchase it')


#Part C

#y = 'Yen'
#d = 'Dollar'
#e = 'Euro'
#p = 'Pound'

yenConv = [1, 0.0092, 0.0084, 0.0074]
dollarConv = [108.2113, 1, 0.9052, 0.8012]
euroConv = [119.5597, 1.1048, 1, 0.8852]
poundConv = [135.0645, 1.2481, 1.1296, 1]
startAmount = float(input('Enter the amount of money you wish to convert?\n>>'))
baseCur = str(input('What is the base currency you wish to convert FROM? Enter y for Yen, d for Dollar, e for Euro, p for Pound.\n>>'))
convCur = str(input('What is the base currency you wish to convert TO? Enter y for Yen, d for Dollar, e for Euro, p for Pound.\n>>'))

if baseCur is 'y' and convCur is 'y':
   print ('¥', startAmount*yenConv[0])
if baseCur is 'y' and convCur is 'd':
       print('$', startAmount*yenConv[1])
if baseCur is 'y' and convCur is 'e':
       print('€', startAmount*yenConv[2])
if baseCur is 'y' and convCur is 'p':
       print('£', startAmount*yenConv[3])
if baseCur is 'd' and convCur is 'y':
       print('¥', startAmount*dollarConv[0])
if baseCur is 'd' and convCur is 'd':
       print('$', startAmount*dollarConv[1])
if baseCur is 'd' and convCur is 'e':
       print('€', startAmount*dollarConv[2])
if baseCur is 'd' and convCur is 'p':
       print('£', startAmount*dollarConv[3])
if baseCur is 'e' and convCur is 'y':
       print('¥', startAmount*euroConv[0])
if baseCur is 'e' and convCur is 'd':
       print('$', startAmount*euroConv[1])
if baseCur is 'e' and convCur is 'e':
       print('€', startAmount*euroConv[2])
if baseCur is 'e' and convCur is 'p':
       print('£', startAmount*euroConv[3])
if baseCur is 'p' and convCur is 'y':
       print('¥', startAmount*poundConv[0])
if baseCur is 'p' and convCur is 'd':
       print('$', startAmount*poundConv[1])
if baseCur is 'p' and convCur is 'e':
       print('€', startAmount*poundConv[2])
if baseCur is 'p' and convCur is 'p':
       print('£', startAmount*poundConv[3])



   
 