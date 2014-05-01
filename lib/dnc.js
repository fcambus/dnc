/*****************************************************************************/
/*                                                                           */
/* dnc 0.1.2 (c) by Frederic Cambus 2014                                     */
/* https://github.com/fcambus/dnc                                            */
/*                                                                           */
/* Created: 2014/02/11                                                       */
/* Last Updated: 2014/05/01                                                  */
/*                                                                           */
/* dnc is released under the BSD 2-Clause license.                           */
/* See LICENSE file for details.                                             */
/*                                                                           */
/*****************************************************************************/

var dns = require('dns');



/**[ NPM Modules ]************************************************************/

var async = require('async');
var alexa = require('alexarank');

var Intl = require('intl');
var Table = require('cli-table');



/**[ dnc ]********************************************************************/

module.exports = function(config) {

    var table = new Table({
        head: ['Domain', 'NS', 'IPv4', 'IPv6', 'Alexa']
    });

    async.forEach(config.domains, function(domain, callback) {

        var site = {
            ns: '',
            ipv4: '',
            ipv6: '',
            alexa: ''
        };

        async.series([

            /**[ Get Alexa Traffic Rank ]*************************************/

            function(callback) {
                alexa(domain, function(error, result) {
                    if (!error && result.rank) {
                        site.alexa = new Intl.NumberFormat().format(result.rank);
                    }

                    callback();
                });
            },

            /**[ Get Name Servers ]*******************************************/

            function(callback) {
                dns.resolveNs(domain, function(error, addresses) {
                    if (!error) {
                        for (var item in addresses) {
                            site.ns += addresses[item] + "\n";
                        }
                    }

                    callback();
                });
            },

            /**[ Get A records ]**********************************************/

            function(callback) {
                dns.resolve4(domain, function(error, addresses) {
                    if (!error) {
                        for (var item in addresses) {
                            site.ipv4 += addresses[item] + "\n";
                        }
                    }

                    callback();
                });
            },

            /**[ Get AAAA records ]*******************************************/

            function(callback) {
                dns.resolve6(domain, function(error, addresses) {
                    if (!error) {
                        for (var item in addresses) {
                            site.ipv6 += addresses[item] + "\n";
                        }
                    }

                    callback();
                });
            }
        ], function(error) {

            /**[ Populate table ]*********************************************/

            table.push(
                [domain, site.ns.trim(), site.ipv4.trim(), site.ipv6.trim(), site.alexa]
            );

            callback();
        });

    }, function(error) {

        /**[ Sort and display table ]*****************************************/

        table.sort(function(a, b) {
            if (a[0] < b[0]) return -1;
            if (a[0] > b[0]) return 1;
            return 0;
        });

        console.log(table.toString());
    });
};
