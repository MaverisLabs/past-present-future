import csv

with open('list.csv','r') as f:
    csv_file = csv.reader(f,delimiter=",")
    line = 0
    for row in csv_file:
        if line != 0:
            if "naughty" in str(row['???']).lower():
                print(f"[-] NAUGHTY -> {str(row['name'])}")
            line+=1
    print(f"[!] Processed {line} names!")
