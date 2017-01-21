from TestCribbage import *
from TestHandScorer import *

if __name__ == '__main__':
    global TESTING
    TESTING = True
    generate_card_test_list()
    unittest.main()
    #test_suite = unittest.TestSuite()
    #test_runner = unittest.TextTestRunner()
    #test_suite.addTest(unittest.makeSuite(Test_atoi))
    #test_suite.addTest(unittest.makeSuite(Test_Card))
    #test_suite.addTest(unittest.makeSuite(Test_CardSuite))
    #test_suite.addTest(unittest.makeSuite(Test_CardType))
    #test_suite.addTest(unittest.makeSuite(Test_HandScorer))
    #test_runner.run(test_suite)
