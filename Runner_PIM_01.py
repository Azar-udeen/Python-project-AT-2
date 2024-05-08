from TC_PIM_01 import ForgetPassword
import unittest

def main():
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(ForgetPassword)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

if __name__ == '__main__':
            main()