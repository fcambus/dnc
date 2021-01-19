#!/usr/bin/env python3

#
# dnc 0.2.0
# Copyright (c) 2014-2021, Frederic Cambus
# https://github.com/fcambus/dnc
#
# Created: 2014-02-11
# Last Updated: 2021-01-19
#
# dnc is released under the BSD 2-Clause license.
# See LICENSE file for details.
#

import getopt
import socket
import ssl
import sys
import OpenSSL
import dns.resolver
from datetime import datetime
from prettytable import PrettyTable

socket.setdefaulttimeout(1)

def query(domain: str, rrtype: str) -> str:
    try:
        answers = dns.resolver.resolve(domain, rrtype)
    except:
        return ''

    return '\n'.join([rdata.to_text() for rdata in answers])


def tls(domain: str, _: str) -> str:
    try:
        cert = ssl.get_server_certificate((domain, 443))
    except socket.timeout:
        return "No TLS"

    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    return datetime.strptime(
        x509.get_notAfter().decode("ascii"), "%Y%m%d%H%M%SZ"
    ).strftime("%Y-%m-%d")


def main():
    getv6 = False
    results = PrettyTable(hrules=1)

    try:
        options, args = getopt.getopt(sys.argv[1:], "6v")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    header = ["Domain", "NS", "IPv4"]

    for option, arg in options:
        if option == "-6":
            header.append("IPv6")
            getv6 = True
        elif option == "-v":
            print("dnc 0.2.0")
            sys.exit(0)

    results.field_names = header
    results.align = "l"

    for name in args:
        row = [name, query(name, 'NS'), query(name, 'A')]

        if getv6:
            row.append(query(name, 'AAAA'))

        results.add_row(row)

    print(results)


if __name__ == "__main__":
    main()
