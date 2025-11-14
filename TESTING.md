# Testing and Evaluation Guide

This document outlines how to test and evaluate the Insight Copilot POC.

## Test Dataset Setup

### Minimum Requirements

Create a small but realistic dataset in BigQuery with:

1. **campaigns table** (5-10 campaigns):
   - Mix of objectives: awareness, conversions, engagement
   - Mix of tags: smart_home, gen_z, video, etc.
   - Date range: Last 6-12 months

2. **campaign_metrics_daily** (2-4 weeks per campaign):
   - Multiple platforms: Facebook, YouTube, TikTok
   - Multiple audience segments: gen_z, millennials, office_workers
   - Varied performance (some high, some low ROAS)

3. **creatives table** (2-5 creatives per campaign):
   - Public image URLs (GCS bucket or HTTPS)
   - Mix of formats: static, video_thumbnail, carousel
   - Link to campaigns via campaign_id

### Sample Data Generation

You can use this SQL to create sample data:

```sql
-- Sample campaigns
INSERT INTO campaigns VALUES
('camp_001', 'Smart Home Launch', 'BrandX', 'awareness', ['smart_home', 'gen_z'], '2024-01-01', '2024-01-31'),
('camp_002', 'Summer Sale 2024', 'BrandY', 'conversions', ['summer', 'millennials'], '2024-06-01', '2024-06-30'),
-- ... more campaigns

-- Sample metrics (generate daily rows)
-- Use a script or BigQuery's GENERATE_DATE_ARRAY to create daily metrics
```

## Testing Checklist

### 1. Agent Connectivity Tests

- [ ] Social Media Agent can execute google_search queries
- [ ] Internal Data Agent can connect to genai-toolbox server
- [ ] Internal Data Agent can query BigQuery successfully
- [ ] Creative Agent can list creatives for a campaign
- [ ] Creative Agent can analyze image URLs

### 2. Individual Agent Tests

**Social Media Agent:**
```python
# Test: "What's trending on smart home in Thailand?"
# Expected: Returns topics, sentiment, platforms, recency
```

**Internal Data Agent:**
```python
# Test: "Show top 5 campaigns by ROAS"
# Expected: Returns campaign list with metrics
```

**Creative Agent:**
```python
# Test: "Analyze creatives for campaign X"
# Expected: Returns visual style analysis
```

### 3. Orchestrator Integration Tests

Test each demo journey from `POC_DEMO_JOURNEYS.md`:

- [ ] Journey 1: Pre-launch Planning
- [ ] Journey 2: Live Campaign Health Check
- [ ] Journey 3: Post-campaign Review
- [ ] Journey 4: Creative Pattern Mining

### 4. Edge Cases

- [ ] Campaign not found (graceful error handling)
- [ ] No social media results (handles empty results)
- [ ] Invalid image URL (error handling)
- [ ] Toolbox server down (fallback behavior)
- [ ] Ambiguous questions (clarification requests)

## User Testing with Planners

### Test Session Structure

1. **Introduction** (5 min)
   - Explain what the system does
   - Show basic capabilities

2. **Guided Demo** (15 min)
   - Walk through Journey 1 (Pre-launch)
   - Show how insights are synthesized

3. **Free-form Testing** (20 min)
   - Let planners ask their own questions
   - Observe how they interact
   - Note confusion points

4. **Feedback Session** (10 min)
   - What was useful?
   - What was confusing?
   - What's missing?

### Feedback Collection

Collect feedback along three axes:

1. **Usefulness**
   - Did it answer the real business question?
   - Were insights actionable?
   - Would you use this in real work?

2. **Correctness & Robustness**
   - Were SQL queries correct?
   - Were interpretations accurate?
   - Did it handle edge cases well?

3. **UX Flow**
   - Were follow-up questions natural?
   - Was the response structure clear?
   - Did it feel like talking to a colleague?

### Sample Questions for Testers

Ask planners to try:
- "We're planning a campaign about [topic]. What should we know?"
- "How is [campaign name] performing?"
- "What worked best in our campaigns last quarter?"
- "What visual styles resonate with [audience]?"

## Iteration Plan

Based on feedback, iterate on:

### Phase 1: Prompt Refinement
- Improve orchestrator decision logic
- Clarify agent response formats
- Add more examples to prompts

### Phase 2: Tool Improvements
- Better error handling in tools
- More robust BigQuery query generation
- Enhanced image analysis

### Phase 3: Response Formatting
- Standardize output structure
- Add visualizations (if needed)
- Improve readability

### Phase 4: Performance
- Optimize query patterns
- Cache frequently accessed data
- Reduce latency

## Success Metrics

- **Accuracy**: >80% of SQL queries execute correctly
- **Relevance**: >70% of insights rated as "useful" by planners
- **Speed**: <30 seconds for complete multi-agent response
- **Adoption**: Planners want to use it for real campaigns

## Reporting Issues

When reporting issues, include:
1. Exact question asked
2. Expected behavior
3. Actual behavior
4. Error messages (if any)
5. Agent logs (if available)

## Next Steps After POC

1. **Production Hardening**
   - Add authentication/authorization
   - Implement rate limiting
   - Add monitoring/logging

2. **Feature Extensions**
   - More data sources (website analytics, CRM)
   - Scheduled reports
   - Alerting for anomalies

3. **Integration**
   - Slack/Line bot
   - Dashboard embedding
   - API for other tools

