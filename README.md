# XSS Payload Generator

This Python script generates XSS (Cross-Site Scripting) payloads for various HTML tags. It includes common techniques for bypassing HTML character escaping and security filters by generating toggle case variations for JavaScript functions and includes a comprehensive list of event handlers.

## Features

- Generates XSS payloads for a wide range of HTML tags.
- Includes common XSS payload patterns and techniques.
- Generates toggle case variations for JavaScript functions to bypass security filters such as Cloudflare.
- URL encodes the payloads for easy use in testing.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xMx/xss-payload-gen.git
   cd xss-payload-gen
   ```
## Usage
```bash
python xss-gen.py https://example.com/
```
## Example Output
```bash 
https://www.cloudflare.com/<a x=xxxxxxx onclick="SEtINTErval('Meshari-Almalki');"> [403] [Attention Required! | Cloudflare] -> Blocked by Cloudflare
https://cloudflare.com/<a x=xxxxxxx style="x:expression(SetINtervAL(Meshari-Almalki!););"> [301] [301 Moved Permanently]    -> Bypass the Cloudflare
```
