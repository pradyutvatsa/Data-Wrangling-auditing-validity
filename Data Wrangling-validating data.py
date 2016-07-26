
# coding: utf-8

# In[1]:

import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        reader_lst = list(reader)
        #COMPLETE THIS FUNCTION
        
    for line in reader_lst[:]:
        if "dbpedia.org" not in line['URI']:
            reader_lst.remove(line)
            
    good_lst = []
    bad_lst = []
    data_re = re.compile('(?=1)(?=18)((188[6-9]|189[0-9]))|(?=19)(19[0-9][0-9])|(?=200)(200[0-9])|(201[0-4])')
    #print data_re
    for line in reader_lst[:]:
        #print line['productionStartYear']
        mObj = data_re.search(line['productionStartYear'])
        #print mObj
        if mObj:
            for i in range(1,6):
                if isinstance(mObj.group(i), str):
                    #print 'mObj.group(i) is', mObj.group(i)
                    line['productionStartYear'] = mObj.group(i)
                    good_lst.append(line)
                    break
        else:
            bad_lst.append(line)



    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in good_lst:
            writer.writerow(row)
            
    with open(output_bad, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in bad_lst :
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()


# In[ ]:



