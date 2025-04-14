#huffman coding - greedy technique
import heapq
from collections import defaultdict

def generate_huffman_codes(text:str) -> tuple[dict[str,str],dict[str, int]]:
    frequency = defaultdict(int)
    for char in text:
        frequency[char]+=1
        
    heap = []
    for char, freq in frequency.items():
        heap.append([freq, [char, ""]])
    heapq.heapify(heap)
    
    while len(heap)>1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        
        for pair in low1[1:]:
            pair[1] = "0" + pair[1]
            
        for pair in low2[1:]:
            pair[1] = "1" + pair[1]
            
        combined = [low1[0] + low2[0]] + low1[1:] + low2[1:]
        heapq.heappush(heap, combined)
        
    huffman_codes = {}
    for char, code in heap[0][1:]:
        huffman_codes[char] = code
        
    return huffman_codes, frequency

#test case
text = "huffman coding is fun"
codes, freqs = generate_huffman_codes(text)
print("Character Frequencies:", freqs)
print("Huffman Codes:", codes)