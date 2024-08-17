class Author:
    def __init__(self,name=None):
        self.name = name
        self.dic = {}
        self.count = 0

    def setName(self,n=None):
        self.name = n
    
    def addBook(self,*s):
        if self.name == None:
            print("A book can not be added without author name ")
        else:
            if len(s) == 2:
                if s[1] not in self.dic:
                    self.dic[s[1]] = s[0]
                    self.count += 1
                else:
                    self.dic[s[1]] += ", " + s[0]
                    self.count += 1

    def printDetail(self):
        print(f"Number of Book(s): {self.count}\nAuthor Name: {self.name}")
        for k,v in self.dic.items():
            print(f"{k}:{v}")

a1 = Author() 
print("=================================") 
a1.addBook("Ice", "Science Fiction") 
print("=================================") 
a1.setName("Anna Kavan") 
a1.addBook("Ice", "Science Fiction") 
a1.printDetail() 
print("=================================") 
a2 = Author("Humayun Ahmed") 
a2.addBook("Onnobhubon", "Science Fiction") 
a2.addBook("Megher Upor Bari", "Horror") 
print("=================================") 
a2.printDetail() 
a2.addBook("Ireena", "Science Fiction") 
print("=================================") 
a2.printDetail() 
print("=================================")
