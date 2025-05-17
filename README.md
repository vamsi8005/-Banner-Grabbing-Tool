
# Banner Grabbing Port Scanner

A Python tool that scans a range of TCP ports on a target machine, detects open and closed ports, and grabs service banners or version information where available.

## 🔧 How It Works

- User inputs target IP address and maximum port number to scan.
- The tool attempts to connect to each port within the range.
- For open ports, it tries to read any immediate banner sent by the service.
- For common HTTP ports, it sends an HTTP GET request to fetch server response headers.
- Displays port status (open/closed) along with any banner or version information received.

## 🚀 Skills Used

- Python socket programming
- Network reconnaissance techniques
- Service banner grabbing
- Basic HTTP protocol
- Error and exception handling

## 🛠️ Usage

1. Run the script:

   ```bash
   python banner_grabber.py
