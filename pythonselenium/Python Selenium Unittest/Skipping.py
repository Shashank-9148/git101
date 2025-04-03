import  unittest


class AppTesting(unittest.TestCase):
    @unittest.SkipTest #decorator
    def test_search(self):
        print("Search test is passed")

    @unittest.skip("I am skipping this because test is not ready")
    def test_advanced_search(self):
        print("Advanced test is passed")

    @unittest.skipIf(1==1,"Numbers are equals")
    def test_prepaid_search(self):
        print("prepaid is passed")

    def test_postpaid_search(self):
        print("postpaid is passed")

    def test_login_email(self):
        print("email is passed")

    def test_login_twitter(self):
        print("twitter is passed")

if __name__ == "__main__":
    unittest.main()