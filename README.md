# dnc

## Description

dnc (Domain Name Checker), is a CLI tool to check domain names configuration.

## Requirements

dnc requires Python 3.5+ and the following Python modules:

- Dnspython
- PrettyTable
- pyOpenSSL

## Installation

## Usage

## Example

Here is the output of running dnc querying NS and A records, along with
SSL certificate expiration date for one domain:

	+------------+--------------------------+---------------+------------+
	| Domain     | NS                       | IPv4          | TLS        |
	+------------+--------------------------+---------------+------------+
	| cambus.net | oxygen.ns.hetzner.com.   | 116.203.5.115 | 2021-02-26 |
	|            | hydrogen.ns.hetzner.com. |               |            |
	|            | helium.ns.hetzner.de.    |               |            |
	+------------+--------------------------+---------------+------------+

## License

dnc is released under the BSD 2-Clause license. See `LICENSE` file for details.

## Author

dnc is developed by Frederic Cambus.

- Site: https://www.cambus.net
