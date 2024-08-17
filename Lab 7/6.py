class Library:
    def __init__(self,loc,books):
        self.loc = loc
        self.books = books
        self.borrower = {}
    
    def details(self):
        print(f"{self.loc} Library details")
        print(f"Borrower Details:\n{self.borrower}\nBooks availibility:\n{self.books}")

class Reader:
    def __init__(self,name):
        self.name = name
        self.borrowed_book = {}
        self.count = 0

    def borrow(self,obj,*book):
        for i in book:
            if obj.books[i] != 0:
                if self.count < 5:
                    print(f"{i} book is borrowed succcessfully.")
                    self.count += 1
                    if i not in self.borrowed_book or self.borrowed_book == {}:
                        self.borrowed_book[i] = 1
                    else:
                        self.borrowed_book[i] += 1
                    for k,v in obj.books.items():
                        if k == i:
                            obj.books[k] -= 1
                else:
                    print("You cannot borrow more than 5 books.")
                    break

            else:
                print(f"{i} books are not available at the moment.")

        obj.borrower[self.name] = self.count

    def readerInfo(self,*topic):
        if len(topic) == 0:
            print(f"{self.name}, you have {self.count} book(s) with you.")
            for k,v in self.borrowed_book.items():
                print(f"Books on {k}: {v}")

        else:
            for i in topic:
                for k,v in self.borrowed_book.items():
                    if k == i:
                        print(f"{self.name}, you have {v} {k} book(s) with you.")


L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()