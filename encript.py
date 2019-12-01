a = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'''
def cripter(mess, key, op):
    #function for individual letters
    def sl(l1, l2):
        for x in a:#transform the first letter into a number
            if l1 == x:
                l1 = a.index(x) + 1
            if l2 == x:
                l2 = a.index(x) + 1
        #sum the numbers and transform back to a letter
        r = l1 + l2*op#op = +1 or -1. +1 for sum, -1 for subtract
        if r > len(a):
            r -= len(a)
        return a[r-1]
    #process
    new = ''
    k = 0
    for x in mess:
        new += sl(x, key[k])
        k += 1
        if k == len(key):
            k = 0
    return new
