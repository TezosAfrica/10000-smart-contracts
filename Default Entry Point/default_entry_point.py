import smartpy as sp

class MyContract(sp.Contract):
    def __init__(self):
        self.init(payments = sp.list(t = sp.TRecord(address = sp.TAddress, amount = sp.TMutez)))

    @sp.entry_point
    def default(self):
        self.data.payments.push(sp.record(address = sp.source, amount = sp.amount))


@sp.add_test(name = "Test")
def test():
    c = MyContract()
    s = sp.test_scenario()
    s += c

    a = sp.test_account('A')
    b = sp.test_account("B")

    c.default().run(sender=b.address, source=a.address, amount=sp.mutez(1000000))