# Data Split Guide: BigQuery vs Postgres

This document explains the rationale for splitting data between BigQuery and Postgres, and how the agent routes queries.

## Why Split?

### BigQuery (Analytics/Warehouse)
- **Purpose**: Historical performance data, analytics, trends
- **Characteristics**: 
  - Large volume, time-series data
  - Read-heavy, batch-oriented
  - Complex aggregations and analytics
- **Best for**: "What happened?", "What's the trend?", "Show me performance"

### Postgres (Operational/Transactional)
- **Purpose**: Current configurations, operational status, real-time data
- **Characteristics**:
  - Transactional, frequently updated
  - Relational integrity important
  - Real-time lookups
- **Best for**: "What's the current status?", "Which campaigns are...", "Show me configurations"

## Data Mapping

| Data Type | Database | Table | Use Case |
|-----------|----------|-------|----------|
| Historical metrics | BigQuery | `campaign_metrics_daily` | Analytics, ROAS, trends |
| Campaign configs | Postgres | `campaigns` | Current status, objectives |
| Creative metadata | Postgres | `creatives` | Approval status, tags |
| Real-time status | Postgres | `campaign_status` | Budget, alerts, active status |

## Query Routing Examples

### Route to BigQuery
- "Show top 5 campaigns by ROAS"
- "What's the average CTR for Gen Z?"
- "Compare performance trends month-over-month"
- "Show me conversion rates by platform"

### Route to Postgres
- "Which campaigns are currently active?"
- "Show me campaigns that need approval"
- "What's the budget remaining for campaign X?"
- "Which creatives are pending review?"

### Route to Both
- "How is campaign 'Summer Sale' performing and what's its status?"
  → Postgres: Get current status
  → BigQuery: Get performance metrics

## Agent Decision Logic

The internal_data_agent uses these heuristics to route queries:

1. **Keywords indicating analytics** → BigQuery
   - "performance", "ROAS", "CTR", "trends", "average", "compare", "historical"

2. **Keywords indicating operational** → Postgres
   - "status", "active", "approval", "current", "which campaigns", "pending"

3. **Ambiguous queries** → Try Postgres first (faster), then BigQuery if needed

## Benefits

1. **Performance**: Right tool for the right job
2. **Cost**: BigQuery optimized for analytics, Postgres for transactions
3. **Scalability**: Each database optimized for its use case
4. **Real-world pattern**: Mirrors actual production architectures

