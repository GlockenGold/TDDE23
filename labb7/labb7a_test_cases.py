import labb7a

def labb7a_test():
    test1 = ['--']
    assert labb7a.search(test1, db) == db

    test2 = ['--', ['författare', ['--']], ['titel', ['diskret', 'matematik']],
       ['år', 2012]]
    result2 = [[['författare', ['armen', 'asratian']],
                ['titel', ['diskret', 'matematik']], ['år', 2012]]]
    assert labb7a.search(test2, db) == result2

    test3 = [['författare', ['&', 'asratian']], '--']
    assert labb7a.search(test3, db) == result2

    test4 = [['författare', ['&']], '--']
    result4 = []
    assert labb7a.search(test4, db) == result4

    test5 = ['--', ['titel', ['--', 'an', '--']], '--']
    result5 = [[['författare', ['john', 'zelle']],
                ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
                ['år', 2010]], [['författare', ['j', 'glenn', 'brookshear']],
                ['titel', ['computer', 'science', 'an', 'overview']],
                ['år', 2011]]]

    assert labb7a.search(test5, db) == result5


    print ("Labb7a passed all the tests!")


db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], 
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]
