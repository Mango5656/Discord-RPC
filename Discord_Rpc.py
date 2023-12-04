from pypresence import Presence
import time
import requests

def is_valid_url(url):
    try:
        response = requests.get(url)

        return response.status_code == 200
    
    except requests.RequestException:

        return False

client_id = input("Discord client_id:")

details = input("Details:")

state = input("State:")

large_image = input("large_image url:")

small_image = input("small_image url:")

large_text = input("large_text:")

small_text = input("small_text:")

button1 = input("button1 Name:")

button1_url = input("button1 url:")

button2 = input("button2 Name:")

button2_url = input("button2 url:")

RPC = Presence(client_id)
RPC.connect()

details_1 = details if details and len(details) >= 2 else None

state_1 = state if state and len(state) >= 2 else None

large_image_1 = large_image if large_image and len(large_image) >= 2 else None

small_image_1 = small_image if small_image and len(small_image) >= 2 else None

large_text_1 = large_text if large_text and len(large_text) >= 2 else None

small_text_1 = small_text if small_text and len(small_text) >= 2 else None

buttons_1 = [
    {"label": button1, "url": button1_url},

    {"label": button2, "url": button2_url},
    
] if button1 and button2 else None

if large_image_1 is not None and not is_valid_url(large_image_1):
    large_image_1 = None

if small_image_1 is not None and not is_valid_url(small_image_1):
    small_image_1 = None

try:
    RPC.update(
        details=details_1,

        state=state_1,

        large_image=large_image_1,

        small_image=small_image_1,

        large_text=large_text_1,

        small_text=small_text_1,

        buttons=buttons_1


    )
    print("Success。")

except Exception as e:
    print(f"fail。ERRO：{e}")


start = time.time()

while True:
    time.sleep(15)
