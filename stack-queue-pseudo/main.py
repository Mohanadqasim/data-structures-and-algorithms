from pseudo_queue import Pseudo_queue

if __name__ == '__main__':
    queue1=Pseudo_queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    print(queue1)
    queue1.dequeue()
    print(queue1)
    # queue1.enqueue(4)
    print(queue1.peek())