# Pulse Review Scraper

# Objective

The objective of this assignment is to build a script that extracts product reviews for SaaS companies from multiple sources over a specified time period and outputs them in a structured JSON format.

Since direct scraping of platforms like G2 and Capterra is restricted due to bot protection and legal policies, this implementation uses a CSV-based data source to simulate real-world review data while maintaining the same input, filtering, and output behavior required by the assignment.


# Features

Accepts company name, source, start date, and end date as input parameters.

Supports multiple review platforms:

G2

Capterra

TrustRadius (bonus source)

Filters reviews based on:

Company name

Source

Date range

Outputs reviews into a clean and structured reviews.json file.

Handles invalid or out-of-range inputs gracefully.

# Usage

Run the script using the following command format:
```bash
python scraper.py --company <company> --start <YYYY-MM-DD> --end <YYYY-MM-DD> --source <source>
```
# Example:
```bash
python scraper.py --company hubspot --start 2023-12-01 --end 2024-03-31 --source g2
```


## Installation

```bash
pip install -r requirements.txt




