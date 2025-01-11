API_KEYS = [
    'AIzaSyA06DBE5hA08uJd3_tya3qa3tiYQHYir4M',
    'AIzaSyA5dbJYNMkWVYD9G_ijW1pB-w1WQpFdlMQ',
    'AIzaSyAcMJs34OTSybGk_KeYnpkJQxi6k4eZcg4',
    'AIzaSyAD8I54SAvCHeXRZV0tsol1_fNXwzyQkGw',
    'AIzaSyD-YIfs2MWNPvHNVasp-04K_eiRTTUDl80',
    'AIzaSyDhMGVY2WGwCn1pQ-u3qUvPr1Opmi257dQ',
    'AIzaSyDMQ9AYz6ro2-clCnLZYB2LeCTd9h51dAg',
    'AIzaSyAUIYoAJcd8NfV83pNjGqxF3mvJfY5reZ8',
]

key_index = 0

def get_next_api_key():
    global key_index
    key = API_KEYS[key_index]
    key_index = (key_index + 1) % len(API_KEYS)
    return key


