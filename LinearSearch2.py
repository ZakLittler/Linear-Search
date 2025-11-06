#   Linear Search
#   Zak Littler
#   06/11/25
#   OCR AS Computer Science

#

#   - Imports -




#   - Constants -




#   - Global Variables -

example_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
find = 5


#   - Sub-Programs -

def linSearch(plist, find):
    found = False
    index = -1
    
    for item in plist:
        index += 1
        
        if item == find:
            found = True
            break

    if found:
        return found, count

    else:
        return found, -1


#   - Main Program -

try:
    linSearch(example_list, find)

except Exception as e:
    print("Error Occured", e)
