vargu1 = [10, 20 , 50,10]
vargu2 = [3,4,5,2,1]
vargu3 = [123,4213,111]


def mean (xs):
    return sum(xs)//len(xs)

def median_odd(xs):
    return sorted(xs)[len(xs) // 2]

def median_even (xs):
    sorted_xs=sorted(xs)
    hi_midpoint = len(xs)//2
    return (sorted_xs[hi_midpoint-1]+sorted_xs[hi_midpoint]/2)

def median(v):
    return median_even(v) if len(v) % 2 == 0 else median_odd(v)

def distributions(xs):
    if (median(xs) == mean(xs)):
        return 'Normal Distribution'
    elif (median(xs) > mean(xs)):
        return 'Negative Distribution'
    else:
        return'Positiv Distribution'
def print(xs):
    print ("Mediana: "+ str(median(xs)))
    print ("Mesatarja: "+str(mean(xs)))
    print (distributions(xs))
    print ('')
print(vargu1)
print(vargu2)
print(vargu3)