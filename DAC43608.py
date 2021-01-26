import busio
import board
from adafruit_bus_device.i2c_device import I2CDevice

# Standard mode (100 kbps)
# Fast mode (400 kbps)
# Fast+ mode (1.0 Mbps)
#
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
# | MSB | ... | LSB | ACK | MSB | ... | LSB | ACK | MSB | ... | LSB | ACK | MSB | ... | LSB | ACK |
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
# | Address (byte)  |     | Command byte    |     | MSDB            |     | LSDB            |     |
# +-----------------+-----+-----------------+-----+-----------------+-----+-----------------+-----+
# | DB [32:24]      |     | DB [23:16]      |     | DB [15:8]       |     | DB [7:0]        |     |
# +-----------------+-----+-----------------+-----+-----------------+-----+-----------------+-----+
#

# Vout = (DACn_DATA / (2^N)) * Vref
#   N = resolution in bits (8 for DAC43608)
#   DACn_DATA decimal equivalent to binary code loaded into DAC reg
#   DACn_DATA ranges from 0 to 2^N - 1

# DAC43608 Data Byte (MSDB and LSDB)

# DACn_DATA Register Field
# B15 - B12 Don't Care
# B11 - B2  DACn_DATA[7:0]
#  B1 - B0  Don't Care

class DAC43608:

    i2c = None

    # DAC43608 Command Byte
    # Controls which command is executed and which is being accessed.
    # TI 8.5.4 pg 27
    # Byte:   B23 - B16
    __DAC43608_DEVICE_CONFIG = 1
    __DAC43608_STATUS        = 2
    __DAC43608_BRDCAST       = 3
    __DAC43608_DACA_DATA     = 8
    __DAC43608_DACB_DATA     = 9
    __DAC43608_DACC_DATA     = 10
    __DAC43608_DACD_DATA     = 11
    __DAC43608_DACE_DATA     = 12
    __DAC43608_DACF_DATA     = 13
    __DAC43608_DACG_DATA     = 14
    __DAC43608_DACH_DATA     = 15


    def __init__(self, address=0x49):
        comm_port = busio.I2C(board.SCL, board.SDA)
        self.i2c = I2CDevice(comm_port, address)


    def write_dac(self, command, data):
        buffer_ = bytearray([command, *data])
        self.i2c.write()
        return

    def write_config(self, config_byte):
        self.write_dac(self.__DAC43608_DEVICE_CONFIG, config_byte)
        return

    def write_dac_A(self, DACn_DATA):
        """
        DACn_DATA is an array of two bytes/integers, ex: [0x08, 0x04] or [15, 20]
        """
        self.write_dac(self.__DAC43608_DACA_DATA, DACn_DATA)
        return

    def write_dac_B(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACB_DATA, DACn_DATA)
        return

    def write_dac_C(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACC_DATA, DACn_DATA)
        return

    def write_dac_D(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACD_DATA, DACn_DATA)
        return

    def write_dac_E(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACE_DATA, DACn_DATA)
        return

    def write_dac_F(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACF_DATA, DACn_DATA)
        return

    def write_dac_G(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACG_DATA, DACn_DATA)
        return

    def write_dac_H(self, DACn_DATA):
        self.write_dac(self.__DAC43608_DACH_DATA, DACn_DATA)
        return