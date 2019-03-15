def Anagram(str1, str2): 

    count1 = [0] * 26                           #To count frequency of each character
    count2 = [0] * 26 
  

    i = 0
    while i < len(str1):                        #Counts frequency of each character for str1
        count1[ord(str1[i])-ord('a')] += 1	# 'ord' refers to the unicode value for each respective character
        i += 1
  

    i =0
    while i < len(str2): 
        count2[ord(str2[i])-ord('a')] += 1      #Count frequency of each character for str2 
        i += 1


    result = 0                                  #Transverses the count arrays to find and remove the character
    for i in range(26):                         #from both strings until they are anagrams.
        result += abs(count1[i] - count2[i]) 
    return result 

  
# Driver program to run the case 
if __name__ == "__main__": 
    str1 = "bcadeh"
    str2 = "hea"
    print(Anagram(str1, str2)) 
