🚍 Campus Transport & Bus Tracking System

---

• Project Overview-

The Campus Transport & Bus Tracking System is a web-based application developed using Python and Flask to monitor and manage campus bus transportation in real time.
The system provides live bus location updates, traffic condition monitoring, delay prediction, and simulation of emergency scenarios such as overspeeding, accidents, and bus breakdowns.
This project is designed to demonstrate how modern software systems can improve campus safety, efficiency, and transport management, while being scalable for real-world deployment with actual GPS and sensor data.

--- 

 • Objectives-

To track campus buses using simulated real-time GPS data
To monitor traffic conditions and predict delays
To detect and simulate unsafe or emergency events
To provide a centralized dashboard for transport monitoring
To design a modular and scalable backend architecture

---

• Key Features-

🚍 Live Bus Tracking (Latitude & Longitude simulation)
🚦 Traffic Condition Analysis (Clear / Moderate / Heavy)
⏱ Delay Prediction based on traffic conditions
⚠ Event Simulation
Overspeed detection
Accident detection
Bus breakdown handling
📊 Dashboard Interface for monitoring system status
🧪 Simulation Endpoints for controlled demonstrations
🧱 Modular backend design using services

---

• Technologies Used-

Programming Language: Python 3
Web Framework: Flask
Frontend: HTML, CSS (Jinja Templates)
Database: SQLite (campus.db)
IDE: Visual Studio Code

---

• Project Structure

 CAMPUS_TRANSPORT_SYSTEM/
│
├── app.py                    # Main Flask application (entry point)
├── config.py                 # Application configuration
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── venv/                     # Virtual environment
│
├── database/                 # Database layer
│   ├── campus.db             # SQLite database file
│   └── db_helper.py          # Database helper functions
│
├── models/                   # Data models
│   ├── __init__.py
│   ├── bus.py                # Bus-related data model
│   ├── driver.py             # Driver-related data model
│   ├── incident.py           # Incident data model
│   └── route.py              # Route data model
│
├── services/                 # Core business logic
│   ├── __init__.py
│   ├── gps_service.py        # GPS location simulation
│   ├── traffic_service.py    # Traffic condition analysis
│   ├── delay_predictor.py    # Delay prediction logic
│   ├── speed_monitor.py      # Overspeed monitoring
│   └── emergency_security.py # Emergency & safety handling
│
├── security/                 # Security-related logic
│   ├── __init__.py
│   └── campus_security.py    # Campus security integration
│
├── templates/                # HTML templates
│   ├── dashboard.html        # Main dashboard UI
│   └── alerts.html           # Alerts & simulation UI
│
└── static/                   # Static files
    └── style.css             # CSS styling

---

• How the System Works?

The Flask server is started using app.py
GPS service simulates live latitude and longitude values
Traffic service generates traffic conditions dynamically
Delay predictor calculates expected delays based on traffic
Flask routes render data on the dashboard using HTML templates
Simulation routes trigger alerts for emergency scenarios

---

• How to Run the Project?

1️⃣ Install Dependencies
Bash:
pip install -r requirements.txt
2️⃣ Run the Application
Bash:
python app.py
3️⃣ Open in Browser
http://127.0.0.1:5000/

---

• Simulation Routes

These routes simulate real-world transport incidents:
Overspeed Detection
/simulate/overspeed
Accident Detection
/simulate/accident
Bus Breakdown
/simulate/breakdown

---

• Dashboard Features

Displays live bus coordinates
Shows current traffic condition
Indicates system operational status
Provides links for emergency simulations

---

• Security & Safety Considerations

Modular service-based architecture for better isolation
Simulation-based alerts to prevent false real-world triggers
Designed for future integration with campus security systems

---

• Future Enhancements-

Integration with real GPS devices
Real-time map visualization using Google Maps API
SMS / Email notifications for alerts
Driver behavior analytics using IoT sensors
Admin and user authentication system
Mobile application support

---

• Learning Outcomes-

Practical understanding of Flask framework
Modular Python application design
Backend–Frontend integration
Debugging real-time runtime errors
Web-based system deployment fundamentals

---

• Author-

Project Title: Campus Transport & Bus Tracking System
Developed By: Varshini V
Department: Computer Science & Engineering
Project Type: Major Project

---

• Conclusion

This project demonstrates a practical approach to solving real-world campus transportation challenges using Python and Flask. The system is scalable, modular, and designed with future real-time integrations in mind, making it suitable for both academic and real-world applications.