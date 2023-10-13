# reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0) 
RESET_PIN = 0 # Green OUT
SDA_PIN = 1 # Yellow OUT but used a Chip Select CS 
SCK_PIN = 2 # Orange OUT clock going from Pico to RC522
MISO_PIN = 3 # Blue 
MOSI_PIN = 4 # Purple
IRQ_PIN = 7 # Brown, OUT but not used in the reader demo

# GND is Black
# Red goes to 3.3v out