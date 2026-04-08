import pyotp
import qrcode

# Generate secret key
secret = pyotp.random_base32()
print("Secret Key:", secret)

# Generate QR code
uri = pyotp.totp.TOTP(secret).provisioning_uri(
    name="user@example.com",
    issuer_name="MyApp"
)

img = qrcode.make(uri)
img.save("qrcode.png")

print("QR code saved as qrcode.png")

# Generate OTP
totp = pyotp.TOTP(secret)
print("Current OTP:", totp.now())

# Verify OTP
user_otp = input("Enter OTP: ")

if totp.verify(user_otp):
    print("Login successful ✅")
else:
    print("Invalid OTP ❌")