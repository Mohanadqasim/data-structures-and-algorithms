from LinkedList import LinkedList
if __name__ == "__main__":
    list = LinkedList()
    
    list.insert("A")
    list.insert("B")
    list.insert("this to return \"True\"")

    print(list)
    print(list.include("A"))
    print(list.include("this should return \"False\""))
    print(list.include("this to return \"True\""))
