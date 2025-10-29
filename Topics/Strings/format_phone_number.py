def format_phone_number(digits):
    digits = str(digits)
    return f"+{digits[0:1]} ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"

print(format_phone_number(39991234567))