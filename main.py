#!/usr/bin/env python3

if __name__ == "__main__":
    with open("times.txt", "r") as f:
        data = f.readlines()

    newData = "".join(d for d in data) + "\n----- OUTPUT -----\n\n"
    skipped = ""

    for d in data:
        if "OUTPUT" in d:
            break

        if len(d) > 0:
            d = d[:-1] # remove \n
            if not "none" in d.lower():
                d = d.replace(".", ",")
                if not ":" in d:
                    d = "00:00:" + d
                else:
                    if len(d.split(":")[0]) == 1:
                        d = "0" + d
                    if d.count(":") == 1:
                        d = "00:" + d
                if len(d.split(",")[-1]) == 1:
                        d += "0"
                newData += d + "\n"
            else:
                newData += "\n"
                skipped += f"SKIPPED ENTRY: {d}\n"

    with open("times.txt", "w") as f:
        f.write(newData)
