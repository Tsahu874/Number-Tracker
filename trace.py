import tkinter as tk
# Let's import the phonenumbers module to work with numbers
import phonenumbers as pn


# Let's see what is inside the phonenumbers directory
# print(dir(pn))

from phonenumbers import timezone, geocoder , carrier

def trace_number():
    number = entry.get()
    # we'll use pn.parse() function
    phone = pn.parse(number, None)
    if pn.is_valid_number(phone):
        # for timezone
        time = timezone.time_zones_for_number(phone)

        # for carrier
        car = carrier.name_for_number(phone, "en")

        # to see where the number is registered
        reg = geocoder.description_for_number(phone, "en")

        result_label.config(text =f"Phone number:{phone}\n"
            f"Timezone: {time}\n"
            f"Carrier: {car}\n"
            f"Region: {reg}")

   
    else:
        result_label.config(text="Invalid phone number.")

root = tk.Tk()
root.title("Contact Number Tracer")

label = tk.Label(root, text="Enter your phone number with +__:")
label.pack(pady = 10)

entry = tk.Entry(root, width = 50,bg ='#dbe2e9')
entry.pack(pady=20,padx = 20)

trace_button = tk.Button(root, text="Trace the number", bg= '#c8a2c8' ,command = trace_number)
trace_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)





root.mainloop()
