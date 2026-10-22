# IPv4 Information Application

## Description
This Python application retrieves and displays the current public IPv4 addressing information of the user's computer. It uses the `ipinfo.io` API to gather geolocation, ISP, and timezone data, and uses the `rich` library to format the output into a clean, colorful terminal table.

## How to Run
1. Ensure Python is installed.
2. Create and activate a virtual environment: `python -m venv venv`
3. Activate it (Windows): `.\venv\Scripts\Activate`
4. Install dependencies: `pip install requests rich`
5. Run the app: `python ip_info.py`

## Why we chose these features
We chose a colored table output (using `rich`) to make the data much more readable for network technicians compared to raw JSON output. We chose `ipinfo.io` because it provides reliable geolocation and ISP data on a free tier without requiring an API key.