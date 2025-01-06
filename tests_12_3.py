import unittest
from tests_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        my_walk = Runner("Aristotel")
        for i in range(10):
            my_walk.walk()
        self.assertEqual(my_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        my_run = Runner("Aristotel")
        for i in range(10):
            my_run.run()
        self.assertEqual(my_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        my = Runner("Aristotel")
        my_friend = Runner("Tsusha")
        for i in range(10):
            my.run()
            my_friend.walk()
        self.assertNotEqual(my.distance, my_friend.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = Runner("Усэйн", 10)
        self.run2 = Runner("Андрей", 9)
        self.run3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, res in cls.all_results.items():
            print(f"{key}: {res}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tour = Tournament(90, self.run1, self.run3)
        res = tour.start()
        self.all_results['test1'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tour = Tournament(90, self.run2, self.run3)
        res = tour.start()
        self.all_results['test2'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tour = Tournament(90, self.run2, self.run1, self.run3)
        res = tour.start()
        self.all_results['test3'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

if __name__ == '__main__':
    unittest.main()