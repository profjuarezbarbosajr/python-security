# binascii — Convert between binary and ASCII
# data validation checks

# use of binascii.crc32(data[, value])

# Compute CRC-32, the unsigned 32-bit checksum of data, starting with an initial CRC of value. 
# The default initial CRC is zero. The algorithm is consistent with the ZIP file checksum. 
# Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use
# as a general hash algorithm. 

import binascii

print(binascii.crc32(b"hello world"))
# Or, in two pieces:
crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))
