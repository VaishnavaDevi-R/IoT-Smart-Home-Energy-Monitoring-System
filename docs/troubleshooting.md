# Troubleshooting Guide

## Problem: Module Not Found

### Error

ModuleNotFoundError

### Solution

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Problem: ThingSpeak Not Updating

### Possible Causes

* Incorrect API Key
* No Internet Connection
* Wrong Channel Fields

### Solution

Verify:

```python
WRITE_API_KEY = "HRXKXH3APFUKONWP"
```

---

## Problem: CSV File Not Generated

### Cause

Project execution stopped before logging.

### Solution

Run:

```bash
python main.py
```

Check:

data/energy_logs.csv

---

## Problem: PDF Report Not Generated

### Cause

ReportLab missing.

### Solution

```bash
pip install reportlab
```

---

## Problem: Graphs Not Generated

### Cause

Missing matplotlib package.

### Solution

```bash
pip install matplotlib
```

---

## Problem: Dashboard Not Opening

### Solution

Run:

```bash
streamlit run dashboard/streamlit_dashboard.py
```

Open:

http://localhost:8501

---

## Problem: Empty Dashboard

### Cause

No energy logs available.

### Solution

Run:

```bash
python main.py
```

Generate records first.

---

## Problem: GitHub Images Not Showing

### Cause

Incorrect image path.

### Solution

Use:

```markdown
![Architecture](images/architecture.png)
```

instead of local computer paths.
