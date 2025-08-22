import re

with open("data.txt", "r") as f:
    content = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", content)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted:", emails)
