#!/usr/bin/env python3

#
# dnc 0.2.0
# Copyright (c) 2014-2021, Frederic Cambus
# https://github.com/fcambus/dnc
#
# Created: 2014-02-11
# Last Updated: 2021-01-17
#
# dnc is released under the BSD 2-Clause license.
# See LICENSE file for details.
#

import getopt
import sys
import dns.resolver
from prettytable import PrettyTable


def query(domain, rrtype):
    try:
        answers = dns.resolver.resolve(domain, rrtype)
    except:
        return ''

    return '\n'.join([rdata.to_text() for rdata in answers])


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
