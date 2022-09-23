import unittest

from.account import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_name(self):
        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_account_deposit_funds(self):
        self.acc.deposit(2000)
        self.assertEqual(2000, self.acc.get_balance())

    def test_that_account_withdraw_funds(self):
        self.acc.withdraw(1000)
        self.assertEqual(1000, self.acc.get_balance())

    def test_that_account_transfer_funds(self):
        self.acc1 = Account("Hadiza")
        self.acc2 = Account("Umar")

        self.acc1.deposit(4000)
        self.assertEqual(4000, self.acc1.balance)
        self.acc1.transfer(1000, self.acc2)
        # self.assertEqual(1000, self.acc1.balance)

        self.assertEqual(3000, self.acc1.balance)


if __name__ == '__main__':
    unittest.main()
