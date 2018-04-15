# Create a script to separate a generic piece of data into chunks.
# Accept data as text or as `bytes` and an integer for how many chunks are needed,
# Return an array of chunks as bytes
import os
import sys

dictionary = {}


def getfilesize(filename):
    with open(filename, "rb") as fr:
        fr.seek(0, 2)  # move to end of the file
        size = fr.tell()
        print("getfilesize: size: %s" % size)
        return fr.tell()


def splitfile(dictionary, splitsize):
    # Open original file in read only mode
    if not os.path.isfile(dictionary):
        print("No such file as: \"%s\"" % dictionary)
        return

    filesize = getfilesize(dictionary)
    with open(dictionary, "rb") as fr:
        counter = 1
        orginalfilename = dictionary.split(".")
        readlimit = 5000  # read 5kb at a time
        n_splits = filesize
        print("splitfile: No of splits required: %s" % str(n_splits))
        for i in range(n_splits + 1):
            chunks_count = int(splitsize)
            data_5kb = fr.read(readlimit)  # read
            # Create split files
            print("chunks_count: %d" % chunks_count)
            with open(orginalfilename[0] + "_{id}.".format(id=str(counter)) + orginalfilename[1], "ab") as fw:
                fw.seek(0)
                fw.truncate()  # truncate original if present
                while data_5kb:
                    fw.write(data_5kb)
                    if chunks_count:
                        chunks_count -= 1
                        data_5kb = fr.read(readlimit)
                    else:
                        break
            counter += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Filename or splitsize not provided: Usage:     filesplit.py filename splitsizeinkb ")
    else:
        filesize = int(sys.argv[2]) * 1000  # make into kb
        filename = sys.argv[1]
        splitfile(getDictionary(), filesize)
        
def getFile():    ### makes a python dictionary.....need to implement
    prose = str(input('Please enter the file path for your text file: '))

    dictionary = {}
    
    infile = open(prose, 'r')
    line_num = 1
    for line in infile:
        dictionary[line_num] = line
        line_num += 1
    print(dictionary)
    infile.close()

def getDictionary():
    return dictionary
