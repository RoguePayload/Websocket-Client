# WebSocket Client with Tor Support

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/repo-name)
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/repo-name)
![GitHub stars](https://img.shields.io/github/stars/yourusername/repo-name?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/repo-name?style=social)

A robust WebSocket client that includes Tor support for anonymity. This client allows users to establish secure and anonymous WebSocket connections with customizable headers and user-agent strings.

## Features

- **Tor Support**: Provides anonymity for WebSocket connections.
- **User-Defined Headers**: Customize headers to suit specific needs.
- **Multiple User-Agent Strings**: Support for various devices and platforms.
- **Interactive User Input**: User-friendly interface for entering URL and Origin.
- **Logging and Debugging**: Detailed logs for debugging purposes.
- **Secure WebSocket Connections**: Ensures secure communication using WebSocket protocols.

## Installation

1. **Clone the Repository**

```
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```
2. **Install Dependencies**
```
pip install -r requirements.txt
```
## Usage
1. **Start the Tor Service:**
_On Linux:_
```
sudo service tor start
```
_On MacOS_
```
brew services start tor
```
_On Windows_
```
Run the Client
```

2. **Run the WebSocket Client**
```
python websocket_client.py
```

3. **Enter the Required Information**
 * `Origin:` _The origin of the URL in question._ (e.g., `https://app.my-app.com')  
 * `URL:` _The full URL with the access token._ (e.g., `wss://app.my-app.com/documents/abc123/ws?accessToken=xyz123`)  

4. **Follow On-Screen Instructions**
The application will guide you through establishing a connection and handling the WebSocket communication.

## Configuration
 * Headers Configuration:
   * _The `headers.json` file contains various headers and user-agent strings. You can customize or add more user-agents as needed._
```
{
    "User-Agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36"
    ],
    "Headers": {
        "Custom-Header": "YourValueHere"
    }
}
```
 * Tor Configuration:
   _Ensure your system is configured to route connections through Tor. This can be verified by checking your IP address or using the Tor browser for initial configuration._

## Contact
**Dr. Aubrey W. Love II (AKA Rogue Payload)**
 * Email: [alove@darkmcs.com](mailto:alove@darkmcs.com) | [roguepayload@darkmcs.com](mailto:roguepayload@darkmcs.com)  
 * Web: [DarkMatrix Cyber Solutions LLC](https://www.darkmcs.com)  
_Feel free to reach out with any questions, feedback, or contributions._
