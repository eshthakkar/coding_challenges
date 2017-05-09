def flatten(d):
    """ Flatten a nested dictionary"""
    
    results = {}

    for k, v in d.iteritems():
        if isinstance(v, dict):
            for k2,v2 in flatten(v).iteritems():
                results[k + "." + k2] = v2
        else:
            results[k] = v

    return results                


# Tests
indict = {
        "Key1" : 1,
        "Key2" : {
                "a" : 2,
                "b" : 3,
                "c" : {
                    "d" : 3,
                    "e" : 1
                    }
                }
        }

print flatten(indict)
