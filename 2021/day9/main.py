import json
import binascii


def decrypt(encoded_str):
    algorithm = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "J"], [
        "L", "M", "N", "O", "P"], ["Q", "R", "S", "T", "U"], ["V", "W", "X", "Y", "Z"]]
    encoded_str = [char.strip()
                   for char in encoded_str.split(" ") if len(char) > 0]
    decrypted_str = ""
    for char in encoded_str:
        decrypted_str += algorithm[int(char[0])-1][int(char[1])-1]
    return decrypted_str


messages = []
with open("network_data.json") as f:
    for tcp in json.load(f):
        temp = tcp["_source"]["layers"]["tcp"]["tcp.payload"].split(":")
        hex_string = "".join(e for e in temp)
        ascii_string = binascii.unhexlify(hex_string)
        decoded = decrypt(ascii_string)
        messages.append(decoded)

flag_line = 0
for i, message in enumerate(messages):
    if "PST" in message:
        flag_line = i + 1

ip = None
with open("network_data.json") as f:
    data = json.load(f)
    for e in data:
        if e["_source"]["layers"]["frame"]["frame.number"] == str(flag_line):
            ip = e["_source"]["layers"]["ip"]["ip.src"]

ip_encrypted = " ".join(num for num in ip.split("."))
source_ip = decrypt(ip_encrypted)

message = messages[flag_line - 1]
message = message[16:91]
message = message.replace("APOSTROF", "")
message = message.replace("CROLLPARANTESSLUTT", "")
message = message.replace("CROLLPARANTES", "")
message = message.replace("C", "K")
message = message[1:]
message = message.replace("SOURKEIP", source_ip)
print("PST{%s}" % message)
