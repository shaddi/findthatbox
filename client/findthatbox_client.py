import yaml

import netifaces
import requests
import snowflake

with open("/etc/findthatbox.conf") as conf_file:
    conf = yaml.load("".join(conf_file.readlines()))

def get_private_ips():
    ifaces = netifaces.interfaces()
    inet_ifaces = [netifaces.ifaddresses(i)[netifaces.AF_INET]
                   for i in netifaces.interfaces()
                   if netifaces.AF_INET in netifaces.ifaddresses(i)]
    ips = []
    for i in inet_ifaces:
        for j in i:
            if not j['addr'].startswith("127"):
                ips.append(j['addr'])
    return ips


"""
Perform a checkin. Will send the machine's unique ID plus any additional data specified.
"""
def checkin(server=conf['server'], data={}):
    private_ips = str(get_private_ips())
    data['private_ip'] = private_ips
    url = server + "/checkin/%s" % snowflake.snowflake()
    print url
    return requests.get(url, params=data)

if __name__ == "__main__":
    checkin()
