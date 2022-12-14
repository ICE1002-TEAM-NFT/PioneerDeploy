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
            if line[1] == number:
                line[2] = info
                line[3] = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            lines.append(line)

        
        f = open("data.csv", "w", newline="")
        wr = csv.writer(f)
        wr.writerows(lines)
        f.close()

        f = open("data.txt", 'a')
        now = datetime.datetime.now()
        now_string = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")
        f.writelines(tmp+now_string+" "+"\n")
        f.close()

        return 1

#This is for test fun.py
csv_make()
csv_add("435, Using")