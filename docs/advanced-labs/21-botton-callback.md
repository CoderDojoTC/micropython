# Button Callback

```py
import re

def extract_gpio_pin(input_string):
    # Use a regular expression to find the GPIO number
    match = re.search(r"GPIO(\d+)", input_string)
    if match:
        # Convert the extracted number to an integer to remove leading zeros
        return int(match.group(1))
    else:
        # Return None if no match is found (or raise an exception if that's preferable)
        return None

# Test the function with examples
print(extract_gpio_pin("Pin(GPIO15, mode=IN, pull=PULL_UP)"))  # Output: 15
print(extract_gpio_pin("Pin(GPIO7, mode=IN, pull=PULL_UP)"))   # Output: 7
print(extract_gpio_pin("Pin(GPIO03, mode=IN, pull=PULL_UP)"))  # Output: 3

```


https://chat.openai.com/share/6e6d8123-ed4d-4dc6-a915-030fe2245dfe