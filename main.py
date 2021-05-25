fname = input("Enter file name: ") # Test: mbox-short.txt
fh = open(fname)
counter = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Find float of interest, and sum
    index = line.find("0")
    line = float(line[index:])
    add += line
    counter += 1
print("Average spam confidence: " + str(add / counter))
