def high_key(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
         ## possible weakness in max(v), returns the first key/value in list if multiple highest values present in dict.
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
