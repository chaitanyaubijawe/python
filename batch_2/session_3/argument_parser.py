import argparse
from file_handling import *

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fetchIp", action="store_true", help="provide ip here...." )
parser.add_argument("-r","--fetchRam", action="store_true", help="list u ram here....")

args = parser.parse_args()

print((args))

fetchIPs = args.fetchIp
fetchRam = args.fetchRam


if fetchIPs:
    # do cloud serach/gather fact....
    servers = read_csv("a.csv", ",")
    ipList = []

    for server in servers:

        ipList.append(server.server_ip)
        print(server.server_ip)

if fetchRam:
    # do cloud serach/gather fact....
    servers = read_csv("a.csv", ",")
    ipList = []

    for server in servers:

        ipList.append(server.server_ip)
        print(server.ram)
