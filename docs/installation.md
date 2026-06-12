# Installation Guide

## Prerequisites

* Python 3.10 or higher
* Git
* VS Code (Recommended)
* Internet Connection (for ThingSpeak)

---

## Clone Repository

```bash
git clone https://github.com/yourusername/IoT-Smart-Home-Energy-Monitoring-System.git
cd IoT-Smart-Home-Energy-Monitoring-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure ThingSpeak

Open:

```python
python_simulation/thingspeak_uploader.py
```

```python
WRITE_API_KEY = "HRXKXH3APFUKONWP"
```

---

## Run the Project

```bash
python main.py
```

---

## Launch Dashboard

```bash
streamlit run dashboard/streamlit_dashboard.py
```

Open:

```text
http://localhost:8501
```
