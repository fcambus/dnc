# dnc

## Description

dnc (Domain Name Checker), is a CLI tool to check domain names configuration.

## Requirements

dnc requires Python 3.5+ and the following Python modules:

- Dnspython
- PrettyTable
- pyOpenSSL

## Usage

	dnc [-hv] domain

The options are as follows:

	-4	Resolve and display A records (IPv4 addresses).
	-6	Resolve and display AAAA records (IPv6 addresses).
	-h	Display usage.
	-m	Resolve and display MX records (Mail Exchange).
	-n	Resolve and display NS records (Name Servers).
	-s	Display SSL/TLS certificate expiration date.
	-v	Display version.

## Example

Here is the output of running dnc querying NS and A records, along with
SSL certificate expiration date for one domain:

	$ dnc -n4s cambus.net
	+------------+--------------------------+---------------+------------+
	| Domain     | NS                       | IPv4          | TLS        |
	+------------+--------------------------+---------------+------------+
	| cambus.net | oxygen.ns.hetzner.com.   | 116.203.5.115 | 2021-04-23 |
	|            | hydrogen.ns.hetzner.com. |               |            |
	|            | helium.ns.hetzner.de.    |               |            |
	+------------+--------------------------+---------------+------------+

## License

dnc is released under the BSD 2-Clause license. See `LICENSE` file for details.

## Author

dnc is developed by Frederic Cambus.

- Site: https://www.cambus.net
