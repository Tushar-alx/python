'''
create module communicator which has below methods 
    sendsms which has mobile no message as argument 
        decrease credit by 2
    sendWhatmsg which has mobile no message as argument
        decrease credit by 1.5
    sendEmail which has email & message as argument
        decrease credit by 1
    increaseCredit(points)
        increase credit variable using value given in points (must be positive)

    use can send sms/msg/email only when he has sufficient credit (global variable) 
        deduct credit variable as per value given above 
    initial credit value will be 10
'''

credit = 0
def sendsms(mobile_no, message):
    global credit
    if credit >= 2:
        credit -= 2
        print(f"SMS sent to {mobile_no}: {message}")
    else:
        print("Not enough credit to send SMS.")

def sendWhatmsg(mobile_no, message):
    global credit
    if credit >= 1.5:
        credit -= 1.5
        print(f"WhatsApp message sent to {mobile_no}: {message}")
    else:
        print("Not enough credit to send WhatsApp message.")

def sendEmail(email, message):
    global credit
    if credit >= 1:
        credit -= 1
        print(f"Email sent to {email}: {message}")
    else:
        print("Not enough credit to send Email.")

def increaseCredit(points):
    global credit
    if points > 0:
        credit += points
        print(f"Credit increased by {points}. Total credit: {credit}")
    else:
        print("Points must be positive.")

increaseCredit(10)