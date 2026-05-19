# E-Commerce Competitor Price Monitor & Data Scraper

A lightweight, automated Python tool designed to monitor competitor product pricing, availability, and catalog updates. This project demonstrates a production-ready web scraping pipeline that extracts unstructured HTML data and converts it into a clean, structured business intelligence report (CSV/Excel).

## 📌 Project Overview & Business Case

In e-commerce, staying competitive requires real-time pricing strategy updates. This project simulates a real-world freelance request where an e-commerce coffee brand owner needed to monitor a key competitor's catalog weekly.

The script extracts the following key data points:
- **Product Name:** Identifying the specific product item.
- **Current Price:** Tracking pricing changes over time.
- **Stock Status:** Monitoring inventory availability (`In Stock` / `Out of Stock`).
- **Product URL:** Direct links for automated reference or deep-diving.

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3.10+
- **Parser Engine:** Beautiful Soup 4 (Optimized for high-speed, static HTML parsing)
- **Data Manipulation:** Pandas (For data structuring, indexing management, and clean CSV pipelines)

The pipeline is structured as follows:
1. Fetching/Simulating target web page DOM tree.
2. Initializing `BeautifulSoup` object with the standard HTML parser.
3. Node iteration over generic product container classes (`.product-card`).
4. Data normalization (whitespace trimming, absolute URL generation).
5. Schema construction via tabular Pandas DataFrames and multi-encoding export (`utf-8`).

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your local machine.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/otuncel/e-commerce-price-monitor-data-scraper.git
   cd e-commerce-price-monitor-data-scraper
