class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = "" #string to store encoded result
        for s in strs: #for each string in the input, add it to res with a delimiter and length
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #empty list to store decoded strings
        i = 0 #traversal index
        
        while i < len(s): #loop through string until the end
            j = i
            while s[j] != '#': #j starts at current index until the delimiter
                j += 1
            length = int(s[i:j]) #covert length of this word to int
            i = j + 1 #update i to start of the string (past the delimiter)
            j = i + length #endpoint of the string
            res.append(s[i:j]) #append extracted string to the result list
            i = j #start processing next length
             
        return res