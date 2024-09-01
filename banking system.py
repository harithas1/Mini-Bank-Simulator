total_info={"gowthami":{"mail":"gowthami@gmail.com","password":"#Sgowthami1","AC.no":1234,"amount":12000},"hemavathi":{"mail":"hemavathi@gmail.com","password":"&Shemavathi1","AC.no":4432,"amount":20000}}
names=list(total_info.keys())

# user_info=total_info["gowthami"]
# mail=user_info["mail"]
# password=user_info["password"]

ac_nums=[2345,5678]

name=input("\nEnter your name: ")

existing_user=input("\nAre you an existing account holder?(yes/no): ")


user_info={} #empty dictionary to store user info 

if name not in names and existing_user!="yes":
  names.append(name) #appending new user name
  print(f"\nHello, {name}! welcome Kedar to Bank!!") 
  sign_up_mail=input("\nPlease sign up with your mail id: ")
  set_password=input("\ncreate a strong password of min 8 characters using a "
                     "special character, small letter, capital letter and a number: ") #To set a pasword
  special="~!#$%^&*"
  small_alpha="abcdefghijklmnopqrstuvwxyz"
  cap_alpha="abcdefghijklmnopqrstuvwxyz".upper()
  nums='1234567890'
  if len(set_password)<8:
    print("\nPlease set a strong password of min 8 characters")
  valid=[]
  if len(set_password)>=8:
    if any(char in special for char in set_password):
      valid.append(1)
    if any(char in small_alpha for char in set_password):
      valid.append(2)
    if any(char in cap_alpha for char in set_password):
      valid.append(3)
    if any(char in nums for char in set_password):
      valid.append(4)
  if len(valid)<4: #If they created an invalid password
    print("\nInvalid password, please set a strong password")
    for i in range(10): #chance to create a strong password
      set_password=input("\ncreate a strong password of min 8 characters using a"
         " special character, small letter, capital letter and a number: ")
      if len(set_password)<8:
        print("\nPlease set a strong password of min 8 characters")
      valid=[]
      if len(set_password)>=8:
        if any(char in special for char in set_password):
          valid.append(1)
        if any(char in small_alpha for char in set_password):
          valid.append(2)
        if any(char in cap_alpha for char in set_password):
          valid.append(3)
        if any(char in nums for char in set_password):
          valid.append(4)
      if len(valid)<4:
        print("\nInvalid password, please set a strong password")
      if len(valid)>=4:
        break  #Chances to create password correctly
        
  user_info["mail"]=sign_up_mail #Appending mail id 
  user_info["password"]=set_password
  user_info["AC.no"]=ac_nums[0]
  user_info["amount"]=0
  total_info[name]=user_info
  
  print("\nPlease confirm your details",total_info[name])#Confirmation details
  confirm_details=input("\nIs the information provided above correct?(yes/no): ")
  if confirm_details!="yes":
    if name not in names and existing_user=="no":
        names.append(name) #appending new user name
        print(f"\nHello, {name}! welcome Kedar to Bank!!") 
        sign_up_mail=input("\nPlease sign up with your mail id: ")
        set_password=input("\ncreate a strong password of min 8 characters using a "
                           "special character, small letter, capital letter and a number: ") #To set a pasword
        special="~!#$%^&*"
        small_alpha="abcdefghijklmnopqrstuvwxyz"
        cap_alpha="abcdefghijklmnopqrstuvwxyz".upper()
        nums='1234567890'
        if len(set_password)<8:
          print("\nPlease set a strong password of min 8 characters")
        valid=[]
        if len(set_password)>=8:
          if any(char in special for char in set_password):
            valid.append(1)
          if any(char in small_alpha for char in set_password):
            valid.append(2)
          if any(char in cap_alpha for char in set_password):
            valid.append(3)
          if any(char in nums for char in set_password):
            valid.append(4)
        if len(valid)<4: #If they created an invalid password
          print("\nInvalid password, please set a strong password")
          for i in range(10): #chance to create a strong password
            set_password=input("\ncreate a strong password of min 8 characters using a"
               " special character, small letter, capital letter and a number: ")
            if len(set_password)<8:
              print("\nPlease set a strong password of min 8 characters")
            valid=[]
            if len(set_password)>=8:
              if any(char in special for char in set_password):
                valid.append(1)
              if any(char in small_alpha for char in set_password):
                valid.append(2)
              if any(char in cap_alpha for char in set_password):
                valid.append(3)
              if any(char in nums for char in set_password):
                valid.append(4)
            if len(valid)<4:
              print("\nInvalid password, please set a strong password")
            if len(valid)>=4:
              break
          print("Please confirm your details",total_info[name])
          confirm_details=input("\nIs the information provided above correct?(yes/no): ")
  else:
      print("Thank you for confirmation")
      
      
  
  
# print(total_info) ##for my clarity to check if new user info added or not

#Login existing user
l_name=input("\nPlease log in with your name: ")
  
if l_name in names:
  print("\nlogin with your mail and password")
  take_mail=input("\nEnter your mail id: ")
  if total_info[l_name]["mail"]!=take_mail:
    print("\nYou entered incorrect mail id.")
    for i in range(6):
      take_mail=input("\nPlease enter your correct mail id: ")
      if take_mail==total_info[l_name]["mail"]:
        break    
  take_password=input("\nEnter your password: ")
  if total_info[l_name]["password"]!=take_password:
    print("\nYou entered incorrect password")
    for i in range(6):
      take_password=input("\nPlease enter your correct password : ")
      if take_password==total_info[l_name]["password"]:
        break
  print(f"\nHey {l_name},\n\nYou logged into your account succesfuly!!")
  print(f"\nYour account number is {total_info[l_name]['AC.no']}")
  print(f"\nYour total balance is : Rs.{total_info[l_name]['amount']}/-")
  
  credit=input("\nDo you want to credit amount in your account?(yes/no): ")
  if credit=="yes":
    how_much_credit=float(input("\nPlease enter how much do you want to credit: "))
    total_info[l_name]["amount"]=total_info[l_name]["amount"]+how_much_credit
    print(f"\nYour total balance is : Rs.{total_info[l_name]['amount']}/-")
    
  debit=input("\nDo you want to Debit amount?(yes/no): ")
  if debit=="yes":
    how_much=float(input("\nEnter your how much you want to debit: "))
    total_info[l_name]["amount"]=total_info[l_name]["amount"]-how_much
    print(f"\nYour total balance is : Rs.{total_info[l_name]['amount']}/-")  
  
  transfer=input("\nDo you want to transfer to anyone?(yes/no): ")
  if transfer=="yes":
    trans_name=input("\nEnter the name of the person whom you want to transfer? : ")
    if trans_name in names:
      trans_mail=input("\nEnter receiver mail id: ")
      if trans_mail==total_info[trans_name]["mail"]:
        how_much_trans=float(input("\nhow much you want transfer? : "))
        total_info[trans_name]["amount"]+=how_much_trans
        # print("added succesfully: ",total_info[trans_name]["amount"])
        total_info[name]["amount"]-=how_much_trans
      print(f"\nYour total balance is :{total_info[name]['amount']}")




