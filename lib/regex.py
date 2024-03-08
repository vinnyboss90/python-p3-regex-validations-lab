import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-z']*(?:'[A-Z][a-z]+)?(?: [A-Z][a-z']*(?:'[A-Z][a-z]+)?)*(?:-[A-Z][a-z']*(?:'[A-Z][a-z]+)?)?"
name_regex = re.compile(name)

# phone_number = r"[0-9]*(([0-9]{3})?-+[0-9]{3}-+[0-9]{4})?"
phone_number = r"\d*(\d{3}-+)*(\(\d{3}\''+)*((\d{3}-+\d{4})?"
phone_number = r"\(?(\d{3})\)? ?-?(\d{3})-?(\d{4})"
phone_regex = re.compile(phone_number)

email_address = r"\b(?!\d)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_regex = re.compile(email_address)