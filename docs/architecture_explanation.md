# System Architecture Explanation

## Overview

The Smart Home Energy Monitoring System is an IoT-based solution designed to monitor household energy consumption, estimate electricity costs, generate alerts, and provide analytics through cloud and dashboard platforms.

---

## Architecture

Smart Appliances
↓
Energy Consumption Simulation
↓
ESP32 / Python Digital Twin
↓
Energy Processing Engine
↓
ThingSpeak Cloud
↓
CSV Logging
↓
Graph Generation
↓
PDF Reports
↓
Streamlit Dashboard

---

## Layer 1: Appliance Layer

The system simulates energy consumption from common household appliances such as:

* LED Bulb
* Fan
* Television
* Refrigerator
* Laptop
* Air Conditioner
* Water Heater
* Washing Machine

Each appliance has a predefined power rating.

---

## Layer 2: Processing Layer

The ESP32 or Python Simulator performs:

* Voltage Monitoring
* Current Monitoring
* Power Calculation
* Energy Calculation
* Cost Estimation
* Alert Detection

---

## Layer 3: Cloud Layer

ThingSpeak stores energy data in the cloud.

Stored Parameters:

* Voltage
* Current
* Power
* Energy
* Cost
* Alert Status

---

## Layer 4: Analytics Layer

The Streamlit dashboard visualizes:

* Live Energy Usage
* Cost Trends
* Energy Trends
* Historical Data
* Appliance Status

---

## Layer 5: Reporting Layer

The system automatically generates:

* CSV Logs
* Daily Usage Reports
* Monthly Usage Reports
* PDF Reports
* Energy Charts

---

## Benefits

* Energy Optimization
* Cost Reduction
* Data Analytics
* Smart Home Automation Foundation
* Real-Time Monitoring
