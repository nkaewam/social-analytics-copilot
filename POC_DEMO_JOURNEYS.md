# POC Demo Journeys

This document outlines the flagship demo flows for the Adapter Insight Copilot POC, showing how the multi-agent system combines internal data, external social media insights, and creative analysis.

## Journey 1: Pre-launch Campaign Planning

### User Question (Thai)
"เราจะทำแคมเปญใหม่เรื่อง 'smart home' ให้ลูกค้า FMCG X ช่วงเดือนหน้า ช่วยดูให้หน่อยว่าตอนนี้คนไทยคุยเรื่อง smart home ว่าไง แล้วจากแคมเปญเก่า ๆ ของเรา น่าจะ perform ดีแค่ไหน?"

### English Translation
"We're launching a new campaign about 'smart home' for FMCG client X next month. Can you help check what Thai people are saying about smart home right now, and based on our past campaigns, what performance can we expect?"

### Expected Agent Flow

1. **Orchestrator** recognizes this needs:
   - External social media insights (what's trending)
   - Internal performance data (past similar campaigns)
   - Creative guidance (visual style recommendations)

2. **Social Media Agent** (`social_insights`):
   - Searches: `"สมาร์ทโฮม บ้านอัจฉริยะ site:facebook.com ล่าสุด"`
   - Searches: `"smart home Thailand รีวิว site:pantip.com past week"`
   - Searches: `"smart home site:youtube.com Thailand trending"`
   - Returns:
     - Topics: price concerns, security, convenience, ease of use
     - Sentiment: mixed (positive on convenience, concerns about price and reliability)
     - Platforms: TikTok (short reviews), YouTube (long-form), Pantip (discussions)
     - Recency: Past 3-7 days

3. **Internal Data Agent** (`internal_insights`):
   - Queries campaigns table for campaigns tagged "smart_home" or similar
   - Aggregates metrics: CTR, ROAS, conversions by audience segment
   - Returns:
     - "Video creatives explaining how-to use features performed 30% better in CTR than static images"
     - "Best performance among 25-34 urban audience (ROAS 4.2 vs 2.8 average)"
     - "Gen Z audience showed lower conversion but higher engagement"

4. **Creative Agent** (`creative_insights`):
   - Analyzes top-performing creatives from past smart home campaigns
   - Returns:
     - "Successful creatives use lifestyle imagery with people using devices"
     - "Bright, modern colors (white, blue, orange) perform best"
     - "Low text density with clear product visibility"

5. **Orchestrator Synthesis**:
   ```
   **Internal Performance:**
   - Past smart home campaigns averaged ROAS of 3.5
   - Video creatives outperform static by 30% CTR
   - Best audience: 25-34 urban (ROAS 4.2)
   
   **External Market Context:**
   - Smart home is trending positively on convenience
   - Concerns: price and reliability (especially on Pantip)
   - Active discussions on TikTok (short reviews) and YouTube (long-form)
   
   **Creative Analysis:**
   - Successful style: lifestyle imagery, bright modern colors, low text
   - Avoid: product-only shots, heavy text overlays
   
   **Synthesis & Recommendations:**
   - Expected performance: ROAS 3.5-4.0 (similar to past campaigns)
   - Creative direction: Video format showing real people using devices
   - Messaging: Emphasize convenience and ease of use (addresses market concerns)
   - Target: 25-34 urban audience first, then expand
   - Platforms: YouTube (long-form) and TikTok (short reviews) align with current trends
   ```

---

## Journey 2: Live Campaign Health Check

### User Question (Thai)
"ตอนนี้แคมเปญ 'Summer Sale 2024' บน Facebook เป็นยังไงบ้างเมื่อเทียบกับคนที่พูดเรื่อง summer sale ในตลาด?"

### English Translation
"How is our 'Summer Sale 2024' campaign on Facebook performing compared to what people are saying about summer sales in the market?"

### Expected Agent Flow

1. **Orchestrator** recognizes this needs:
   - Internal performance metrics (current campaign)
   - External market sentiment (summer sale trends)
   - Creative analysis (if performance issues suspected)

2. **Internal Data Agent** (`internal_insights`):
   - Queries campaign_metrics_daily for "Summer Sale 2024"
   - Compares last 7 days vs historical average
   - Returns:
     - "CTR: 1.2% (below average of 2.1%)"
     - "ROAS: 2.3 (below average of 3.5)"
     - "Spend: $15K (on track)"
     - "Conversions: 45 (below expected 70+)"

3. **Social Media Agent** (`social_insights`):
   - Searches: `"summer sale 2024 site:facebook.com Thailand"`
   - Searches: `"summer sale site:pantip.com ล่าสุด"`
   - Returns:
     - Topics: "Summer sales are hot right now, many brands running promotions"
     - Sentiment: Positive (people actively looking for deals)
     - Platforms: Facebook (ads), Pantip (discussions), TikTok (hauls)
     - Recency: Very active in past 3 days

4. **Creative Agent** (`creative_insights`):
   - Analyzes creatives for "Summer Sale 2024"
   - Returns:
     - "Creatives use dark backgrounds (unusual for summer theme)"
     - "Text-heavy (high text density)"
     - "Limited lifestyle imagery"
     - "Doesn't match successful summer campaign patterns (bright colors, lifestyle)"

5. **Orchestrator Synthesis**:
   ```
   **Internal Performance:**
   - Campaign is underperforming: CTR 1.2% vs 2.1% average, ROAS 2.3 vs 3.5 average
   - Conversions below expected despite adequate spend
   
   **External Market Context:**
   - Summer sale topic is HOT in the market right now
   - People are actively looking for deals (positive sentiment)
   - High engagement on social media about summer sales
   
   **Creative Analysis:**
   - Visual style doesn't match market trends: dark backgrounds vs bright summer colors
   - Too text-heavy, lacks lifestyle imagery
   - Doesn't align with successful summer campaign patterns
   
   **Synthesis & Recommendations:**
   - **Diagnosis**: Performance issue is likely CREATIVE/TARGETING, not topic fatigue
   - Market interest is high, but your creatives aren't resonating
   - **Action Items**:
     1. Update creatives: Bright colors, lifestyle imagery, lower text density
     2. Test new creative variants immediately (market is hot now)
     3. Consider A/B test: current dark creatives vs bright summer-themed
     4. Review targeting: Ensure alignment with active summer sale seekers
   ```

---

## Journey 3: Post-campaign Insight Report

### User Question (Thai)
"สรุปให้หน่อยว่าแคมเปญ 'New Retail AI' ของเรา resonate กับตลาดไทยแค่ไหน ทั้งภายในและภายนอก"

### English Translation
"Summarize how well our 'New Retail AI' campaign resonated with the Thai market, both internally and externally."

### Expected Agent Flow

1. **Orchestrator** recognizes this needs:
   - Internal performance breakdown
   - External market alignment
   - Creative pattern analysis

2. **Internal Data Agent** (`internal_insights`):
   - Queries full campaign performance for "New Retail AI"
   - Breaks down by audience segment, platform, creative
   - Returns:
     - "Overall ROAS: 4.2 (above average 3.5)"
     - "Best performing: Gen Z audience (ROAS 5.1), TikTok platform (ROAS 4.8)"
     - "Top creative: Creative_AI_03 (ROAS 6.2)"
     - "Weakest: Millennials on Facebook (ROAS 2.1)"

3. **Social Media Agent** (`social_insights`):
   - Searches: `"retail AI Thailand site:facebook.com"`
   - Searches: `"AI ร้านค้า site:pantip.com"`
   - Searches: `"retail AI site:tiktok.com Thailand"`
   - Returns:
     - Topics: "AI in retail is discussed positively, especially convenience"
     - Sentiment: Positive (excitement about technology, some concerns about jobs)
     - Platforms: TikTok (viral), Pantip (discussions), YouTube (explanations)
     - Alignment: Campaign messaging aligned with "convenience" narrative

4. **Creative Agent** (`creative_insights`):
   - Analyzes all creatives, compares top vs bottom performers
   - Returns:
     - "Top performers: Bright colors, tech-forward imagery, minimal text"
     - "Bottom performers: Corporate style, heavy text, traditional retail imagery"
     - "Pattern: Gen Z responds to modern, tech-forward visuals"

5. **Orchestrator Synthesis**:
   ```
   **Internal Performance:**
   - Strong overall performance: ROAS 4.2 (20% above average)
   - Standout: Gen Z + TikTok combination (ROAS 5.1)
   - Best creative: Creative_AI_03 (ROAS 6.2) - tech-forward, bright colors
   - Weak spot: Millennials on Facebook (ROAS 2.1) - needs improvement
   
   **External Market Context:**
   - Campaign aligned well with market conversations
   - "Convenience" messaging matched what people are discussing
   - AI in retail is trending positively (especially on TikTok)
   - Some concerns about job displacement (not addressed in campaign)
   
   **Creative Analysis:**
   - Successful pattern: Bright colors + tech-forward imagery + minimal text
   - Failed pattern: Corporate style + heavy text + traditional retail
   - Gen Z clearly prefers modern, tech-forward visuals
   
   **Synthesis & Recommendations:**
   - **What Worked:**
     - Strong alignment with market sentiment (convenience narrative)
     - Gen Z targeting was spot-on (ROAS 5.1)
     - Creative_AI_03 style should be replicated
   
   - **What to Improve:**
     - Millennials on Facebook underperformed - test different creative style
     - Address job displacement concerns in future campaigns
   
   - **Next Campaign Suggestions:**
     - Double down on Gen Z + TikTok (proven winner)
     - Replicate Creative_AI_03 visual style
     - Develop Millennials-specific creative (less tech-forward, more practical)
     - Address job concerns with messaging about "enhancing jobs, not replacing"
   ```

---

## Journey 4: Creative Pattern Mining

### User Question (Thai)
"ดูให้หน่อยว่าจากแคมเปญทั้งหมดในปีที่แล้ว รูปแบบภาพแบบไหนที่ perform ดีสุดในกลุ่ม Gen Z"

### English Translation
"Check from all campaigns last year, what visual styles performed best for Gen Z audiences?"

### Expected Agent Flow

1. **Orchestrator** recognizes this needs:
   - Internal performance data (Gen Z campaigns)
   - Creative analysis (visual patterns)

2. **Internal Data Agent** (`internal_insights`):
   - Queries all campaigns from last year
   - Filters by audience_segment = 'gen_z'
   - Aggregates performance by creative
   - Returns:
     - "Top 10 Gen Z creatives: Average ROAS 5.2"
     - "Bottom 10 Gen Z creatives: Average ROAS 1.8"
     - "Campaigns: 15 total, 8 above average"

3. **Creative Agent** (`creative_insights`):
   - Lists creatives for top-performing Gen Z campaigns
   - Analyzes each creative
   - Compares top vs bottom performers
   - Returns:
     - "Top performers: 90% have bright colors (blue, orange, pink)"
     - "Top performers: 80% show faces (youthful people)"
     - "Top performers: 70% have low text density"
     - "Top performers: 90% use playful/energetic tone"
     - "Bottom performers: 60% use corporate style"
     - "Bottom performers: 70% have high text density"

4. **Orchestrator Synthesis**:
   ```
   **Internal Performance:**
   - Gen Z campaigns: 15 total, 8 above average (ROAS 3.5+)
   - Top 10 creatives: Average ROAS 5.2 (49% above average)
   - Bottom 10 creatives: Average ROAS 1.8 (49% below average)
   
   **Creative Pattern Analysis:**
   - **Top Performers (ROAS 5.2 average):**
     - 90% use bright, vibrant colors (blue, orange, pink)
     - 80% feature faces (youthful people, diverse)
     - 70% have low text density (headlines only, minimal copy)
     - 90% use playful/energetic emotional tone
     - Common layout: Centered or split-screen
     - Platform fit: TikTok/Instagram style
   
   - **Bottom Performers (ROAS 1.8 average):**
     - 60% use corporate/formal style
     - 70% have high text density (lots of copy)
     - 50% use serious/formal tone
     - Common: Product-only shots, minimal people
   
   **Synthesis & Recommendations:**
   - **Winning Formula for Gen Z:**
     - Bright colors (blue, orange, pink) + Faces (youthful) + Low text + Playful tone
     - ROAS improvement: 189% vs corporate style
   
   - **Action Items:**
     1. Apply winning formula to all Gen Z campaigns
     2. Avoid: Corporate style, high text density, serious tone
     3. Test: Variations within bright color palette
     4. Platform: Optimize for TikTok/Instagram format
   ```

---

## Demo Tips

1. **Start with Journey 1** (Pre-launch) - Shows full power of combining all three lenses
2. **Use real campaign names** if available, or use realistic examples
3. **Show the agent reasoning** - Explain which agents are being called and why
4. **Highlight synthesis** - The value is in combining insights, not just individual agent outputs
5. **Be ready for follow-ups** - Users will ask clarifying questions, show how the orchestrator handles them

## Expected Response Times

- Social Media Agent: 5-15 seconds (multiple searches)
- Internal Data Agent: 2-5 seconds (SQL query)
- Creative Agent: 3-10 seconds (image analysis)
- Orchestrator Synthesis: 2-5 seconds

Total: ~15-35 seconds for a complete multi-agent response

