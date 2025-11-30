# Nomadiq-Task

## Objective
Collect real flight fare data and analyze how ticket prices change as the
departure date gets closer, across different airlines on the top 5 most in-
demand routes. The goal is to identify the best booking window and price
fluctuation patterns, helping us strengthen the Smart Booking prediction
model.

## Top 5 Routes
- DEL → DXB (Dubai)
- BOM → LHR (London Heathrow)
- DEL → SIN (Singapore)
- BOM → DOH (Doha)
- DEL → JFK (New York)

## Task Requirements
1. Scrape daily flight prices from publicly available airline / travel websites for
each of the above routes for the next 30 days (no login-required sources).
2. Store data in CSV/Excel in a structured format.
3. Clean and preprocess data with at least the following columns:
   - days_to_departure
   - airline
   - price
   - stops_count
   - duration
4. Create analysis & visualization:
   - Graph: Price vs Days-to-Departure per airline
   - Compare volatility across airlines
   - Detect price spikes and drops
   - Identify minimum price window
   - Summary report with 4–6 insights per route, including observations, learning, and recommendations

## Deliverables
- Scraping script (Python / Selenium / Playwright / BeautifulSoup)
- Clean CSV/Excel dataset
- Visualization graphs (for all 5 routes)
- Short insight summary (PDF / Doc)

## Expected Timeline
5–7 days

## End Goal
Build meaningful insights to support Nomadiq’s Smart Price Prediction
Model, helping automate the best booking window for travellers.

## Sample Expected Output
For BOM–DEL, Indigo (6E) shows highest fluctuation between day 18–27 with cheapest
price around day 14. Vistara remains stable but rarely the lowest. Major spike on
weekends & holidays.
