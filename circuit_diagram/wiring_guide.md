# Smart Home Energy Monitoring System - Wiring Guide

## ESP32 Connections

| Component          | ESP32 Pin |
| ------------------ | --------- |
| ACS712 OUT         | GPIO34    |
| Voltage Sensor OUT | GPIO35    |
| Green LED          | GPIO18    |
| Yellow LED         | GPIO19    |
| Red LED            | GPIO21    |
| Buzzer             | GPIO25    |
| Relay IN           | GPIO26    |

---

## Power Connections

### ACS712

* VCC → 3.3V
* GND → GND
* OUT → GPIO34

### Voltage Sensor

* VCC → 3.3V
* GND → GND
* OUT → GPIO35

### LEDs

* Green LED → GPIO18
* Yellow LED → GPIO19
* Red LED → GPIO21

### Buzzer

* Positive → GPIO25
* Negative → GND

### Relay Module

* IN → GPIO26
* VCC → 5V
* GND → GND

---

## Working Principle

1. ACS712 measures current consumption.
2. Voltage Sensor measures supply voltage.
3. ESP32 calculates power and energy consumption.
4. Data is uploaded to ThingSpeak via WiFi.
5. CSV logs and PDF reports are generated.
6. Alerts are triggered for high power consumption.

---

## Formulae Used

Power (W) = Voltage × Current

Energy (kWh) = Power × Time / 1000

Cost = Energy × Tariff

---

## Alert Conditions

* Normal: < 1000W
* Medium Usage: 1000W – 1999W
* High Usage: ≥ 2000W
