#!/usr/bin/env python3

from time import time

if __name__ == "__main__":
    startTime = time()
    print("Welcome! I am reading your times...")

    # start by opening the file containing the times from livesplit
    with open("times.txt", "r") as file:
        fileLines = file.readlines()

    # start the new file data
    newData = "".join(curLine for curLine in fileLines) + "\n----- OUTPUT -----\n\n```\n"
    outputData = ""

    # skipped splits
    skipped = ""

    print("Now I'm going to process them...")
    for i, curLine in enumerate(fileLines, 1):
        # stop processing if the file is read again
        if "OUTPUT" in curLine:
            break

        # ignore empty lines and lines that are newlines
        if len(curLine) > 0 and curLine != "\n":
            # remove the trailing newline char
            curLine = curLine[:-1]

            # if this isn't a skipped split
            # replace the dot of the milliseconds by a comma
            # and add the necessary prefixes
            if not "none" in curLine.lower():
                curLine = curLine.replace(".", ",")
                if not ":" in curLine:
                    curLine = "00:00:" + curLine
                else:
                    if len(curLine.split(":")[0]) == 1:
                        curLine = "0" + curLine
                    if curLine.count(":") == 1:
                        curLine = "00:" + curLine
                if len(curLine.split(",")[-1]) == 1:
                        curLine += "0"
                outputData += curLine + "\n"
            else:
                # append the skipped entries
                outputData += "\n"
                skipped += f"Skipped Entry at line {i}: {curLine}\n"

    # complete the new file data and write it
    newData += outputData + "```\n\n" + skipped
    with open("times.txt", "w") as file:
        file.write(newData)

    print(f"Done in {time() - startTime:.2f}s!\n")
    print("You can find my work inside times.txt, alternatively:")
    print("```\n" + outputData + "\n```")

    print("\nPress enter to continue...")
    input()  # trick to avoid the console closing on its own
