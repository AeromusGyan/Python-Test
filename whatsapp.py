import pywhatkit

user_num = (input("Enter your Number which you want to send Message!!!"))

hour = int(input("Enter the Hour which time to send message"))

minute = int(input("Enter the Minute which time to send message"))

message = input("Enter the message what are you sending!!!")

pywhatkit.sendwhatmsg(user_num, message, hour, minute,)

print("This", message, "is sent to", user_num)
