{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPyaAeFJpqy2IY2/vUaGCkk"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "class Queue:\n",
        "    def __init__(self):\n",
        "        self.items = []\n",
        "\n",
        "    def enqueue(self, item):\n",
        "        self.items.append(item)\n",
        "\n",
        "    def dequeue(self):\n",
        "        return self.items.pop(0)\n",
        "\n",
        "    def peek(self):\n",
        "        return self.items[0]\n",
        "\n",
        "    def is_empty(self):\n",
        "        return not self.items\n",
        "    def display(self):\n",
        "        for item in self.items:\n",
        "            print(item)\n",
        "\n",
        "\n",
        "def print_menu():\n",
        "    print('1. Enqueue an item')\n",
        "    print('2. Dequeue an item')\n",
        "    print('3. Peek at the front item')\n",
        "    print('4. Check if the queue is empty')\n",
        "    print('5. Quit')\n",
        "    print()\n",
        "\n",
        "\n",
        "queue = Queue()\n",
        "\n",
        "while True:\n",
        "    print_menu()\n",
        "    choice = int(input('Enter your choice: '))\n",
        "\n",
        "    if choice == 1:\n",
        "        item = input('Enter an item to enqueue: ')\n",
        "        queue.enqueue(item)\n",
        "    elif choice == 2:\n",
        "        if queue.is_empty():\n",
        "            print('The queue is empty.')\n",
        "        else:\n",
        "            print('Dequeued', queue.dequeue())\n",
        "    elif choice == 3:\n",
        "        if queue.is_empty():\n",
        "            print('The queue is empty.')\n",
        "        else:\n",
        "            print('Peeked', queue.peek())\n",
        "    elif choice == 4:\n",
        "        if queue.is_empty():\n",
        "            print('The queue is empty.')\n",
        "        else:\n",
        "            print('The queue is not empty.')\n",
        "    elif choice == 5:\n",
        "        break\n",
        "    elif choice==6:\n",
        "        print(queue.display())\n",
        "    else:\n",
        "        print('Invalid choice. Enter a number between 1 and 5.')\n",
        "    print()"
      ],
      "metadata": {
        "id": "aI4wvRyLd5pb"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}