#!/bin/tclsh

load tclrega.so
source [file join $env(DOCUMENT_ROOT) once.tcl]
source [file join $env(DOCUMENT_ROOT) cgi.tcl]

cgi_eval {
    cgi_input
    cgi_content_type "text/plain; charset=iso-8859-1; version=0.0.4"

    set list ""
    catch { import list }

    array set res [rega_script {

string s_device;
object o_device;

string s_channel;
object o_channel;

string s_dp;
object o_dp;

string metric_list = "";

foreach(s_device, dom.GetObject(ID_DEVICES).EnumUsedIDs()) {
    var o_device = dom.GetObject(s_device);
    if ((o_device.Address() != "BidCoS-Wir") && (o_device.Address() != "BidCoS-RF")) {
        ! WriteLine(o_device.Address() # "# " # o_device.HssType() # " (" # o_device.Name() # ")");

        foreach(s_channel, o_device.Channels().EnumUsedIDs()) {
            o_channel = dom.GetObject(s_channel);

            foreach (s_dp, o_channel.DPs().EnumUsedIDs()) {
                o_dp = dom.GetObject(s_dp);

                integer val_tp = o_dp.ValueType();
                string val_str;

                if (val_tp == 2) {
                    if (o_dp.Value()) {
                        val_str = "1";
                    } else {
                        val_str = "0";
                    }
                } else {
                    val_str = o_dp.Value().ToString();
                }

                if (val_str.Length() > 0) {
					var d_h = o_device.HssType();
					var d_a = o_device.Address();
					var d_n = o_device.Name();
					var d_hss = o_dp.HssType();
					string metric_name = "";
					string metric_help = "";
					string metric_type = "gauge";

					if (d_h == "HM-CC-RT-DN") {
						if (d_hss == "ACTUAL_TEMPERATURE") {
							metric_name = "homematic_temperature_celsius";
							metric_help = "Temperature in celsius.";
						} elseif (d_hss == "SET_TEMPERATURE") {
							metric_name = "homematic_set_temperature_celsius";	
							metric_help = "Set temperature in celsius.";
						} elseif (d_hss == "BATTERY_STATE") {
							metric_name = "homematic_battery_volts";
							metric_help = "Battery voltage.";
						} elseif (d_hss == "CONTROL_MODE") {
							metric_name = "homematic_control_mode";
							metric_help = "Valve control mode.";
						} elseif (d_hss == "AUTO_MODE") {
							metric_name = "homematic_auto_mode";
							metric_help = "Valve auto mode.";
						} elseif (d_hss == "BOOST_MODE") {
							metric_name = "homematic_boost_mode";
							metric_help = "Valve boost mode.";
						} elseif (d_hss == "COMFORT_MODE") {
							metric_name = "homematic_comfort_mode";
							metric_help = "Valve comfort mode.";
						} elseif (d_hss == "LOWERING_MODE") {
							metric_name = "homematic_lowering_mode";
							metric_help = "Valve lowering mode.";
						} elseif (d_hss == "BOOST_STATE") {
							metric_name = "homematic_boost_state";
							metric_help = "Valve boost state.";
						} elseif (d_hss == "VALVE_STATE") {
							metric_name = "homematic_valve_state";
							metric_help = "Valve state.";
						}
					} elseif (d_h == "HM-WDS30-T-O") {
						if (d_hss == "TEMPERATURE") {
							metric_name = "homematic_temperature_celsius";
							metric_help = "Temperature in celsius.";
						}
					} elseif (d_h == "HM-WDS40-TH-I-2") {
						if (d_hss == "TEMPERATURE") {
							metric_name = "homematic_temperature_celsius";
							metric_help = "Temperature in celsius.";
						} elseif (d_hss == "HUMIDITY") {
							metric_name = "homematic_humidity_percent";
							metric_help = "Humidity in percent.";
						}
					}
				
					if (metric_name.Length() > 0) {
						if (metric_list.Find(metric_name) == -1) {
							metric_list = metric_list # "\t" # metric_name;
							WriteLine("# HELP " # metric_name # " " # metric_help)
							WriteLine("# TYPE " # metric_name # " " # metric_type)
						}
						WriteLine(metric_name # "{"
                        #     "dev_address=\"" # d_a
                        # "\", dev_hss_type=\"" # d_h
                        # "\", dev_name=\"" # d_n
                        # "\"} " # val_str )
					} elseif (0) {
						WriteLine("# UNKNOWN " # metric_name # "{"
                        #     "dev_address=\"" # d_a
                        # "\", dev_hss_type=\"" # d_h
                        # "\", dev_hss=\"" # d_hss
                        # "\", dev_name=\"" # d_n
                        # "\"} " # val_str )
                        		}
                }
            }
        }
    }
}


    }]
    set response [string map {\r\n \n} $res(STDOUT)]
    puts $response
}

