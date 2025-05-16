import pywhatkit

phone = input("Enter the phone number with country code (e.g., +91XXXXXXXXXX): ")
message = input("Enter the message you want to send: ")

pywhatkit.sendwhatmsg_instantly(phone_num=phone, message=message, wait_time=20, tab_close=True)

print("Message sent.")
