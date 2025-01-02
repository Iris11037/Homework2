import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        my_walk = Runner("Aristotel")
        for i in range(10):
            my_walk.walk()
        self.assertEqual(my_walk.distance, 50)

    def test_run(self):
        my_run = Runner("Aristotel")
        for i in range(10):
            my_run.run()
        self.assertEqual(my_run.distance, 100)

    def test_challenge(self):
        my = Runner("Aristotel")
        my_friend = Runner("Tsusha")
        for i in range(10):
            my.run()
            my_friend.walk()
        self.assertNotEqual(my.distance, my_friend.distance)

if __name__ == '__main__':
    unittest.main()