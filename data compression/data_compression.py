import time

string = 'In computer science, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes.'

# Calculating frequency
def calc_freq(string):
    freq = {}
    total = 0
    for c in string:
        if c in freq:
            freq[c] += 1
            total += 1
        else:
            freq[c] = 1
            total += 1
    return (freq,total)

freq,total = calc_freq(string)
print("Frequency of characters : \n",freq)
print("\nTotal characters(frequency) : ",total)


# ASCII (METHOD 1)
start=time.time()

print("\n*************** ASCII METHOD ***************")
freq,total = calc_freq(string)
ascii = total * 7           # ASCII value(0-127) 7 bits
print("\nTotal no. of bits using ASCII Method (Method1) : ",ascii)

end = time.time()
print('Time of execution for METHOD-1 : {} '.format(end - start))


# 5-bits (METHOD 2)
start=time.time()

print("\n*************** 5-BITS METHOD ***************")
freq,total = calc_freq(string)
bit = total * 5           # 5-bits => A-Z/a-z(26 chars) => 2^5 = 32(>26)
print("\nTotal no. of bits using 5-Bits Method (Method-2) : ",bit)

end = time.time()
print('Time of execution for METHOD-2 : {} '.format(end - start))


# Huffman Coding (METHOD 3)
# A data compression algorithm to lower the cost of communication

import heapq                #from heapq using(importing) heappush, heappop, heapify
 
def encode(freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
#Driver Code 
start=time.time()

print("\n*************** HUFFMAN CODING ***************")
freq,total = calc_freq(string)
huff = encode(freq)
totalhuff = 0

print("\nSymbol\tHuffman Code\tWeight")
for p in huff:
    print("{}\t{}\t\t{}".format(p[0], p[1], freq[p[0]]))
    totalhuff += freq[p[0]]
print("\nTotal no. of bits using Huffman Coding (Method-3) : ",totalhuff) 

end = time.time()
print('Time of execution for METHOD-3 : {} '.format(end - start))   