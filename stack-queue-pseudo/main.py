from pseudo_queue import Pseudo_queue

if __name__ == '__main__':
    queue1=Pseudo_queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(5)
    print(queue1)
    print(queue1.peek())
