import time
import pyotp

key=""

totp =pyotp.TOTP(key)

print(totp.now())