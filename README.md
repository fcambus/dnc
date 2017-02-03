# dnc

## Description

dnc (Domain Name Checker), is a CLI tool to check domain names configuration and statistics. 
  

## Installation

Install the program:

	npm install -g dnc

## Usage

	dnc [domain ...]

If no domains are specified as command line arguments, dnc will attempt to read its configuration file.

## Configuration

Configuration options are set in the `~/.dnc` file. If dnc cannot find an user defined configuration file in the home directory, the bundled `config.json` if used instead.

Example configuration with two domains:

	{
	    "domains": [
	        "cambus.net",
	        "echojs.com"
	    ]
	}

## Example

Here is the output of running dnc with the default configuration file:

![dnc Screenshot](http://www.cambus.net/content/2014/02/dnc.png)

## License

dnc is released under the BSD 2-Clause license. See `LICENSE` file for details.

## Author

dnc is developed by Frederic Cambus.

- Site : http://www.cambus.net
- Twitter: http://twitter.com/fcambus
