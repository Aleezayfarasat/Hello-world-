# Simple Phishing Email Detector
# By [Aleezay farasat]

# List of suspicious keywords
suspicious_words = ["urgent", "verify", "click here", "update account", "password", "login", "bank", "confirm", "payment", "limited time"]

print("=== Phishing Email Detector ===")
email_text = input("Paste the email text here:\n").lower()

# Check if any suspicious word appears in the email
found_words = [word for word in suspicious_words if word in email_text]

if found_words:
    print("\n⚠ WARNING: This email may be a phishing attempt!")
    print("Suspicious words found:", ", ".join(found_words))
else:
    print("\n✅ This email seems safe. (But always double-check!)")
