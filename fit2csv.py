# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:12:19 2019
@author: SALMAN
salmah2@unlv.nevada.edu

place this script in a folder with fit files 
this script will convert .fit -> .csv
"""

from fitparse import FitFile
import re
import csv
import glob
for filename in glob.glob('*.fit'):
    fitfile = FitFile(filename)
    z = []
    headers = []
    for record in fitfile.get_messages('record'):
        x = []
        y = []
        for record_data in record:
            if(record_data.name == "timestamp"):
                datetime =  re.findall('\d+', str(record_data.value) )
                y.append('year')
                y.append('month')
                y.append('day')
                y.append('hour')
                y.append('min')
                y.append('sec')
                for split in datetime:
                    x.append(split)
            else:
                x.append(record_data.value)
                y.append(record_data.name)
        z.append(x)
        headers = y
    print z
    with open(filename+'.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(z)
