# XSS Payload Generator

This Python script generates XSS (Cross-Site Scripting) payloads for various HTML tags. It includes common techniques for bypassing HTML character escaping and security filters by generating toggle case variations for JavaScript functions and includes a comprehensive list of event handlers.

## Features

- Generates XSS payloads for a wide range of HTML tags.
- Includes common XSS payload patterns and techniques.
- Generates toggle case variations for JavaScript functions to bypass security filters.
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
Before running the script, you should replace {base_url} with any website to test the payload on.
```bash
python generate_xss_payloads.py
```
