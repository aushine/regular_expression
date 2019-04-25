import re

a = re.match(r"(\d{1,4})(\d{1,4}?)(\d{1,4}?)", "123"[::-1])
print(a)
print(re.findall(r"\d{3}", "123456"))
email_ = input("输入一个邮箱地址:")
ret = re.match(r"[A-Za-z0-9_]{4,20}@(163|126)\.com$", email_)
if ret:
    print("输入的是符合规范的163邮箱地址")
else:
    print("输入的邮箱地址不符合163邮箱地址规范")