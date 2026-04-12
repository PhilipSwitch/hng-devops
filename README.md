# HNG DevOps Stage 0 - Linux Server Configuration & Nginx Deployment

## 🚀 Project Overview

This project demonstrates a production-ready Linux server configuration with Nginx web server, SSL/TLS encryption, and comprehensive security hardening. Built as part of the HNG Internship DevOps Track Stage 0 assessment.

## 🔗 Live Deployment

- **Primary Domain:** [https://mobolaji-babajide.xyz](https://mobolaji-babajide.xyz)
- **API Endpoint:** [https://mobolaji-babajide.xyz/api](https://mobolaji-babajide.xyz/api)

## 🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| **Operating System** | Ubuntu 22.04 LTS (64-bit) |
| **Web Server** | Nginx 1.18+ |
| **SSL/TLS** | Let's Encrypt (Certbot) |
| **Firewall** | UFW (Uncomplicated Firewall) |
| **Cloud Provider** | DigitalOcean |
| **DNS** | Namecheap |

## 📋 Implementation Details

### Server Configuration

#### User Management
- **Primary User:** `hngdevops`
- **Privileges:** Sudo access with passwordless execution for specific commands
- **Passwordless Sudo Scope:** `/usr/sbin/sshd`, `/usr/sbin/ufw` only
- **Authentication:** SSH key-based (password authentication disabled)

#### Security Hardening
- ✅ Root SSH login disabled
- ✅ Password-based SSH authentication disabled
- ✅ Key-based authentication enforced
- ✅ UFW firewall active with whitelist approach
- ✅ Minimal attack surface (only 3 ports exposed)

#### Network Configuration
**Open Ports:**
- `22` - SSH (Secure Shell)
- `80` - HTTP (redirects to HTTPS)
- `443` - HTTPS (Secure web traffic)

**All other ports:** Blocked by default

### Web Endpoints

#### `GET /`
**Description:** Serves static HTML page with HNG username prominently displayed

**Response Type:** `text/html`

**Status Code:** `200 OK`

**Features:**
- Clean, responsive design
- Username clearly visible as text content
- Professional styling

---

#### `GET /api`
**Description:** Returns JSON object with internship metadata

**Response Type:** `application/json`

**Status Code:** `200 OK`

**Response Body:**
```json
{
  "message": "HNGI14 Stage 0",
  "track": "DevOps",
  "username": "Mobolaji-Philip-Babajide"
}
Headers:

Content-Type: application/json
Access-Control-Allow-Origin: * (CORS enabled)
SSL/TLS Implementation
Certificate Authority: Let's Encrypt
Certificate Type: Domain Validated (DV)
Encryption: TLS 1.2/1.3
HTTP to HTTPS Redirect: 301 Permanent Redirect
Auto-Renewal: Enabled via systemd timer
Renewal Frequency: Checked twice daily
Certificate Validity: 90 days (auto-renews at 30 days)
🔍 Verification & Testing
Manual Testing Commands
Bash

# Test HTTPS root endpoint
curl https://mobolaji-babajide.xyz

# Test HTTPS API endpoint
curl https://mobolaji-babajide.xyz/api

# Verify HTTP to HTTPS redirect (should return 301)
curl -I http://mobolaji-babajide.xyz

# Check JSON Content-Type header
curl -I https://mobolaji-babajide.xyz/api | grep "application/json"

# Verify SSL certificate
openssl s_client -connect mobolaji-babajide.xyz:443 -servername mobolaji-babajide.xyz < /dev/null

# Check firewall status
sudo ufw status verbose

# Verify user configuration
id hngdevops
sudo -l -U hngdevops
Browser Testing
Visit https://mobolaji-babajide.xyz - Should display HTML page with padlock icon
Visit https://mobolaji-babajide.xyz/api - Should display JSON response
Visit http://mobolaji-babajide.xyz - Should auto-redirect to HTTPS
Check certificate - Click padlock icon, verify Let's Encrypt issuer
📁 Server File Structure
text

/
├── etc/
│   ├── nginx/
│   │   ├── nginx.conf
│   │   └── sites-available/
│   │       └── default (main config)
│   ├── ssh/
│   │   └── sshd_config (hardened SSH config)
│   ├── letsencrypt/
│   │   └── live/mobolaji-babajide.xyz/
│   │       ├── fullchain.pem
│   │       └── privkey.pem
│   └── ufw/
│       └── (firewall rules)
├── var/
│   └── www/
│       └── html/
│           └── index.html (custom page)
└── home/
    └── hngdevops/
        └── .ssh/
            └── authorized_keys (grading bot key)
🔐 Security Compliance Checklist
 Non-root user created with limited sudo privileges
 Passwordless sudo restricted to specific commands only
 Root SSH login disabled
 Password authentication disabled (SSH keys only)
 UFW firewall enabled and configured
 Only essential ports exposed (22, 80, 443)
 Valid SSL certificate from trusted CA
 HTTPS enforced with 301 redirects
 Proper file permissions on SSH keys and web files
 Nginx running as non-privileged user (www-data)
🎯 Task Requirements Met
Requirement	Status	Notes
Non-root user hngdevops	✅	With sudo privileges
Passwordless sudo for specific commands	✅	/usr/sbin/sshd, /usr/sbin/ufw
Root SSH login disabled	✅	PermitRootLogin no
Password SSH auth disabled	✅	PasswordAuthentication no
UFW active, ports 22/80/443 only	✅	All others denied
Nginx installed and running	✅	Serving on port 80/443
GET / returns HTML with username	✅	Username visible as text
GET /api returns correct JSON	✅	Exact format match
JSON has Content-Type: application/json	✅	Header configured
Username matches HNG registration	✅	Mobolaji-Philip-Babajide
Valid Let's Encrypt SSL	✅	Not self-signed
HTTP→HTTPS redirect is 301	✅	Permanent redirect
Grading bot SSH key added	✅	In authorized_keys
📚 Learning Outcomes
Through this project, I gained hands-on experience with:

Linux system administration and user management
SSH configuration and security hardening
Firewall configuration and network security principles
Nginx web server installation and configuration
SSL/TLS certificate management with Let's Encrypt
DNS configuration and domain management
Server blocks and location directives in Nginx
HTTP/HTTPS protocol understanding
RESTful API endpoint configuration
Security best practices for production servers
👤 Author
Name: Mobolaji Philip Babajide
HNG Username: Mobolaji-Philip-Babajide
Track: DevOps
Stage: 0

🗓️ Project Timeline
Start Date: April 11, 2026
Completion Date: April 12, 2026
Submission Deadline: April 16, 2026
🙏 Acknowledgments
HNG Internship Program
DigitalOcean for cloud infrastructure
Let's Encrypt for free SSL certificates
Nginx and Ubuntu communities
📄 License
This project is part of the HNG Internship assessment and is for educational purposes.

Built with dedication as part of the HNG Internship DevOps Track 🚀
