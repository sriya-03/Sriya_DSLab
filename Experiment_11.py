{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPUk4W/7KBE/8tTv/qzHLN5"
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
      "execution_count": null,
      "metadata": {
        "id": "4gsBxKvgUYTq"
      },
      "outputs": [],
      "source": [
        "def pop(stack):\n",
        "    stack.pop()\n",
        "    \n",
        "def push(value,stack,top,limit):\n",
        "    if top>=limit:\n",
        "        print(\"Stack overflow!\")\n",
        "    else:\n",
        "        stack.append(value)\n",
        "\n",
        "def peak(stack,top):\n",
        "    return stack[top]\n",
        "\n",
        "def display(stack,limit,top):\n",
        "    for i in range(limit):\n",
        "        print(stack[top])\n",
        "        top=top-1\n",
        "        if top<0:\n",
        "            break\n",
        "\n",
        "stack=[]\n",
        "top=-1\n",
        "limit=int(input(\"Please enter size of stack\"))\n",
        "for i in range(limit):\n",
        "        a=input()\n",
        "        stack.append(a)\n",
        "        top+=1\n",
        "print(\"Please select the command you want to execute:\")\n",
        "print(\"1: Adding value to stack\")\n",
        "print(\"2: Poping a value\")\n",
        "print(\"3: Displaying stack\")\n",
        "print(\"4: To print the last value\")\n",
        "b=int(input())\n",
        "if b==1:\n",
        "    print(\"Enter of elements you want to add\")\n",
        "    limit1=int(input())\n",
        "    print(\"Before adding value:\",stack)\n",
        "\n",
        "    for i in range(limit1):\n",
        "        value=input()\n",
        "        push(value,stack,top,limit)\n",
        "    print(\"After adding values:\",stack)\n",
        "\n",
        "elif b==2:\n",
        "    print(\"Enter how many elements you want to remove\")\n",
        "    limit2=int(input())\n",
        "    for i in range(limit2):\n",
        "        print(\"Before Pop:\",stack)\n",
        "        pop(stack)\n",
        "        print(\"After pop:\",stack)\n",
        "\n",
        "elif b==4:\n",
        "    print(\"Last value is:\",peak(stack,top))\n",
        "\n",
        "elif b==3:\n",
        "    print(\"The Current Stack elements are:\")\n",
        "    display(stack,limit,top)"
      ]
    }
  ]
}