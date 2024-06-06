class Parent:
    def printLog(self):
        print("Logs from Parent")


class Child(Parent):
    def __init__(self) -> None:
        self.a = Parent()

    def printLog(self):
        print("Logs from Child")

# Creates Parent method
parent = Parent()
parent.printLog()

child = Child()
# Print child method
child.printLog()

# prints parent method
child.a.printLog()