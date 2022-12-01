import datetime
import csv
import pandas as pd

class class_room:
    pass

def csv_make():
    class_room = [307, 435, 522, 534]
    class_info = ["Empty", "Empty", "Empty", "Empty"]
    used_time = [0, 0, 0, 0]

    df = pd.DataFrame(class_room, columns = ['class_room'])
    df["class_info"] = class_info
    df["used_time"] = used_time

    return df.to_csv("data.csv")

def csv_add(tmp):
        number = tmp[0:3]
        info = tmp[4:10]
        
        
        f = open("data.csv", "r")
        rdr = csv.reader(f)
        lines = []
        for line in rdr:
            # print(line)
            if line[1] == number:
                # print(1)
                line[2] = info
                line[3] = datetime.datetime.now()
            lines.append(line)

        
        f = open("data.csv", "w", newline="")
        wr = csv.writer(f)
        wr.writerows(lines)

        f.close()
        return 1

#This is for test fun.py
csv_make()
csv_add("435, Using")