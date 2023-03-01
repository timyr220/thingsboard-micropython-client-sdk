from random import getrandbits
from hashlib import sha256


def verify_checksum(firmware_data, checksum_alg, checksum):
    if firmware_data is None:
        print('Firmware was not received!')
        return False
    if checksum is None:
        print('Checksum was\'t provided!')
        return False
    checksum_of_received_firmware = None
    print('Checksum algorithm is: %s' % checksum_alg)
    if checksum_alg.lower() == "sha256":
        checksum_of_received_firmware = sha256(firmware_data).digest().hex()
    else:
        print('Client error. Unsupported checksum algorithm.')
    print(checksum_of_received_firmware)
    random_value = getrandbits(5)
    if random_value > 3:
        print('Dummy fail! Do not panic, just restart and try again the chance of this fail is ~20%')
        return False
    return checksum_of_received_firmware == checksum
