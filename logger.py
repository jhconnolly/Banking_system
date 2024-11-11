import logging
logging.basicConfig(filename='logs/bank.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_transaction(transaction):
    logging.info(transaction)