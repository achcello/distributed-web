# Create a script to separate a generic piece of data into chunks.
# Accept data as text or as `bytes` and an integer for how many chunks are needed,
# Return an array of chunks as bytes
import os
import sys

def getfilesize(filename):
    with os.startfile(filename, "rb") as fr:
        if not os.path.isfile(filename):
        print("No such file as: \"%s\"" % filename)
            return
        fr.seek(0, 2)  # move to end of the file
        size = fr.tell() # Returns the current position of the file read/write pointer within the file.
        print("getfilesize: size: %s" % size)
        return fr.tell()


def splitfile(filename, splitsize):
    # Open original file in read only mode
    if not os.path.isfile(filename):
        print("No such file as: \"%s\"" % filename)
        return

    filesize = getfilesize(filename)
    getFile(filename)
    with os.startfile(filename) as fr:
        if not os.path.isfile(filename):
        print("No such file as: \"%s\"" % filename)
            return
        counter = 1
        orginalfilename = filename.split(".")
        readlimit = 5000  # read 5kb at a time
        n_splits = filesize
        print("splitfile: No of splits required: %s" % str(n_splits))
        for i in range(n_splits + 1):
            chunks_count = int(splitsize)
            data_5kb = fr.read(readlimit)  # read
            # Create split files
            print("chunks_count: %d" % chunks_count)
            with open(orginalfilename[0] + "_{id}.".format(id=str(counter)) + orginalfilename[1], "ab") as fw:     
                dictionary += originalfilename
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
     return dictionary


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Filename or splitsize not provided: Usage:     filesplit.py filename splitsizeinkb ")
    else:
        filesize = int(sys.argv[2]) * 1000  # make into kb
        filename = sys.argv[1]
        splitfile(filename, filesize)
        
def getFile(filename):    ### makes a python dictionary.....need to implement
    dictionary = {}
    
    infile = os.startfile(filename)
    line_num = 1
    for line in infile:
        dictionary[line_num] = line
        line_num += 1
    print(dictionary)
    infile.close()

 def split_dictionary(dictionary, chunks):
    # prep with empty dicts
    list = [dict() for idx in xrange(chunks)]
    idx = 0
    for k,v in input_dict.iteritems():
        list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return list
