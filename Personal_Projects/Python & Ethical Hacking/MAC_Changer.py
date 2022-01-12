import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address')
    parser.add_option('-m', '--mac', dest='new_MAC', help='New MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC. Use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'ether', 'hw', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


option = get_arguments()
change_mac(option.interface, option.new_mac)
