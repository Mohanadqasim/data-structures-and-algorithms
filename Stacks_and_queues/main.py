from Stacks_and_queues.queue_file import Queue
from Stacks_and_queues.stack_file import Stack
if __name__ == '__main__':
    queue1=Queue()
    queue1.enqueue(6)
    queue1.enqueue(5)
    queue1.enqueue(4)
    queue1.enqueue(3)
    queue1.enqueue(2)
    queue1.enqueue(1)
    print(queue1)
    queue1.dequeue()
    # queue1.dequeue()
    print(queue1)
    # print(queue1.peek())


    # stack1 = Stack()
    # stack1.push(1)
    # stack1.push(2)
    # stack1.push(3)
    # print(stack1)
    # stack1.pop()
    # print(stack1)
    # stack1.pop()
    # stack1.pop()
    # stack1.pop()
    # print(stack1)
    # # stack1.push('a')
    # # stack1.push('b')
    # # stack1.push('c')
    # print(stack1.peek())
    # print(stack1.get_size())
    # print(stack1.is_empty())
