import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = (
    r"^[A-Z](?:(?=[-'])[a-z]*|[a-z]+)(?:[-'][A-Z][a-z]+)*"         # First name with optional internal hyphen/apostrophe part.
    r"(?: [A-Z](?:(?=[-'])[a-z]*|[a-z]+)(?:[-'][A-Z][a-z]+)*)?$"     # Optional last name (single space preceding it).
)
name_regex = re.compile(name)

phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

email_address = (
    r"^[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)*"  # Local part: starts with a letter, optional dot-separated groups.
    r"@[A-Za-z]+\.[A-Za-z]{2,}$"                  # Domain: letters, dot, and TLD (at least 2 letters).
)
email_regex = re.compile(email_address)
