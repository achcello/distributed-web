#Create a script to separate a generic piece of data into chunks.
# Accept data as text or as `bytes` and an integer for how many chunks are needed,
# Return an array of chunks as bytes

def split_page(data, num_of_chunks):

    #Loops at least once
    entry = True
    while entry:
        #Array that will hold the chunks of data
        divided_array = []
        # As long as the length of the array is smaller than the amount of chunks needed, keep trying to add more in
        while len(divided_array) < num_of_chunks:
            try:
                entry = data.next()
            except StopIteration:
                entry = None
            if entry is None:
                # End of file
                break
            divided_array.append(entry)
        if divided_array:
            #Returns entire array
            yield divided_array


# how to convert string to a byte array
def string_to_byte():
    # b = mystring.encode()
    #s = "ABCD"
    # b = bytearray()
    # b.extend(map(ord, s))
    data = ""  			#string
    data = "".encode()	#bytes
    data = b"" 			#bytes