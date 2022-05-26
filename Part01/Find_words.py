import os
def reading():
  with open("hello.txt") as f:
    total = 0
    for a in f:
      print(a.strip())
      word_list = a.split()
      print(word_list)
      numWords = len(word_list)
      total += numWords
      print(total)

def start():
  print("Opening 'hello.txt'.")
  reading()
start()
  #Could not figure out the 'histogram' thingy. I just found a way to make it myself. I suppose I could have it loop for each space and count them.