import websocket
import json
import socks
import socket
import os
import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Tor setup: Set SOCKS proxy to route through Tor
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# Define application info
app_name = "WebSocket Client"
app_description = "A robust WebSocket client with Tor support for anonymity"
app_developer = "Developed by Dr. Aubrey W. Love II (AKA RoguePayload)"
app_company = "DarkMatrix Cyber Solutions LLC (darkmcs.com)"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    """Get origin and URL with access token from the user."""
    print(Fore.YELLOW + "What is the Origin of the URL? (e.g., https://my.example-app.com)")
    origin = input(Fore.MAGENTA + "Origin: ")

    print(Fore.YELLOW + "What is the URL with Access Token? (e.g., https://my.example-app.com/ws?accessToken=abc123)")
    url = input(Fore.MAGENTA + "URL: ")

    return origin, url

def load_headers(filename):
    """Load headers from a file."""
    with open(filename, 'r') as file:
        headers = json.load(file)
    return headers

def on_message(ws, message):
    print(Fore.GREEN + "Received message:", message)

def on_error(ws, error):
    print(Fore.RED + "Error:", error)

def on_close(ws, close_status_code, close_msg):
    print(Fore.YELLOW + "Connection closed")

def on_open(ws):
    print(Fore.GREEN + "WebSocket connection opened")

def main():
    clear_screen()

    # Display application information
    print(Fore.GREEN + app_name)
    print(Fore.BLUE + app_description)
    print(Fore.YELLOW + app_developer)
    print(Fore.YELLOW + app_company)

    # Get user input for origin and URL
    origin, url = get_user_input()

    # Load headers from a file
    headers_data = load_headers('headers.json')

    # Randomly select a User-Agent from the list
    user_agent = random.choice(headers_data['User-Agents'])

    # Construct headers dictionary
    headers = {
        "User-Agent": user_agent,
        "Origin": origin
    }

    # Enable WebSocket trace for debugging
    websocket.enableTrace(True)

    # Create WebSocket app
    ws = websocket.WebSocketApp(
        url,
        header=[f"{k}: {v}" for k, v in headers.items()],
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    # Run the WebSocket app
    ws.run_forever()

if __name__ == "__main__":
    main()

