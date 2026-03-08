# Instagram Non-Followers Finder

A Python automation tool that finds Instagram accounts you follow that do not follow you back.

## Features
- Fetch followers list
- Fetch following list
- Compare both lists
- Display accounts not following back

## Requirements
- Python 3.8+
- Instaloader library

## Installation

pip install -r requirements.txt

## Usage

1. Login once using:

instaloader --login YOUR_USERNAME

2. Run the script:

python3 insta_not_following.py

3. Enter your Instagram username.

The script will display accounts that do not follow you back.

## Disclaimer
This project uses Instagram's public endpoints via Instaloader. Excessive requests may trigger rate limits.