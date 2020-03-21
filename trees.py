#computerphile coding trees in python
#with Professor Thorsten Altenkirch
# book conceptual programming with python

#expression 1 = 3 * (y + x)
#expression 2 = 3 * y + x

class Expr:
    pass

#subclasses of expression
#operators, constants, variables

class Times(Expr):
    """when you do multiplication you need two expressions,
    one to the left of the * operator and and one to the right"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "*" + str(self.right) + ")"

    def evaluate(self, envDict):
        """Here you really see the recursion. Evaluate the left, then the right,
        then multiply the two"""
        return self.left.evaluate(envDict) * self.right.evaluate(envDict)

class Plus(Expr):
    """when you do addition you need two expressions,
        one to the left of the + operator and and one to the right"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

    def evaluate(self, envDict):
        """Here you really see the recursion. Evaluate the left, then the right,
        then add the two"""
        return self.left.evaluate(envDict) + self.right.evaluate(envDict)

class Const(Expr):
    """For a constant we just initialize a value (i.e. 3, 5, 7, etc.)"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def evaluate(self, envDict):
        """Can just return the value because the value of the constant
        does not depend on the assignment to vlaues"""
        return self.value

class Var(Expr):
    """For a variable, we just need its string name"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def evaluate(self, envDict):
        """There is a dependency here so you must return the value stored at the
        key entered in as name"""
        return envDict[self.name]

expression1 = Times(Const(3), Plus(Var("y"), Var("x")))

expression2 = Plus(Times(Const(3), Var("y")), Var("x"))

print(expression1)
print(expression2)

#Now lets do an evaluation using a dictionary

environ = {"x": 2, "y": 4}

print(expression1.evaluate(environ))  #3*2+4 = 18

print(expression2.evaluate(environ))  #3*4+2 = 14