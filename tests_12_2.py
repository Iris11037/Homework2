import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
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

    def test_1(self):
        tour = Tournament(90, self.run1, self.run3)
        res = tour.start()
        self.all_results['test1'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

    def test_2(self):
        tour = Tournament(90, self.run2, self.run3)
        res = tour.start()
        self.all_results['test2'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

    def test_3(self):
        tour = Tournament(90, self.run2, self.run1, self.run3)
        res = tour.start()
        self.all_results['test3'] = {k: str(runner) for k, runner in res.items()}
        self.assertTrue(res[max(res)] == 'Ник')

if __name__ == "__main__":
    unittest.main()