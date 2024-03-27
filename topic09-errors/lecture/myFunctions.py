# a module of useful functions
# Author: Finbar Dennehy

import logging
logging.basicConfig(filename="./bank.log",
                    level=logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d")
balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the amount ({amount}) should never be less than 0")
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.critical(f"trying to withdraw ({amount}) more than is in account ({balance})")
        raise ValueError("not enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount} new balance is {balance}")
    return balance

# only run if running myFunctions.py, not if I'm running testMyFunctions.py
if __name__ == "__main__":
    #print("dont want this")
    assert withdraw(20) == 80, "incorrect calculation"
    try:
        withdraw(-1)
        assert False, "this should have thrown a value error"
    except ValueError as ve:
        pass

    try:
        withdraw(110)   
        assert False, "can't withdraw more than is in the account balance" 
    except ValueError as ve:
        pass
    print("all good")