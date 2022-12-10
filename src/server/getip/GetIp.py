#lets make this very ez
from requests import get
import yaml

ip = get('https://api.ipify.org').content.decode('utf8')
port = None

# some checking
in1 = input("What port do you want to assign? (redis runs defaultly on 6379):")
port = int(in1)

data = {
    "ip_address": ip,
    "port": port
}

with open('sender.yml', 'w') as file:
    yaml.dump(data, file)

print("Done!")