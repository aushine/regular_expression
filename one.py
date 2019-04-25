import re
UseTheApplication = True
s = r'ABC\-001'
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print(m.group(1))
print(m.group(2))
print(re.split(r"[\s\,]+", 'a,  b,    c ,,,, d'))