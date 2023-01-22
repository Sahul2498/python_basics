# def hello():
def dec(fun):
    def wra(*args, **ka):
        print("Before")
        a = fun(*args, *ka)
        print("After")
        return a
    return wra


@dec
def hell(ah):
    print("Done {}".format(ah))


hell('s')
   
