from pprint import pprint

def num_dict(n):
    return{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)}

pprint([num_dict(i) for i in range(16)])
#