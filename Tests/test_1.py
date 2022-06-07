
############## Ex Cours
def t_1(a,b):
    return a+b

def test_1():
    a = 5
    b = 10
    assert t_1(a,b)==15

#############################

def isinterger(a):
    if int(a):
        return True 


def test_isinteger(): 
    assert isinterger(2)==True   # doit passer 
    assert isinterger(4.5)== False # ne doit pas passer 
    assert isinterger(2)==True # Ne doit pas passer 