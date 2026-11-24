# AppSumo Lifetime Deals & Software Scraper (Showcase Mirror)

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-orange.svg)](https://apify.com/moneygain/appsumo-deals-scraper)
[![Pricing](https://img.shields.io/badge/Pricing-Pay--Per--Event%20($0.005)-blue.svg)](https://apify.com/moneygain/appsumo-deals-scraper)
[![RAM](https://img.shields.io/badge/Memory-128%20MB-success.svg)](https://apify.com/moneygain/appsumo-deals-scraper)
[![Zero Browser](https://img.shields.io/badge/Zero--Browser-curl__cffi-brightgreen.svg)](https://apify.com/moneygain/appsumo-deals-scraper)

**Scrape AppSumo software lifetime deals (LTD), AI tools, SaaS pricing, discounts, and customer reviews to structured JSON, CSV, or Excel in seconds without headless browser overhead.**

Run directly on [Apify Store](https://apify.com/moneygain/appsumo-deals-scraper) or call programmatically via the Python client wrapper in this repository.

---

## ⚡ Why Choose Our AppSumo Deals Scraper?

| Metric / Feature | Traditional Playwright / Puppeteer Scrapers | **AppSumo Deals Scraper (Our Actor)** |
| :--- | :--- | :--- |
| **Execution Speed** | 15 – 30 seconds per page | **< 0.3 seconds per query** (Instant `__NEXT_DATA__` SSR Extraction) |
| **Memory Footprint** | 2 GB – 4 GB RAM per run | **128 MB RAM** (Zero headless browser overhead) |
| **Pricing Model** | Expensive platform compute charges ($0.08+/run) | **Pay-Per-Event ($0.005 / record)** — Pay only for real data |
| **Data Cleanliness** | Fragile DOM scraping & frequent nulls | **100% Typed SSR Data** (Zero nulls on core pricing & category fields) |
| **AI / MCP Native** | Heavy unparsed HTML | **Optimized for Cursor, Claude Desktop & n8n** |

---

## 📋 Sample JSON Output

```json
{
  "name": "LeadOcean",
  "slug": "leadocean",
  "description": "Unlimited GTM data API for 996M people and 73M companies",
  "price": 49.0,
  "originalPrice": 1164.0,
  "discountPercentage": 95.8,
  "category": "Lead Generation",
  "group": "Sales & Leads",
  "subcategory": "Cold Email",
  "productUrl": "https://appsumo.com/products/leadocean/",
  "imageUrl": "https://appsumo2-cdn.appsumo.com/media/deals/images/leadocean-hero-996m_8CooRSR.jpg",
  "logoUrl": "https://appsumo2-cdn.appsumo.com/media/deals/images/5b52f0ff-9253-4196-9718-7cf991717671_uuid_616f0140-d258-4b3b-86b8-5a3635c84cb7.jpeg",
  "reviewsSummary": "Customers appreciate LeadOcean, praising its extensive database of 996M people and 73M companies...",
  "query": "ai",
  "scrapedAt": "2026-11-24T11:15:00.000Z"
}
```

---

## 🚀 Quick Start (Python Client)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Apify API Token:
```bash
export APIFY_TOKEN="your_apify_token_here"
```

3. Run extraction:
```bash
python run.py
```

---

## 🎯 Key Use Cases

1. **SaaS Lifetime Deals Tracking & Bargain Alerts**: Discover 90%+ discounted lifetime software deals before they sell out or end their campaign window.
2. **Competitor & SaaS Pricing Benchmarking**: Analyze emerging B2B SaaS competitors, feature offerings, lifetime pricing tiers, and customer review sentiment.
3. **Founder Prospecting & B2B Lead Generation**: Identify fast-growing early-stage software companies and founders actively investing in customer acquisition.
4. **AI & MCP Agent Feeds**: Power automated software procurement bots, deal newsletters, and Claude/Cursor AI research agents with live software marketplace feeds.

---

## 🤖 AI Agent & MCP Server Integration (Cursor / Claude)

You can call this Actor directly from your AI agents using the official Apify MCP Server:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

---

## ❓ Frequently Asked Questions (FAQ)

### Is scraping AppSumo compliant?
Yes. This Actor strictly collects public deal listings openly indexed on AppSumo Browse. It operates without requiring user accounts or passwords.

### How much does this Actor cost?
We use a 100% transparent **Pay-Per-Event (PPE)** pricing model at **$0.005 per extracted deal record** ($5.00 per 1,000 deals). You never pay for server idle time or empty results.

---

## 🔗 Official Links & Resources

- **Apify Actor Store**: [moneygain/appsumo-deals-scraper](https://apify.com/moneygain/appsumo-deals-scraper)
- **Developer Profile**: [Moneygain on Apify](https://apify.com/moneygain)
