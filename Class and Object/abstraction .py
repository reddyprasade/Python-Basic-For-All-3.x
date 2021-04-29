class Payment(ABC):

    def print_slip(self,amount):
        print("Puruchase of amount",amount)
    
    @abstractmethod
    def payment(self,amount):
        pass


class CreditCardPayment(Payment):
    def payment(self,amount):
        print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
    def payment(self,amount):
        print('Mobile Wallet payment of- ', amount)
        
        
        
CCP = CreditCardPayment()
CCP.payment(10000)
CCP.print_slip(10000)
print(isinstance(CCP, Payment))

MWP = MobileWalletPayment()
MWP.payment(250)
MWP.print_slip(250)
