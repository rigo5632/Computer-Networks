def printAverageSize(average):
    print(f'* Average Size: \t{average}')

def printTopPorts(ports, classification, totalPackets):
    print(f'* {classification} (Port Number - Number of Instances - Percentage of Traffic)')
    for i in range(10):
        percentage = (ports[i][1]/totalPackets)*100
        print(f'\t{ports[i][0]}\t-\t{ports[i][1]}\t-\t{percentage:.2f} %')

def printAddressTraffic(addresses, limit, totalPackets):
    percentage = limit * 100
    limit = int(limit*totalPackets)
    print(f'* {percentage}% Source Address Traffic (Address - (instances: #, number of bytes: #))')
    for i in range(limit):
        print(f'\t{addresses[i][0]}\t-\t{addresses[i][1]}')

