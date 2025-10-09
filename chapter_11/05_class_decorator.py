class Principle:
    a = 1

    ## IMP: without @classmethod during "self" it uses the inheritance's object value, with @classmethod it force "self" to use it's own value where it defined

    @classmethod  ## it force a to take value from it's own parent not inheritance
    def att(cls):
        print(f"Principle's attribute a is : {cls.a} ")


e = Principle()
e.a = 50

e.att()
