# HomeOS


## Architecture
To run the app we need to start 2 systemd services.
- **cloudflared**.service: With this service we connect to cloudflare to host our app via a public domain
- **homeos**.service: This is the streamlit app running on port 8001. Make sure to start the app only on this port, because it is connected to the cloudflare tunnel.

## Installation

## Restart
```
sudo systemctl restart homeos.service
```

## Troubleshooting
1. **List all services**: Check is services are running (Exit with: Q)
```
systemctl list-units --type=service
```
2. **Check Status of Service**
```
systemctl systemctl status homeos.service
```# homeOS
