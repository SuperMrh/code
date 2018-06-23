from random import randint


def say_hello():
    num = randint(1, 3)
    return 'hello' if num == 1 else 'hello' * 2 if num == 2 else 'hello' * 3
  
  
if __name__ == '__main__':
    print(say_hello())
