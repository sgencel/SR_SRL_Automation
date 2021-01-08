#PYTHON SCRIPTS USING NETMIKO AND PARSER FOR NOKIA SROS ROUTERS
from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import  AuthenticationException
import textfsm
import os

def parse_show_card_manual(args):
    counter_card_number = {}
    counter_card_number_UP = {}
    slot_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','A', 'B']
    for i in args:
        sros = {
        'device_type': 'alcatel_sros',
        'host':   i,
        'username': 'admin',
        'password': 'Alcateldc',
        }
# CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
#PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show card')
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        list = output.split('\n') #split the string with new lines
        for n in list:
            if len(n) == 0:
                continue
            if n[0] in slot_number:
                n = (n.split(' ')) #split to the words using whitespace delimeter
                n = [a for a in n if a != ''] # extract whitespaces
                if n[1] in counter_card_number.keys():  # if key is present in the list, just append the value
                    counter_card_number[n[1]] = counter_card_number[n[1]] +1
                else:
                    counter_card_number[n[1]] = 1  # else create a empty list as value for the key
                if n[3] == 'up' or n[3] == 'up/active':
                    if n[1] in counter_card_number_UP.keys():  # if key is present in the list, just append the value
                        counter_card_number_UP[n[1]] = counter_card_number_UP[n[1]] + 1
                    else:
                        counter_card_number_UP[n[1]] = 1  # else create a empty list as value for the key
        print('HOST IP ADDRESS: ' + i)
        print('CARD NUMBERS')
        print(counter_card_number)
        print('CARD NUMBERS WHICH IS OPERATIONALLY UP')
        print(counter_card_number_UP)
        counter_card_number_UP = {} # Improve with dictionaries dictionary-3 dimensions
        counter_card_number = {} # Improve with dictionaries dictionary-3 dimensions


def parse_show_port(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
        'device_type': 'alcatel_sros',
        'host':   i,
        'username': 'admin',
        'password': 'Alcateldc',
        }
# CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
#PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show port', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)

def parse_show_card(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
        'device_type': 'nokia_sros',
        'host':   i,
        'username': 'admin',
        'password': 'Alcateldc',
        }
# CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
#PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show card', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)

def parse_show_version(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
            'device_type': 'nokia_sros',
            'host': i,
            'username': 'admin',
            'password': 'Alcateldc',
        }
        # CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
            # PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show version', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)


def parse_show_bof(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
            'device_type': 'nokia_sros',
            'host': i,
            'username': 'admin',
            'password': 'Alcateldc',
        }
        # CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
            # PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show bof', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)

def parse_show_router_interface(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
            'device_type': 'nokia_sros',
            'host': i,
            'username': 'admin',
            'password': 'Alcateldc',
        }
        # CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
            # PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show router interface', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)


def parse_show_mda(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
            'device_type': 'nokia_sros',
            'host': i,
            'username': 'admin',
            'password': 'Alcateldc',
        }
        # CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
            # PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show mda', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)

def parse_log99(args):
    all_data = {}
    os.environ['NET_TEXTFSM'] = 'C:\\Users\sgancel\\ntc-templates\\templates'
    for i in args:
        sros = {
            'device_type': 'nokia_sros',
            'host': i,
            'username': 'admin',
            'password': 'Alcateldc',
        }
        # CONNECT TO THE SROS NODE
        try:
            net_connect = ConnectHandler(**sros)
            # PARSE THE CARD INFORMATION FROM THE CLI OUTPUT
            output = net_connect.send_command('show log log-id 99', use_textfsm=True)
        except (AuthenticationException):
            print('Authentication Failure: ' + i)
            continue
        except (NetMikoTimeoutException):
            print('\n' + 'Timeout to device: ' + i)
            continue

        except (SSHException):
            print('SSH might not be enabled: ' + i)
            continue
        except (EOFError):
            print('\n' + 'End of attempting device: ' + i)
            continue
        except unknown_error:
            print('Some other error: ' + str(unknown_error))
            continue
        all_data[i] = output
    return(all_data)

if __name__ == "__main__":
    host_ip = ['172.29.12.90', '172.29.12.75']
    print(parse_log99(host_ip))
