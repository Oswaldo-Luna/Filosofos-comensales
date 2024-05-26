import threading
import random
import time

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.times = 0
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.start()

    def run(self):
        while self.times < 6:
            self.think()
            self.dine()

    def think(self):
        print('El Filósofo %s está pensando' % self.index)
        time.sleep(random.randint(5, 10))
        print('El Filosofo %s tiene hambre.' % self.index)

    def dine(self):
        # Filósofos pares toman el tenedor izquierdo primero, luego el derecho
        # Filósofos impares toman el tenedor derecho primero, luego el izquierdo
        if self.index % 2 == 0:
            self.left_fork.acquire()
            self.right_fork.acquire()
        else:
            self.right_fork.acquire()
            self.left_fork.acquire()

        self.times += 1
        self.dining()
        # Suelta los tenedores cuando termina de comer
        self.right_fork.release()
        self.left_fork.release()

    def dining(self):
        print('El Filosofo %s comienza a comer por: %s vez. ' % (self.index, self.times))
        time.sleep(random.randint(5, 10))
        print('El Filosofo %s ha terminado de comer.' % self.index)


def main():
    forks = [threading.Semaphore() for _ in range(1, 6)]

    for i in range(1, 6): Philosopher(i, forks[i % 5], forks[(i + 1) % 5])


if __name__ == "__main__":
    main()