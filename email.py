import re

email = input("Enter email: ").strip()

if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|nhs.net)$", email):
    if re.search(".ac.uk", email):
        print("Valid Academic Email.")
    elif re.search(".gov.uk", email):
        print("Valid Government Email.")
    elif re.search(".nhs.net", email):
        print("Valid NHS Email.")

else:
    print("Not Valid")
