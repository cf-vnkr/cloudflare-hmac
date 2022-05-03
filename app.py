import hmac
import base64
import time
import urllib.parse
import hashlib

base_url = "https://example.none/"
path="/some-path"

secret = "thisisasharedsecret"
time   = str(int(time.time()))
digest = hmac.new(bytes(secret, 'utf-8'), bytes(path + time,'utf-8'), hashlib.sha256)
blob=base64.b64encode(digest.digest()).decode("ascii")
param  = urllib.parse.urlencode({'verify': '{time}-{blob}'.format(time=time, blob=blob)})

print (param)
