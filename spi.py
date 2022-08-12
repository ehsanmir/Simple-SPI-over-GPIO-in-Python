import configparser
import json
from lib import gpio
from time import sleep

# get required variables from the config file
config = configparser.ConfigParser()
config.read("config.ini")
pins = json.loads(config.get("GPIO", "SPI"))

# export gpio pins (in some cases need: chmod 600 /sys/class/gpio/export)
pinCLK = gpio.GPIOPin(pins[0], gpio.OUT) # Serial Clock (output from master)
pinSDO = gpio.GPIOPin(pins[1], gpio.IN)  # Master In Slave Out (data output from slave)
pinSDI = gpio.GPIOPin(pins[2], gpio.OUT) # Master Out Slave In (data output from master)
pinDAV = gpio.GPIOPin(pins[3], gpio.IN)  # Data Available (optional, output from slave)
pinCS = gpio.GPIOPin(pins[4], gpio.OUT)  # Chip/Slave Select (often active low, output from master)

# idle phase
pinCLK.write(gpio.LOW)
pinSDI.write(gpio.LOW)
pinCS.write(gpio.HIGH)


def clkDelay():
    """
    description: function to create required delays for SPI clock signals.
    """
    for i in range(3):
        continue


def readSPI(readLen):
    """
    description: function to read data from SPI's SDO pin.
    arguments:
        readLen (mandatory):
            description: the length of the data that we want to read, in bits not bytes.
            type: int
            example: 8
    returns:
        description: the binary data that we want, or empty string when failure.
        type: str
        example: '10111010'
    """
    buff = ""
    try:
        pinCS.write(gpio.LOW)
        for i in range(readLen):
            clkDelay()
            pinCLK.write(gpio.LOW)
            clkDelay()
            pinCLK.write(gpio.HIGH)
            buff += str(pinSDO.read())
        clkDelay()
        # idle phase
        pinCLK.write(gpio.LOW)
        pinSDI.write(gpio.LOW)
        pinCS.write(gpio.HIGH)
    except:
        return ""
    return buff


def writeSPI(data):
    """
    description: function to write data on SPI's SDI pin.
    arguments:
        data (mandatory):
            description: the hex data that we want to send to the SPI slave
            type: str
            example: 'f01b33ea'
    returns:
        description: writing was successful or not.
        type: bool
        example: True
    """
    binaryData = ''
    for i in range(len(data)):
        binaryData += bin(int(data[i], 16))[2:].zfill(4)
    try:
        pinCS.write(gpio.LOW)
        for i in range(len(binaryData)):
            clkDelay()
            if binaryData[i] == "1":
                pinSDI.write(gpio.HIGH)
            else:
                pinSDI.write(gpio.LOW)
            pinCLK.write(gpio.LOW)
            clkDelay()
            pinCLK.write(gpio.HIGH)
        clkDelay()
        # idle phase
        pinCLK.write(gpio.LOW)
        pinSDI.write(gpio.LOW)
        pinCS.write(gpio.HIGH)
    except:
        return False
    return True


if __name__ == "__main__":
    # EXAMPLE USAGE CODE:
    # send some data to SPI bus
    writeSPI('f01b33ea')
    for i in range(60):
        # we check the data available pin to see if the slave has data for us or not
        if pinDAV.read():
            print(readSPI(32))
            break
        sleep(1)
