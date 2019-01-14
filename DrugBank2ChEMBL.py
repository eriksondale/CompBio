# Python Script to Convert List of Drug Bank IDs to ChEMBL IDs

# input: .txt file of drug bank IDs
# output: .txt file of ChEMBL IDs
# WARNING: Error in conversion will be output to stdout


import sys;
import requests;

if(len(sys.argv) != 3):
    print("Please enter 1) Input file and 2) Output file")
else:
    print("Processing....")
    success = 0
    totalProcess = 0
    writeFile = open(sys.argv[2],"a")
    with open(sys.argv[1]) as readFile:
        for line in readFile:
            totalProcess = totalProcess + 1
            try:
                line = line.strip('\n')
                url = u'https://www.ebi.ac.uk/unichem/rest/src_compound_id/{}/2/1'.format(line)
                response = requests.get(url)
                if("error" not in response.text):
                    IDout = response.text
                    IDout = IDout.strip()
                    IDout = IDout[IDout.find("CHEM"):IDout.rfind("\"")]
                    writeFile.write(IDout + "\n")
                    success = success + 1

            except Exception as e:
                print("Problem occurred while processing: " + line)
                print(e)
    print(str(success) + " out of " + str(totalProcess) + " IDs properly converted")
