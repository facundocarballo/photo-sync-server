import socket
import netifaces
from Requests.status import SUCCESS, NOT_FOUND

def get_local_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        iface_data = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in iface_data:
            for info in iface_data[netifaces.AF_INET]:
                if not info.get('addr', '').startswith('127.') and not info.get('addr', '').startswith('169.254'):
                    return info['addr'], SUCCESS
    return None, NOT_FOUND