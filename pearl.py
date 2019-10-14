"""
name:		Daniel Melero Martinez
email:		daniel.melero.001@gmail.com

name:		Brand Hauser
email:		b.j.hauser@student.utwente.nl
"""


import util



def make_table(word_pairs):

    res = word_pairs #load word_pairs to res
    res = sort(res) #run sort function
    res = remove_dups(res) #run remove_dups function
    return res

def make_counted_table(pairs):
#Sort every word and then remove duplicated word and add a list of files in which the words occur and how many times
    res = remove_dups_counted(sort(pairs))
    return res

def make_density_table(pairs):
#Sort every word and then remove duplicated word and add a list of files in which the words occur and the frequency
    res = count_to_density(make_counted_table(pairs))
    return res

def sort(data):
    if len(data) == 0 or len(data) == 1: #check length of data if data 0 or 1 you're  done
        return data
    else:
        fst = sort(data[:len(data)//2]) #copy first half of data
        snd = sort(data[len(data)//2:]) #copy second half of data
        res = [] #create empty result list
        fi = si = 0 #create fi and si increasing indexes
        while fi < len(fst) and si < len(snd): #check if fi and si are valid
            if ( fst [fi ][0] < snd [si][0] #if fi is smaller than si
                or fst [fi ][0] == snd [si][0] and fst [fi ][1] < snd [si][1]): #or fi and si equal but second element of fi smaller
                res.append(fst[fi]) #add first half fi to result
                fi += 1 #increment fi
            else:
                res.append(snd[si]) #add second si to result
                si += 1 #increment si
        if fi < len(fst): #check if fi is less than length of first
            res.extend(fst[fi:]) #add first fi to end of result
        else:
            if si < len(snd): #check if si is less than length
                res.extend(snd[si:]) #add second si to end of list
        return res

def remove_dups(data):
    fresh = data[0] # copy data[0] to fresh
    i = 1
    res = [] #create empty list
    new = [] #create empty list
    if len(data) > 0: # check if data is empty
        while i < len(data) - 1: #check if i is valid
            if data[i] != fresh: # check if data[i] and fresh are not equal
                new = fresh #copy fresh to new
                val = [] #create empty list
                val.append(fresh[0]) # add word to val
                while i < len(data) and data[i][0] == fresh[0]: #check if data word and fresh word match
                    if data[i][1] not in new: # check if filename is not in new
                        new.append(data[i][1]) # add filename to new
                    i += 1
                else:
                    new.remove(new[0]) # remove word from new
                    val.append(new) # add new to val
                    res.append(val) # add val to res
            fresh = data[i] #overwrite data[i] to fresh
            i +=1
        fresh = data[i] #overwrite data[i] to fresh
        i += 1
        res.append(fresh) # add fresh to result

    return res

def remove_dups_counted(data):
    res = []    #res is the result list
    if len(data) > 0:   #If data is empty, data[0] does not exist
        fresh = [data[0][0],[[data[0][1],1]]]   #fresh is a fresh value not yet occurring in res
        i = 1
        while i < len(data):    #Continue until the end of data
            if data[i][0] != fresh[0]:  #We arrived at the next distinct value
                res.append(fresh)   #The previous fresh value is added to res
                fresh = [data[i][0],[[data[i][1],1]]]   #This is the next fresh value
            else:   #the next value is the same as the fresh value
                j, freshfiles, sim = 0, [], False
                while j < len(fresh[1]):
                    if data[i][1] == fresh[1][j][0]:
                        sim = True
                        freshfiles.append([fresh[1][j][0],fresh[1][j][1]+1])
                        #add 1 to the counter when the filename was already registered
                    else:
                        freshfiles.append(fresh[1][j])
                    j += 1
                if sim == False:
                    freshfiles.append([data[i][1],1])
                    #add the filename when it wasn't registered
                fresh = [data[i][0], counter_bubble_sort(freshfiles)]
                #sort the filenames in decreasing order of the number of times the word occurs in the file
            i += 1
        res.append(fresh)   #The last fresh value is appended to res
    return res

def counter_bubble_sort(data):
#sort filenames by the number of times that the word occur
#bubble sort is used because the lists that have to be sorted are short and most of the times already sorted
    res = data  #res is the result list
    ui = len(res) - 1   #ui is the index of the last unsorted value
    while ui > 0:   #If ui equals 0, everything is sorted
        si = 0  #si is the index of the last swapped value
        i = 0   #i is the index that is currently processed
        while i < ui:   #If ui is reached then the rest is ordered
            if res[i][1] < res[i+1][1]:
                res[i], res[i+1] = res[i+1], res[i] #res[i] en res[i+1] are inverted
                si = i  #We just swapped at index i
            i += 1
        ui = si #The list is ordered from si+1
    return res

def count_to_density(data):
    res = data  #res is the result list
    filenames,filewords = [],[] #list of number of words for each file
    if len(data) > 0:
        i = 1
        while i < len(res):  #Continue until the end of data
            j = 0
            while j < len(res[i][1]):   #Continue until done with every filename
                word = res[i][1][j] #["filename", "number that this word occur"]
                if word[0] not in filenames:
                    #if the number of words of a file is not yet regired then register it
                    filenames.append(word[0])
                    filewords.append(len(util.words(word[0])))
                index = filenames.index(word[0])
                word[1] = round(word[1]/filewords[index],4) #Place density instead of counter and round the result
                j += 1
            res[i][1] = counter_bubble_sort(res[i][1])  #sort all the filenames in decreasing order of density
            i += 1
    return res
