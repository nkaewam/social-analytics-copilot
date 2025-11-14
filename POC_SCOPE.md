# POC Scope and Assumptions

## Flagship POC Questions

1. **Pre-launch Planning**: "We're launching a new campaign about [topic] next month. What's trending on Thai social media for this topic, and based on our past similar campaigns, what performance can we expect?"

2. **Live Campaign Health Check**: "How is our current campaign '[Campaign Name]' performing compared to market trends? Why might it be underperforming?"

3. **Post-campaign Review**: "Summarize our campaign '[Campaign Name]' - what worked, what didn't, and how did it align with Thai social media conversations?"

4. **Creative Pattern Mining**: "What visual styles and messages work best for Gen Z audiences based on our historical campaigns?"

## Data Source Assumptions

- **BigQuery**: Historical analytics data (campaign_metrics_daily)
- **Postgres**: Operational/transactional data (campaigns, creatives, campaign_status)
- **Image Storage**: Public GCS bucket URLs or HTTPS URLs accessible to the model

## Database Schema Split

### BigQuery (Analytics/Warehouse)

**`campaign_metrics_daily`** - Historical performance metrics
- `campaign_id` (INTEGER, FOREIGN KEY)
- `date` (DATE)
- `impressions` (INTEGER)
- `clicks` (INTEGER)
- `spend` (FLOAT)
- `conversions` (INTEGER)
- `roas` (FLOAT)
- `platform` (STRING) - e.g., "facebook", "youtube", "tiktok"
- `audience_segment` (STRING) - e.g., "gen_z", "millennials", "office_workers"

**Use for**: Analytics, trends, historical performance, aggregated metrics

### Postgres (Operational/Transactional)

**`campaigns`** - Campaign configurations and metadata
- `campaign_id` (SERIAL PRIMARY KEY)
- `name` (VARCHAR)
- `brand` (VARCHAR)
- `objective` (VARCHAR) - e.g., "awareness", "conversions", "engagement"
- `status` (VARCHAR) - "draft", "active", "paused", "completed"
- `owner_id` (INTEGER)
- `created_at`, `updated_at` (TIMESTAMP)
- `start_date`, `end_date` (DATE)
- `notes` (TEXT)
- `brief_url` (TEXT)

**`creatives`** - Creative metadata and approval status
- `creative_id` (SERIAL PRIMARY KEY)
- `campaign_id` (INTEGER, FK to campaigns)
- `image_url` (TEXT)
- `platform` (VARCHAR)
- `format` (VARCHAR) - e.g., "static", "video_thumbnail", "carousel"
- `status` (VARCHAR) - "draft", "approved", "rejected", "active"
- `approved_by` (INTEGER), `approved_at` (TIMESTAMP)
- `tags` (TEXT[])
- `notes` (TEXT)

**`campaign_status`** - Real-time operational status
- `campaign_id` (INTEGER PRIMARY KEY, FK to campaigns)
- `is_active` (BOOLEAN)
- `budget_remaining` (DECIMAL)
- `last_metrics_sync` (TIMESTAMP)
- `alert_flags` (TEXT[])

**Use for**: Current status, configurations, operational lookups, approvals

## POC Dataset Requirements

- **BigQuery**: 
  - Daily metrics for 10 campaigns (2-5 days per campaign)
  - Mix of platforms (Facebook, YouTube, TikTok)
  - Mix of audience segments (Gen Z, Millennials, Office Workers)
  
- **Postgres**:
  - 10 campaigns with varied statuses (active, completed, paused)
  - 2-3 creatives per campaign with metadata
  - Campaign status records for all campaigns

**Sample Data**: See `sample_data/` directory for CSV files ready to load into both databases.

