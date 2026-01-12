from flask import Flask, render_template
from services.gps_service import get_live_location
from services.traffic_service import traffic_status
from services.delay_predictor import predict_delay

app = Flask(__name__)


@app.route("/")
def dashboard():
    location = get_live_location()
    traffic = traffic_status()
    delay = predict_delay(traffic)
    return render_template("dashboard.html", location=location, traffic=traffic, delay=delay)


@app.route("/alerts")
def alerts():
    alert_message = "No active emergencies"
    return render_template("alerts.html", alert_message=alert_message)


@app.route("/simulate/<event>")
def simulate(event):
    if event == "overspeed":
        alert = "Overspeed detected! Driver warned."
    elif event == "accident":
        alert = "Accident detected! Emergency services notified."
    elif event == "breakdown":
        alert = "Bus breakdown! Alternate bus dispatched."
    else:
        alert = "System running normally."

    return render_template("alerts.html", alert_message=alert)


if __name__ == "__main__":
    app.run(debug=True)
