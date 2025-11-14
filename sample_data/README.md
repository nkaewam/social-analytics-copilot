# Sample Data Files

This directory contains sample CSV data files for loading into BigQuery and Postgres databases for POC testing.

**Note**: These campaigns are representative of the types of work a Thai MarTech agency would handle, including:
- E-commerce platform launches
- Performance marketing campaigns
- MarTech/SaaS product promotions
- Enterprise B2B campaigns
- Social commerce campaigns

## Files

### BigQuery Data

- **`bigquery_campaign_metrics_daily.csv`**: Historical performance metrics
  - Contains daily metrics for 10 campaigns across multiple platforms and audience segments
  - Date range: January 2024 to October 2024
  - Columns: campaign_id, date, impressions, clicks, spend, conversions, roas, platform, audience_segment

### Postgres Data

- **`postgres_campaigns.csv`**: Campaign operational data
  - 10 sample campaigns representing typical MarTech agency work:
    - E-commerce platform launches (ShopNow, LoveShop, StudyMart, SpookyShop)
    - MarTech/SaaS campaigns (Adapter Digital Performance Suite, CDP Awareness, Enterprise Tools)
    - Fashion/Retail campaigns (FashionHub, StyleBangkok)
    - Various statuses: active, completed, paused
  - Includes campaign configurations, objectives, and metadata
  - Columns: campaign_id, name, brand, objective, status, owner_id, created_at, updated_at, start_date, end_date, notes, brief_url

- **`postgres_creatives.csv`**: Creative metadata and approval status
  - 21 creatives across 10 campaigns
  - Mix of platforms: Facebook, YouTube, TikTok, Instagram, LinkedIn
  - Includes approval status, tags, and platform information
  - Reflects real-world creative types: hero images, carousels, video thumbnails, platform-specific formats
  - Columns: creative_id, campaign_id, image_url, platform, format, status, approved_by, approved_at, tags, notes

- **`postgres_campaign_status.csv`**: Real-time campaign status
  - Current operational status for all campaigns
  - Includes budget remaining and alert flags
  - Columns: campaign_id, is_active, budget_remaining, last_metrics_sync, alert_flags

## Loading Instructions

### BigQuery

1. Create a dataset (e.g., `campaign_analytics`)
2. Create table `campaign_metrics_daily` with schema:
   ```sql
   CREATE TABLE campaign_metrics_daily (
     campaign_id INT64,
     date DATE,
     impressions INT64,
     clicks INT64,
     spend FLOAT64,
     conversions INT64,
     roas FLOAT64,
     platform STRING,
     audience_segment STRING
   );
   ```
3. Load CSV:
   ```bash
   bq load --source_format=CSV --skip_leading_rows=1 \
     campaign_analytics.campaign_metrics_daily \
     bigquery_campaign_metrics_daily.csv
   ```

### Postgres

1. Create database and tables:
   ```sql
   CREATE DATABASE campaign_db;
   
   CREATE TABLE campaigns (
     campaign_id SERIAL PRIMARY KEY,
     name VARCHAR(255),
     brand VARCHAR(255),
     objective VARCHAR(50),
     status VARCHAR(20),
     owner_id INTEGER,
     created_at TIMESTAMP,
     updated_at TIMESTAMP,
     start_date DATE,
     end_date DATE,
     notes TEXT,
     brief_url TEXT
   );
   
   CREATE TABLE creatives (
     creative_id SERIAL PRIMARY KEY,
     campaign_id INTEGER REFERENCES campaigns(campaign_id),
     image_url TEXT,
     platform VARCHAR(50),
     format VARCHAR(50),
     status VARCHAR(20),
     approved_by INTEGER,
     approved_at TIMESTAMP,
     tags TEXT[],
     notes TEXT
   );
   
   CREATE TABLE campaign_status (
     campaign_id INTEGER PRIMARY KEY REFERENCES campaigns(campaign_id),
     is_active BOOLEAN,
     budget_remaining DECIMAL(10,2),
     last_metrics_sync TIMESTAMP,
     alert_flags TEXT[]
   );
   ```

2. Load CSV files:
   ```bash
   # Load campaigns
   psql -d campaign_db -c "\COPY campaigns FROM 'postgres_campaigns.csv' WITH CSV HEADER;"
   
   # Load creatives
   psql -d campaign_db -c "\COPY creatives FROM 'postgres_creatives.csv' WITH CSV HEADER;"
   
   # Load campaign_status
   psql -d campaign_db -c "\COPY campaign_status FROM 'postgres_campaign_status.csv' WITH CSV HEADER;"
   ```

## Data Notes

- **Campaign IDs**: Match between BigQuery and Postgres (1-10)
- **Image URLs**: Placeholder URLs - replace with actual image URLs for creative analysis
- **Dates**: Sample data spans 2024, adjust as needed for your testing
- **Status Values**: 
  - Campaigns: draft, active, paused, completed
  - Creatives: draft, approved, rejected, active
- **Alert Flags**: JSON array format in Postgres (e.g., `{low_budget}` or `{low_performance}`)

## Testing Queries

After loading, test with:

**BigQuery:**
```sql
-- Top campaigns by ROAS
SELECT campaign_id, SUM(conversions) / SUM(spend) as roas 
FROM campaign_metrics_daily 
GROUP BY campaign_id 
ORDER BY roas DESC 
LIMIT 5;
```

**Postgres:**
```sql
-- Active campaigns
SELECT * FROM campaigns WHERE status = 'active';

-- Campaigns with low budget
SELECT c.*, cs.budget_remaining 
FROM campaigns c 
JOIN campaign_status cs ON c.campaign_id = cs.campaign_id 
WHERE cs.alert_flags @> ARRAY['low_budget'];
```

