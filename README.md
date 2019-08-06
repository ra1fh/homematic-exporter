HomeMatic CCU2 Prometheus Exporter
==================================

This repository contains a CGI script to be installed on a
[https://www.eq-3.com/products/homematic.html](HomeMatic)
[https://www.eq-3.com/products/homematic/control-units-and-gateways/homematic-central-control-unit-ccu2.html](CCU2)
home automation control unit. It provides a metrics endpoint for
[https://prometheus.io/](Prometheus) for the following devices:

 * [https://www.eq-3.com/products/homematic/heating-and-climate-control/homematic-wireless-radiator-thermostat.html](HomeMatic Wireless Raditor Thermostat)
 * [https://www.eq-3.com/products/homematic/heating-and-climate-control/homematic-wireless-temperature-sensor-outdoor.html](HomeMatic Wireleass Temperature Sensor)
 
For any additional sensor or unit types the script needs to be extended.

Installation and Usage
----------------------

 * Copy prometheus.cgi via to /usr/local/etc/config/addons/www with
   mode 0755, owner root, group root.
 * Access http://you.homematic.ip/addons/prometheus.cgi

This returns metrics in the form:

    # HELP homematic_control_mode Valve control mode.
    # TYPE homematic_control_mode gauge
    homematic_control_mode{dev_address="MEQ1234567", dev_hss_type="HM-CC-RT-DN", dev_name="Kueche"} 1
    # HELP homematic_battery_volts Battery voltage.
    # TYPE homematic_battery_volts gauge
    homematic_battery_volts{dev_address="MEQ1234567", dev_hss_type="HM-CC-RT-DN", dev_name="Kueche"} 2.800000
    # HELP homematic_valve_state Valve state.
    # TYPE homematic_valve_state gauge
    homematic_valve_state{dev_address="MEQ1234567", dev_hss_type="HM-CC-RT-DN", dev_name="Kueche"} 99
    # HELP homematic_temperature_celsius Temperature in celsius.
    # TYPE homematic_temperature_celsius gauge
    homematic_temperature_celsius{dev_address="MEQ1234567", dev_hss_type="HM-CC-RT-DN", dev_name="Kueche"} 25.500000
    # HELP homematic_set_temperature_celsius Set temperature in celsius.
    # TYPE homematic_set_temperature_celsius gauge
    homematic_set_temperature_celsius{dev_address="MEQ1234567", dev_hss_type="HM-CC-RT-DN", dev_name="Kueche"} 30.500000

This has been tested with CCU2 firmware version 2.47.15.

Example Grafana Dashboard
-------------------------

![Grafana Dashboard](/grafana.png)
