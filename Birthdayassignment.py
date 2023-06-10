name = input ("Enter Recipient's name:")
age = input("Enter year of birth: ")
after_conv = int(age)
age2 = 2023 - after_conv
message = input ("Enter personalised message:")
sender_name = input ("Enter Sender's name:")

print ("Dear " + name + ",")
print ("let's celebrate your")
print ("years of awesomess!")
print ("Wishing you a day filled with joy " + "and laughter as you turn " + str(age2) + ".")
print (message)
print ("With love and best wishes,")
print (sender_name)