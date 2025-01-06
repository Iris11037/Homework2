import unittest
import tests_12_3

clas = unittest.TestSuite()
clas.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
clas.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
run = unittest.TextTestRunner(verbosity=2)
run.run(clas)