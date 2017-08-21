api_map = {
    'k1':'v1',
    'k2':'v2',
    'k3':{'k4':'v4', 'k5':'v5'},
    'k6':'v6'

}

res_map= {}

def flatten_map(api_map):
    for k, v in api_map.iteritems():
        if not isinstance(v,dict):
            res_map[k] = v
        else:

            flatten_map(v)
    return res_map


print flatten_map(api_map)
