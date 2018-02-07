import xml.etree.ElementTree as ET
import csv
import sys


def sanitize(channel, value):
    if(channel == "ts"):
        value = value.split('.')[0]
    return value.replace('.', ',')


def xml_to_csv(xml_file, csv_file):
    ns = {'auth': 'http://rddl.xmlinside.net/PowerMeasurement/data/ion/authenticated/1/'}

    tree = ET.parse(xml_file)
    root = tree.getroot()
    auth_data = (root.find('auth:AuthenticationData', ns))
    device = auth_data.find('auth:Device', ns)
    data_recorder = device.find('auth:DataRecorder', ns)

    header = ['timestamp']
    channels = ['ts']
    for child in data_recorder.find('auth:Channels', ns):
        header.append(child.attrib.get('label'))
        channels.append(child.attrib.get('id'))

    body = []
    for child in data_recorder.find('auth:DataRecords', ns):
        attrs = []
        for channel in channels:
            value = sanitize(channel, (child.attrib.get(channel, '')))
            attrs.append(value)
        body.append(attrs)

    with open(csv_file, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for line in body:
            writer.writerow(line)


files = sys.argv[1:]
for file in files:
    xml_file = file
    csv_file = file.split('.')[0] + '.csv'
    xml_to_csv(xml_file, csv_file)
