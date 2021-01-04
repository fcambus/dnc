#!/usr/bin/env python3

#
# dnc 0.2.0
# Copyright (c) 2014-2021, Frederic Cambus
# https://github.com/fcambus/dnc
#
# Created: 2014-02-11
# Last Updated: 2021-01-04
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
    x = PrettyTable(hrules=1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "6v")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    header = ["Domain", "NS", "IPv4"]

    for o, a in opts:
        if o == "-6":
            header.append("IPv6")
            getv6 = True
        elif o == "-v":
            print("dnc 0.2.0")
            sys.exit(0)

    x.field_names = header
    x.align = "l"

    for name in args:
        row = [name, query(name, 'NS'), query(name, 'A')]

        if getv6:
            row.append(query(name, 'AAAA'))

        x.add_row(row)

    print(x)


if __name__ == "__main__":
    main()
