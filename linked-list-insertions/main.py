from LinkedListInsertions import Linked_List
if __name__ == "__main__":
    list = Linked_List()
    
    list.append("A")
    list.append("B")
    list.append("C")
    # list.insert_before("B","X")
    list.insert_after("C","Z")


    print(list)