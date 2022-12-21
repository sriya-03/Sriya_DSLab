class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return not self.items
    def display(self):
        for item in self.items:
            print(item)


def print_menu():
    print('1. Enqueue an item')
    print('2. Dequeue an item')
    print('3. Peek at the front item')
    print('4. Check if the queue is empty')
    print('5. Quit')
    print()


queue = Queue()

while True:
    print_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        item = input('Enter an item to enqueue: ')
        queue.enqueue(item)
    elif choice == 2:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('Dequeued', queue.dequeue())
    elif choice == 3:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('Peeked', queue.peek())
    elif choice == 4:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('The queue is not empty.')
    elif choice == 5:
        break
    elif choice==6:
        print(queue.display())
    else:
        print('Invalid choice. Enter a number between 1 and 5.')
    print()
