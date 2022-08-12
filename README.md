# SPI over GPIO
The Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems. 
A general-purpose input/output (GPIO) is an uncommitted digital signal pin on an integrated circuit or electronic circuit board which may be used as an input or output, or both, and is controllable by software.

The SPI bus specifies four logic signals:
1. SCLK: Serial Clock (output from master)
2. MOSI(SDI): Master Out Slave In (data output from master)
3. MISO(SDO): Master In Slave Out (data output from slave)
4. CS /SS: Chip/Slave Select (often active low, output from master to indicate that data is being sent)

![SPI BUS](https://dlnware.com/sites/dlnware.com/files/images/spi_single_slave.png)

## Usage
Using of these codes in your project is super easy:
1. Select 4 gpio pins from the board and connect to the SPI device. You also have to connect VCC and GND pins and optionally the DAV pin.
2. Clone the project files:
```
git clone https://github.com/ehsanmir/Simple-SPI-over-GPIO-in-Python
```
2. Import selected pins in the config.ini file.

3. Now you can run something like this: 

```
from spi import *

writeSPI('f01b33ea')
print(readSPI(32))
```

## Author
* **Ehsan Mir** - *Initial work* - [ehsanmir](https://github.com/ehsanmir)
* email: ehsanmiir@gmail.com

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
