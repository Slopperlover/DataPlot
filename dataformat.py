from enum import Enum

class Datafromat(Enum):
    VESC_motor_driver = [
    "Datalogger port",
    "Dataloggertijd, in s",
    "Format header",
    "Tijd sinds boot, in s",
    "Ingangsspanning meetsysteem, in V",
    "Temperatuur meetsysteem, in graden Celsius",
    "Tijd dat het laatste geldige VESC-packet is binnengekomen, in s",
    "Temperatuur van de VESC driver, in graden Celsius",
    "Temperatuur van de motor, in graden Celsius",
    "Motorstroom in A",
    "Ingangsstroom VESC, in A",
    "Huidige duty cycle, fractie tussen 0 en 1",
    "Huidige RPM van de motoras, in 1/min",
    "Ingangsspanning VESC",
    "Energie afgegeven door de VESC sinds boot, in Wh",
    "VESC foutcode",
    "Aantal gemiste startbytes in de VESC-communicatie",
    "Aantal keren dat de payload te groot was voor de buffer",
    "Aantal keren dat een END-byte onverwacht ontbrak",
    "Aantal gedetecteerde CRC-fouten",
    "Aantal onbekende packets",
    "Aantal keren dat er meer of minder velden dan verwacht in een packet zaten",
    "GPS longitude, in graden",
    "GPS latitude, in graden",
    "GPS direction",
    "GPS speed, in km/h",
    "GPS time, in seconden sinds het begin van de huidige GPS-week"
]