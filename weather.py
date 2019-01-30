import xmltodict
import argparse
import json
import os

def xmltojson(inputFile, outputFile):
    try:
        rawXML = open(inputFile, "r").read()
    except:
        print("Error: Can't open file '{:s}'.".format(inputFile))
        return
    weather = xmltodict.parse(rawXML, attr_prefix='')

    if os.path.isfile(outputFile):
        print("File '{:s}' already exist. Do you want to replace?".format(outputFile))
        options = input("(Y/N) > ")
        if options.upper() == "Y":
            json.dump(weather, open(outputFile, "w"), indent=4)
        else:
            return
    print("Convert success!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Covert XML file to json file.')
    parser.add_argument("input", help="Path of XML file.")
    parser.add_argument("output", help="Destination filename of json file.")
    args = parser.parse_args()

    xmltojson(args.input, args.output)
