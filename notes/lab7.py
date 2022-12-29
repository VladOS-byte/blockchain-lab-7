import sys
from crc import Calculator, Configuration
import numpy as np
import pandas as pd

file = sys.argv[1]

numticket = int(sys.argv[2])

par = int(sys.argv[3])

data = pd.read_csv(file, header=None)

# CRC32
config = Configuration(
    width=256,
    polynomial=0x07,
    init_value=0x00,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

calculator = Calculator(config)

data['crc'] = data[0].map(lambda x: calculator.checksum(bytes(map(lambda y: y + par, x.encode('utf-8')))))

data['ticket'] = data['crc'].map(lambda x: (x % numticket) + 1)

for i in range(len(data)):
    print(str(data[0][i]) + ': ' + str(data['ticket'][i]))
