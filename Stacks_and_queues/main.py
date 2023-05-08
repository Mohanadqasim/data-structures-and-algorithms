from queue_file import Queue
from stack_file import Stack
if __name__ == '__main__':
    queue1=Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    print(queue1)
    queue1.dequeue()
    print(queue1)
    queue1.enqueue(4)
    print(queue1)
    
    print('*******************************************')
    
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1)
    stack1.pop()
    print(stack1)
    stack1.push(4)
    print(stack1)
