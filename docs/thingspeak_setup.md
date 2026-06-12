# ThingSpeak Setup Guide

## Create Account

Visit:

https://thingspeak.com

Create a free MathWorks account.

---

## Create Channel

Channel Name:

Smart Home Energy Monitoring System

---

## Create Fields

Field 1 → Voltage

Field 2 → Current

Field 3 → Power

Field 4 → Energy

Field 5 → Cost

Field 6 → Alert Status

---

## Save Channel

After creating the channel, open:

Channels → API Keys

Copy the Write API Key.

---

## Configure Project

Open:

python_simulation/thingspeak_uploader.py

```python
WRITE_API_KEY = "HRXKXH3APFUKONWP"
```

---

## Verify Data Upload

Run:

```bash
python main.py
```

Refresh ThingSpeak dashboard.

Graphs should start updating automatically.
