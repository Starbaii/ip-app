import requests
from rich.console import Console
from rich.table import Table

def get_ip_info():
    """Fetch public IP information from ipinfo.io."""
    try:
        # ipinfo.io free endpoint (no API key required for basic usage)
        response = requests.get("https://ipinfo.io/json", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP info: {e}")
        return None

def display_ip_info(data):
    """Display IP information in a formatted table."""
    if not data:
        print("No data to display.")
        return

    console = Console()
    table = Table(title="Public IP Information", show_header=True, header_style="bold magenta")

    table.add_column("Field", style="cyan", width=20)
    table.add_column("Value", style="green")

    # Updated fields for ipinfo.io API
    fields = [
        ("IP Address", data.get("ip", "N/A")),
        ("City", data.get("city", "N/A")),
        ("Region", data.get("region", "N/A")),
        ("Country", data.get("country", "N/A")),
        ("Postal Code", data.get("postal", "N/A")),
        ("Location (Lat,Lon)", data.get("loc", "N/A")),
        ("Timezone", data.get("timezone", "N/A")),
        ("ISP / Org", data.get("org", "N/A")),
    ]

    for field, value in fields:
        table.add_row(field, str(value))

    console.print(table)

if __name__ == "__main__":
    print("Fetching your public IP information...\n")
    info = get_ip_info()
    display_ip_info(info)