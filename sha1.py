
from hashlib import sha1
from django.utils.crypto import get_random_string

obj = sha1()
i = 0
while(True):
  i+=1
  s = get_random_string(length=20).encode('utf-8')
  obj.update(s)
  crypt = obj.hexdigest()
  print('tentativa %s string %s cript %s' % (i, s, crypt))
  if (crypt.endswith('0'*8)):
    break
