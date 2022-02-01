def separator(ls):
    odd_list =  list( filter( lambda n: n%2, ls) )
    even_list =  list( filter( lambda n: not n%2, ls) )
    return (even_list, odd_list)