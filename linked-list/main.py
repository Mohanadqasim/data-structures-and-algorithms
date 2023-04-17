from LinkedList import LinkedList
if __name__ == "__main__":
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("1")
    list.append("2")
    list.insert_after("a","777")
    list.insert_before("c","Z")
    list.delete("777")
    print(list)
    