import re
TEXT = open('text_emails.txt', 'r').read()
print(TEXT)
filtered = re.findall(r'\b[a-zA-Z0-9._%+\"-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', TEXT)


print(filtered)