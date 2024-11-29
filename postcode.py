import re

address = input("Insert Address somehow: ")
postcode = re.search(r"[A-Z]{1,2}+\d+[A-Z0-9]?\s?+[0-9]+[A-Z]{2}", address)

if postcode:
    print(postcode.group())
else:
    print("No postcode")