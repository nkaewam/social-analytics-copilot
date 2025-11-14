-- Initialize campaign database schema
-- This script runs automatically when the Postgres container is first created

-- Create tables
CREATE TABLE IF NOT EXISTS campaigns (
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

CREATE TABLE IF NOT EXISTS creatives (
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

CREATE TABLE IF NOT EXISTS campaign_status (
    campaign_id INTEGER PRIMARY KEY REFERENCES campaigns(campaign_id),
    is_active BOOLEAN,
    budget_remaining DECIMAL(10,2),
    last_metrics_sync TIMESTAMP,
    alert_flags TEXT[]
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_campaigns_status ON campaigns(status);
CREATE INDEX IF NOT EXISTS idx_campaigns_brand ON campaigns(brand);
CREATE INDEX IF NOT EXISTS idx_creatives_campaign_id ON creatives(campaign_id);
CREATE INDEX IF NOT EXISTS idx_creatives_status ON creatives(status);

