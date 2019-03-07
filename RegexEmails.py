'''
RegexEmails.py
---------------------------------
Bradley Jones
March 23, 2017
email:          bjones@dogwoodgeo.com
Description:    Uses Regex to parse emails saved as text files and write desired info to csv file.
'''

import os
import csv
import re
from datetime import datetime

i = datetime.now()
date = i.strftime("%Y%m%d")

msgDirectory = r"\\PATH\TO\MESSAGES\SAVED\AS\TXT\messages"
messages = []


for mail in os.listdir(msgDirectory):
    messages.append(mail)
    print(mail)
print("Number of OneCall messages: " + str(len(messages)))
print(messages)

rowCount = 0
with open("OneCall-" + date + ".csv", "wb") as f:
    header = ["DATE", "TICKET NUMBER", "OLD TICKET NUM", "STREET #", "STREET NAME", "INTERSECTING STREET", ""]
    w = csv.writer(f)
    w.writerow(header)

    for message in messages:
        filePath = msgDirectory + "\\" + message
        lines = []
        cells = []

        # Open emails in messages list and iterate through lines looking for desired text. 
        with open(filePath, "r") as fr:
            dateCount = 0
            for string in fr:

                date = re.findall(r'\d{2}/\d{2}/\d{2}', string)
                if date:
                    print('Found date on line ' + str(dateCount))
                    print(date)
                    lines.append(date[0])
                    print(lines)
                    break

                else:
                    print('Date not found')
                dateCount += 1

            newCount = 0
            for string in fr:
                print(string)
                newTicket = re.findall(r'TICKET NUMBER--\[\d{6}-\d{4}\]', string)
                if newTicket:
                    print('Found new ticket number on line ' + str(newCount))
                    print(newTicket)
                    lines.append(newTicket[0])
                    print(lines)
                    break
                else:
                    print('New ticket number not found')
                newCount += 1

            oldCount = 0
            for string in fr:
                print(string)
                oldTicket = re.findall(r'OLD TICKET NUM-\[\d{6}-\d{4}\]', string)
                if newTicket:
                    print('Found old ticket number on line ' + str(oldCount))
                    print(oldTicket)
                    if len(oldTicket) > 0:
                        lines.append(oldTicket[0])
                    print(lines)
                    break
                else:
                    print('Old ticket number not found')
                oldCount += 1








                # emergency = re.search('EMERGENCY', line)

        #         lines.append(line.replace("\n", "").replace("\t", " "))
        # newLines = []
        # for line in lines:
        #     if line == 'Importance: High':
        #         newLines.append(lines[7])
        #         newLines.append(lines[11])
        #         newLines.append(lines[28])
        #         newLines.append(lines[29])
        #     elif line == 'Importance: Low':
        #         newLines.append(lines[11])
        #         newLines.append(lines[12])
        #         newLines.append(lines[29])
        #         newLines.append(lines[30])
        #     # elif line == '':
        #     #     pass
        #     # else:
        #     #     newLines.append(line)
        # print("newLines:")
        # print(newLines)
        # print("**************************************")

#         cells = []
#         addressList = lines[27].split('   ')
#         address = addressList[0][10:-1]
#         street = addressList[1].replace("STREET--[", "").replace("][", " ").replace("]", "")
#
#         newTicket = lines[9][16:27]
#         day = newTicket[4:6]
#         month = newTicket[2:4]
#         year = newTicket[0:2]
#         date = month + "/" + day + "/" + year
#         oldTicket = lines[10][17:-1]
#         intersect = lines[28][29:-1]
#         status = lines[0]
#
#         cells.append(date)
#         cells.append(newTicket)
#         cells.append(oldTicket)
#         cells.append(address)
#         cells.append(street.strip())
#         cells.append(intersect)
#         cells.append(status)
#         print(cells)
#
#         w.writerow(cells)
#         rowCount += 1
#
# print("Rows written to csv file: " + str(rowCount))
# if rowCount != len(messages):
#     print("WARNING: Number of rows written to csv does not equal number of OneCall email messages\n" +
#           "A message may have been missed or duplicated. Compare rows in csv to messages to determine error.")









