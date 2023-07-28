# Let's import the phonenumbers module to work with numbers
import phonenumbers as pn


# Let's see what is inside the phonenumbers directory
# print(dir(pn))

from phonenumbers import timezone, geocoder , carrier

# any phonenumber should be in a form of string
# +91 --->(country code) represents India
number = input("Enter your No. with +__ : ")

# we'll use pn.parse() function
phone = pn.parse(number, None)
if pn.is_valid_number(phone):
    # for timezone
    time = timezone.time_zones_for_number(phone)

    # for carrier
    car = carrier.name_for_number(phone, "en")

    # to see where the number is registered
    reg = geocoder.description_for_number(phone, "en")

    # for printing phone number and timezone
    print(phone)
    print(time)
    print(car)
    print(reg)

else:
    print("Invalid phone number.")

# except pn.NumberParseException:
    # print("Invalid phone number format.")   