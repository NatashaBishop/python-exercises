# Write all content of a given file into a new file, but skip line number 5

# read testOld.txt
with open("testOld.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("testNew.txt", "w") as fp:
    count = 0
    # iterate line by line from a testOld.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # reduce the count every time
        count += 1
