import subprocess
import os
import logging
import pandas as pd
import datetime

if __name__ == '__main__':
    logging_filename = datetime.datetime.utcnow().strftime(r'%Y-%m-%d_%H:%M:%S') + '.log'
    logging.basicConfig(filename=logging_filename, level=logging.DEBUG)

    logging.info('* start data collection')

    sc = pd.read_csv('erc-721.csv')

    os.environ['RPC_URL'] = 'http://127.0.0.1:8547'
    for index, row in sc.iterrows():
        try:
            tag, address = row[0], row[1]
            #if tag != 'MoonLanderz':
            #    continue
            logging.info('\ntag: {}\naddress: {}\n\n'.format(tag, address))

            target_dir = 'collected-data' + '/' + tag + '/' + address

            os.makedirs(target_dir, exist_ok=True)

            subprocess.run('python -m scrape_721 {} -p {} -R'.format(address, target_dir), shell=True, check=True)
        except Exception as ex:
            logging.error('Exception is thrown in subprocess:\ntag: {}\naddress:{}\nexception msg: {}'.format(tag, address, ex))
