{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN6J4tY9BMEv6yrAuLQFgDF"
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
        "id": "PGQKBwF2Fszb"
      },
      "outputs": [],
      "source": [
        "def binary_search(data, target):\n",
        "    low = 0\n",
        "    high = len(data) - 1\n",
        "    while low <= high:\n",
        "        mid = (low + high) // 2\n",
        "        if data[mid] == target:\n",
        "            return mid\n",
        "        elif data[mid] < target:\n",
        "            low = mid + 1\n",
        "        else:\n",
        "            high = mid - 1\n",
        "    return -1\n",
        "\n",
        "def main():\n",
        "    data = []\n",
        "    limit=int(input(\"Enter size of list\"))\n",
        "    for i in range (limit):\n",
        "        a=input()\n",
        "        data.append(a)\n",
        "    target = input(\"Enter a target value: \")\n",
        "    index = binary_search(data, target)\n",
        "    if index == -1:\n",
        "        print(\"Value not found\")\n",
        "    else:\n",
        "        print(\"Value found at index\", index)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    }
  ]
}