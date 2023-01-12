URL = 'https://b2c.passport.rt.ru/'
valid_phone = "+79998769120"
valid_password = "Exa12!@#"
valid_mail = "abazaba717@gmail.com"
import random,string
random_mail = (f"{random.choice(['king','miller','kean'])}.{random.randint(100,999)}@{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5,7+1))}.{random.choice(['net','com','ru'])}").lower()
random_phone = f"+7999{random.randint(100,999)}{random.randint(10,99)}{random.randint(10,99)}"
random_phone_with_spaces = valid_phone[0:2]+" "+valid_phone[2:5]+" "+valid_phone[5:8]+"-"+valid_phone[8:10]+"-"+valid_phone[10:12]
print(random_mail)