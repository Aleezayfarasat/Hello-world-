# UC San Diego Health Phishing Attack – Final Project (CS50 Introduction to Cybersecurity)

**Author:** Aleezay Farasat  
**Country:** Pakistan  
**edX Username:** aleezay_farasat  
**GitHub:** [aleezayfarasat](https://github.com/aleezayfarasat)  
**Recorded on:** 16 August 2025  
YouTube vedio:https://youtu.be/keu5TO0kLVc?si=yaJy4ILNNWsOJ0_o
---

## 📌 Project Overview

This project is my final submission for **CS50’s Introduction to Cybersecurity**.  
My topic is the **UC San Diego Health phishing attack** from January 2024, covered in **Lecture 3** on phishing.  

I chose this topic because I am a medical student, and it connects both to my academic field and my interest in cybersecurity. The project also includes a **simple Python phishing email detector** that scans emails for suspicious keywords and warns the user if the email may be unsafe.

---

## 📰 Case Background: UC San Diego Health Phishing Attack

- **Date of Incident:** January 9–22, 2024  
- **Cause:** Two employees clicked on malicious email links and entered their credentials.  
- **Risk:** Exposure of sensitive patient information.  
- **Investigation Completed:** February 2024  

**Impact:**
- Exposure of **confidential patient data**.
- Threat to **privacy, trust, and reputation**.
- Potential **financial losses** and operational disruption.
- Highlighted the **critical need for cybersecurity in healthcare**.

---

## 🔍 How It Was Detected

- Unusual email activity was spotted through **security monitoring**.  
- Staff **reported suspicious messages**.  
- Automated alerts flagged **potentially malicious links**.  
- A quick IT response helped contain the threat.

---

## ⚠️ Key Vulnerabilities

1. No robust **email filtering**.  
2. **Password reuse** by staff.  
3. **Human error** — clicking malicious links without verification.  

---

## 🛠️ My Project: Phishing Email Detector

A **simple Python tool** that:
- Scans the text of an email.  
- Looks for suspicious keywords such as `urgent`, `click here`, `password`.  
- Warns the user if the email may be a phishing attempt.  

---

### 💻 Technology Used

- **Language:** Python  
- **Environment:** CS50 IDE  

---

## 📂 How It Works

1. **User enters** an email text into the program.  
2. Program **checks** for predefined suspicious keywords.  
3. **Output:**
   - If found → Displays a **warning**.  
   - If not found → Marks the email as **safe**.
4. code snipet:# List of suspicious keywords
suspicious_words = ["urgent", "verify", "click here", "update account", "password", "login", "bank", "confirm"]

# Input email text
email_text = input("Paste the email text here:\n").lower()

# Check for suspicious keywords
found_words = [word for word in suspicious_words if word in email_text]

if found_words:
    print(f"⚠ WARNING: This email may be a phishing attempt! Suspicious words found: {found_words}")
else:
    print("✅ This email seems safe. (But always double-check!)")
5. for improved output:import logging

# Set up logging
logging.basicConfig(filename='phishing_alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# List of suspicious keywords
suspicious_words = ["urgent", "verify", "click here", "update account", "password", "login", "bank", "confirm", "prize"]

# Function to check phishing keywords and log results
def check_phishing_and_log(email_text):
    found_words = [word for word in suspicious_words if word in email_text.lower()]
    
    if found_words:
        alert_message = f"⚠ WARNING: This email may be a phishing attempt! Suspicious words found: {found_words}"
        logging.info(alert_message)  # Log the suspicious email
        return alert_message
    else:
        return "✅ This email seems safe. (But always double-check!)"

# Input email text
email_text = input("Paste the email text here:\n")
result = check_phishing_and_log(email_text)
print(result)
---

## 📧 Example

**Phishing Email Example:**
- From an unverified sender.
- Urgent or alarming tone.
- Includes suspicious links.

**Safe Email Example:**
- From a trusted source.
- Professional and clear tone.
- No requests for sensitive data.

---

## 🚀 Future Improvements

- Integrate **machine learning** for advanced phishing detection.  
- Expand keyword and pattern database for better accuracy.  
- Add **real-time alerts**.  
- Improve **user interface** for better usability.

---

## 🛡️ Recommendations for Prevention

1. **Raise awareness** among healthcare workers.  
2. Use **multi-factor authentication** (MFA).  
3. Apply **email filtering** and anti-phishing tools.  
4. **Verify senders** before clicking links.

---

## 📚 Lessons Learned

- Writing basic Python code.  
- Searching for text patterns.  
- Understanding the **cybersecurity risks** in healthcare.  

> **Conclusion:** Even simple tools can play an important role in defending against phishing. Awareness is the strongest defense — knowledge is an asset in any field.

---

## 📂 Repository

This repository contains:
- Python code for the phishing detector.
- Example phishing and safe emails.
- Documentation of the UC San Diego Health phishing attack case.
## 📌 Note to Grader  

This is my very first coding project.  
As a **medical student with no prior programming background**, I wanted to challenge myself by connecting what I learned in CS50 Cybersecurity with a real-world healthcare phishing case.  

My goal was not to build a perfect phishing detector, but to show **effort, curiosity, and a basic working program** that links medicine and cybersecurity.
