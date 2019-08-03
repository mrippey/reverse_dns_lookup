#!/usr/bin/python

import sys
import dns.resolver
from ipwhois import IPWhois
import pprint

if len(sys.argv) < 2:
    print(sys.argv[0] + ": <ip_addr>")
    sys.exit(1)

try:
    rev_name = dns.reversename.from_address(sys.argv[1])
    reversed_dns = str(dns.resolver.query(rev_name, "PTR")[0])
    print(reversed_dns)
except:
    print("Reverse Address Not Found!")
    pass

print("\n---------------------------")
whois = IPWhois(sys.argv[1])
whois_info = whois.lookup_whois()

if whois_info:
    pprint.pprint(whois_info)
else:
print("No WhoIs data found")
