import xml.etree.ElementTree as ET
from ncclient import manager
import logging
import sys
import xmltodict
import time
def parse_port_stats(args):
    all_data = {}
    port_stats = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <port>

                    <statistics/>
            </port>
          </state>
    '''



    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", port_stats))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['port']
            all_data[host] = mydict_only_port

    return(all_data)


def parse_cpm_cpu_number(args):
    all_data = {}
    cpu_num = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <cpm>

                    <number-of-cpus/>
            </cpm>
          </state>
    '''



    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", cpu_num))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['cpm']
            all_data[host] = mydict_only_port

    return(all_data)




def parse_card_state(args):
    all_data = {}
    card_state = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <card>
                    <equipped-type/>
                    <hardware-data>
                        <oper-state/>                        
                    </hardware-data>
            </card>
          </state>
    '''

    cli = ''' <oper-data-format-cli-block>
            <cli-show>card</cli-show>
          </oper-data-format-cli-block>
    '''

    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", card_state))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['card']
            all_data[host] = mydict_only_port

    return(all_data)

def parse_card_errors(args):
    all_data = {}
    card_errors = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <card>
            <fp>
            <statistics></statistics>
            </fp>
            </card>
          </state>
    '''


    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", card_errors))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['card']
            all_data[host] = mydict_only_port

    return(all_data)



def parse_ipv4_unicast_stats(args):
    all_data = {}
    ipv4_unicast = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <router>
            <route-table>
            <unicast>
            <ipv4>
            <statistics>
            </statistics>
            </ipv4>
            </unicast>
            </route-table>
            </router>
          </state>
    '''


    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", ipv4_unicast))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['router']
            all_data[host] = mydict_only_port

    return(all_data)


def parse_system_connections(args):
    all_data = {}
    system_connections = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <system>
            <connections>
            <statistics>
            </statistics>
            </connections>
            </system>
          </state>
    '''


    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", system_connections))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['system']
            all_data[host] = mydict_only_port

    return(all_data)


def parse_bgp_info(args):
    all_data = []
    bgp_info = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <router>
                    <bgp>
                    <neighbor>
                    <ip-address/>
                    <statistics>
                    <session-state/>
                    </statistics>
                    </neighbor>
                    </bgp>
            </router>
          </state>
    '''

    cli = ''' <oper-data-format-cli-block>
            <cli-show>card</cli-show>
          </oper-data-format-cli-block>
    '''

    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", bgp_info))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_data = mydict['rpc-reply']['data']['state']['router']
            mydict_only_data["host"] = host
            all_data.append(mydict_only_data)
    return(all_data[1])

def parse_port_error_last_1min(args):
    all_data_initial = {}
    all_data_second_iteration = {}
    m=0
    error_data = {}
    port_stats = ''' <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <port>

                    <statistics/>
            </port>
          </state>
    '''



    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", port_stats))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['port']
            all_data_initial[host] = mydict_only_port
    print('sleeping 1 min')
    time.sleep(60)
    print('1min is over')
    for host in args:
        with manager.connect(host=host, port=830,
                     username="admin", hostkey_verify=False, password="Alcateldc",
                     device_params={'name': 'alu'}) as m:
            get_reply = m.get(("subtree", port_stats))
            mydict = xmltodict.parse(str(get_reply),dict_constructor=dict)
            mydict_only_port = mydict['rpc-reply']['data']['state']['port']
            all_data_second_iteration[host] = mydict_only_port
# Report and create Dic, if there are additional error/discard packets discovered (Increasing error/discard packets over time)
    for host in args:
        port_list = []
        n = 0
        for per_port in all_data_second_iteration[host]:
            port_list.append({'port-id':per_port['port-id']})
            if (int(per_port['statistics']['in-discards']) - int(all_data_initial[host][n]['statistics']['in-discards'])) >0:
                port_list[n].update({'in-discards':(int(per_port['statistics']['in-discards']) - int(all_data_initial[host][n]['statistics']['in-discards']))})
            if (int(per_port['statistics']['in-errors']) - int(all_data_initial[host][n]['statistics']['in-errors'])) > 0:
                port_list[n].update({'in-errors':(int(per_port['statistics']['in-errors']) - int(all_data_initial[host][n]['statistics']['in-errors']))})
            if (int(per_port['statistics']['in-unknown-protocol-discards']) - int(all_data_initial[host][n]['statistics']['in-unknown-protocol-discards'])) >0:
                port_list[n].update({'in-unknown-protocol-discards': (int(per_port['statistics']['in-unknown-protocol-discards']) - int(all_data_initial[host][n]['statistics']['in-unknown-protocol-discards']))})
            if (int(per_port['statistics']['out-discards']) - int(all_data_initial[host][n]['statistics']['out-discards'])) >0 :
                port_list[n].update({'out-discards': (int(per_port['statistics']['out-discards']) - int(all_data_initial[host][n]['statistics']['out-discards']))})
            if (int(per_port['statistics']['out-errors']) - int(all_data_initial[host][n]['statistics']['out-errors'])) >0:
                port_list[n].update({'out-errors': (int(per_port['statistics']['out-errors']) - int(all_data_initial[host][n]['statistics']['out-errors']))})
            n=n+1
        error_data[host] =port_list
    return (error_data)
if __name__ == "__main__":
    host_ip = ['172.29.12.75', '172.29.12.90']
    print(parse_bgp_info(host_ip))



