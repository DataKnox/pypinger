import subprocess
import ipaddress
from subprocess import Popen, PIPE, DEVNULL
import platform
import argparse


def pyping(subnet=None, count=5, printer="True"):
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subnet', type=str,
                        dest="subnet", help='Provide subnet or host.')
    parser.add_argument('-c', '--count', type=int,
                        dest="count", help='Provide ping count.')
    parser.add_argument('-p', '--printer', type=str,
                        dest="printer", help='Print output? True|False')
    args = parser.parse_args()
    if args.subnet:
        subnet = args.subnet
    elif not subnet:
        subnet = input("Please enter the network: ")
    if args.count:
        count = args.count
    elif not count:
        count = 5
    if args.printer:
        if (args.printer.title() == "True") or (args.printer.title() == "False"):
            temp_print = args.printer.title()
            if temp_print == "False":
                suppress_output = True
            else:
                suppress_output = False
        else:
            print("Incorrect printer argument. Defaulting to True")
            suppress_output = True
    elif printer:
        if (printer.title() == "True") or (printer.title() == "False"):
            temp_print = printer.title()
            if temp_print == "False":
                suppress_output = True
            else:
                suppress_output = False
        else:
            print("Incorrect printer argument. Defaulting to True")
            suppress_output = True

    elif not count:
        count = 5
    count = str(count)
    toping = {}
    alive_hosts = []

    current_os = platform.system().lower()
    # print(current_os)

    network = ipaddress.ip_network(subnet)

    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    for i in network.hosts():
        i = str(i)
        toping[i] = subprocess.Popen(
            ['ping', parameter, '5', '-i', '0.2', i], stdout=DEVNULL)
    while toping:
        for i, proc in toping.items():
            if proc.poll() is not None:
                del toping[i]
                hostalive = proc.returncode
                if hostalive == 0:
                    alive_hosts.append(i)
                    if not suppress_output:
                        print(i, ': !!!!!')
                else:
                    if not suppress_output:
                        print(i, ': .....')
                break
    return alive_hosts


if __name__ == "__main__":
    pyping()
