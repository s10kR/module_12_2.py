import runner_and_tournament as runtour
import unittest as ut


class TournamentTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        print('TEST IS STARTED')

    def setUp(self):
        self.runner_1 = runtour.Runner('Усэйн', 10)
        self.runner_2 = runtour.Runner('Андрей', 9)
        self.runner_3 = runtour.Runner('Ник', 3)

    def test_sprint1(self):
        sprint_1 = runtour.Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results[1] = sprint_1.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[1][2], 'Ник')
        # print('Track run 1')

    def test_sprint2(self):
        sprint_2 = runtour.Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results[2] = sprint_2.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[2][2], 'Ник')
        # print('Track run 2')

    def test_sprint3(self):
        sprint_3 = runtour.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results[3] = sprint_3.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[3][3], 'Ник')
        # print('Track run 3')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for number_test in TournamentTest.all_results:
            print(number_test, ':', end=' ')
            for i in TournamentTest.all_results[number_test]:
                print(i, '-', TournamentTest.all_results[number_test][i], end=' ')
            print()
        print('TEST IS COMPLETE')


if __name__ == "__main__":
    ut.main()