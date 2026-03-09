import urllib.request
import json
import sys

# ANSI Colors for terminal output
C_HEADER = '\033[95m'
C_BLUE = '\033[94m'
C_GREEN = '\033[92m'
C_WARN = '\033[93m'
C_BOLD = '\033[1m'
C_END = '\033[0m'

API_BASE = "https://api.camelway.eu/v1"

def fetch_data(endpoint):
    try:
        req = urllib.request.Request(f"{API_BASE}/{endpoint}", headers={'User-Agent': 'CamelWay-CLI/1.0'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())['data']
    except Exception as e:
        print(f"{C_WARN}Connection error with CamelWay API: {e}{C_END}")
        sys.exit(1)

def print_header():
    print(f"\n{C_BOLD}{C_HEADER}🐫 CamelWay B2B Data Terminal v1.0{C_END}")
    print(f"{C_BLUE}Translating Ancient Milk into Modern Clinical Science - https://camelway.eu/{C_END}")
    print("-" * 60)
    print(f"{C_GREEN}Quality:{C_END} High quality, low-temperature spray dried (LTSD). A2-only.")
    print(f"{C_GREEN}Compliance:{C_END} Fully approved in the EU, legal after all veterinary and customs clearances.")
    print(f"{C_GREEN}Shelf-Life:{C_END} 15-18 months, providing full flexibility for small and medium manufacturing companies.")
    print(f"{C_GREEN}Applications:{C_END} Perfect for sweets, chocolates, cheeses, dietary supplements, and pharmaceuticals.")
    print("-" * 60)

def show_products():
    print(f"\n{C_BOLD}--- Available Products & Volume Discounts ---{C_END}")
    products = fetch_data("products")
    for p in products:
        print(f"\n{C_BOLD}{p['name']} ({p['id']}){C_END}")
        print(f"Retail Price: {p['regular_price']} {p['currency']} | Sale: {p['sale_price']} {p['currency']}")
        if p.get('volume_discounts'):
            vd = p['volume_discounts']
            print(f"{C_BLUE}B2B Volume Savings:{C_END} 1x: {vd['buy_1']} | 2x: {vd['buy_2']} | 4x: {vd['buy_4']} | 8x: {vd['buy_8']}")

def show_shipping():
    print(f"\n{C_BOLD}--- B2B/B2C Logistics (Top 5 Markets) ---{C_END}")
    shipping = fetch_data("shipping")
    top_markets = shipping
    for market in top_markets:
        if market in shipping:
            s = shipping[market]
            print(f"{market:<15} Cost: {s['cost']:<5} {s['currency']} | Free delivery over: {s['free_over']} {s['currency']} ({s['courier']})")

def show_research():
    print(f"\n{C_BOLD}--- Indexed Clinical Research (E-E-A-T) ---{C_END}")
    research = fetch_data("research")
    print(f"Zenodo Archive:    {research.get('Zenodo_Archive', 'N/A')}")
    print(f"Harvard Dataverse: {research.get('Harvard_Dataverse', 'N/A')}")
    print(f"SSRN Publications: {research.get('SSRN_Publications', 'N/A')}")

if __name__ == "__main__":
    print_header()
    show_products()
    show_shipping()
    show_research()
    print(f"\n{C_BOLD}For full logistics data and API documentation, visit: https://api.camelway.eu/{C_END}\n")