### High-level idea

Build a **dual‑lens insight assistant**:  
- One lens = **external social media** (your current social media agent)  
- One lens = **internal performance data** (BigQuery/Postgres)  
- A **query/orchestrator agent** sits on top and decides when/how to pull from each, then merges into one narrative for the user.

---

## 1. Overall POC story you can pitch

**“Insight Copilot”** that can answer questions like:

- “For our last 3 FMCG campaigns, which messages performed best internally, and how does that align with what’s trending on Thai social media right now?”
- “We’re planning a new campaign about sustainable living. What’s the current sentiment in Thailand on this topic, and based on our past campaigns, what performance can we expect?”
- “Our current campaign for [Brand X] on Facebook looks weak. Is this because of internal issues (low media spend / poor creative) or because the market is cold on this topic?”

This shows **federated reasoning**: the AI pulls **internal numbers** + **external context** and synthesizes.

---

## 2. Minimal architecture for the POC

### **A. Social Media Agent (already done)**

- Uses `google_search` to pull:
  - Trends, sentiment, content formats, hashtags from Thai social media  
  - Prioritizes: Facebook, YouTube, TikTok, Pantip, then X (for Gen Z)
- Output: structured summary (topics, sentiment, examples, time window).

### **B. Internal Data Agent (Query Agent)**

Expose internal data via tools, e.g.:

- `bigquery_query` tool → runs parameterized SQL on BigQuery
- `postgres_query` tool → runs parameterized SQL on Postgres

This agent specializes in questions like:

- “For campaign XYZ, what were impressions, CTR, CPC, conversions over the last 14 days?”
- “Which creatives had the highest engagement rate among Gen Z in the last 6 months?”
- “Show top 5 campaigns by ROAS in [industry/vertical].”

It learns schema summaries (e.g. `campaigns`, `ad_groups`, `creatives`, `daily_metrics`) and can:
- Translate NL → SQL
- Return **structured** JSON + **business-language** explanation.

### **C. Orchestrator / “Insight Copilot” Agent**

- User talks only to this root agent.
- It decides:
  - When to call the **Social Media Agent** (external)
  - When to call the **Internal Data Agent** (internal)
  - When to use **both** and merge results.

Prompt logic for orchestrator:

- If user asks about:
  - Performance, metrics, ROAS, historical campaigns → **internal first**.
  - Trends, sentiment, “what people say” → **external first**.
  - “Compare”, “align”, “is this consistent with”, “how does this match the market” → **call both**, then synthesize.

---

## 3. Concrete POC scenarios (easy to demo)

### **Scenario 1: Pre‑launch campaign planning**

**User:**  
“เราจะทำแคมเปญใหม่เรื่อง ‘smart home’ ให้ลูกค้า FMCG X ช่วงเดือนหน้า ช่วยดูให้หน่อยว่าตอนนี้คนไทยคุยเรื่อง smart home ว่าไง แล้วจากแคมเปญเก่า ๆ ของเรา น่าจะ perform ดีแค่ไหน?”

**What happens under the hood:**

- **External (social agent):**
  - `google_search` queries like:
    - `"สมาร์ทโฮม บ้านอัจฉริยะ site:facebook.com ล่าสุด"`
    - `"smart home Thailand รีวิว site:pantip.com past week"`
  - Returns:
    - Topics: price concerns, security, convenience
    - Sentiment: mixed, with worries about reliability
    - Platforms where it’s hot (e.g. TikTok short reviews, YouTube longform)

- **Internal (query agent):**
  - SQL on BigQuery/Postgres:
    - Find past campaigns tagged `smart_home` / `home tech` / similar.
    - Pull metrics: impressions, CTR, CVR, ROAS, by audience and creative type.
  - Returns:
    - “Video creatives explaining how-to use features performed 30% better in CTR than static images.”
    - “Best performance among 25–34 urban audience.”

- **Orchestrator output to user:**
  - External: what’s hot, what people complain about, sentiment.
  - Internal: what has worked for your campaigns.
  - Recommendation: creative angle, messaging to emphasize, risk points.

### **Scenario 2: Live campaign health check**

**User:**  
“ตอนนี้แคมเปญ ‘Adapter Performance Suite Q1’ บน Facebook เป็นยังไงบ้างเมื่อเทียบกับคนที่พูดเรื่อง martech ในตลาด?”

- Internal agent:
  - Fetch latest metrics (last 7 days) for that campaign.
  - Compare vs historical benchmarks.
- Social agent:
  - Check “martech”, “marketing automation”, “CDP”, etc. across Thai social.
- Orchestrator:
  - “Your CTR is below your own average but market interest in martech is high; likely creative/targeting issue, not topic fatigue.”

### **Scenario 3: Post‑campaign insight report**

**User:**  
“สรุปให้หน่อยว่าแคมเปญ ‘New Retail AI’ ของเรา resonate กับตลาดไทยแค่ไหน ทั้งภายในและภายนอก”

- Internal: Which creatives, audiences, channels worked.
- External: How the same topic is being discussed, competing narratives, sentiment.
- Output: one **deck‑ready narrative**: key findings, what to repeat, what to avoid, next‑campaign suggestions.

---

## 4. How this makes sense to the customer (Adapter Digital)

For a MarTech company like [Adapter Digital](https://www.adapterdigital.com/):

- **Strategic value**:
  - Turns scattered dashboards + social sentiment into one **conversation with an AI planner**.
  - Helps planners/strategists answer “so what?” faster.
- **Operational value**:
  - Reduces manual time: no more switching between BigQuery, Looker dashboards, and social screenshots.
  - Always-on assistant available to AE/Planner/Strategist teams.
- **POC scope is small but impressive**:
  - 1–2 tables in BigQuery/Postgres (campaign + daily metrics)
  - Your existing social media agent
  - A thin orchestrator agent + a few polished demo questions.

---

## 5. How to position the POC

You can position the POC as:

> “An AI planning assistant that continuously **reads your own performance data** and **listens to the Thai social media market**, then helps planners answer campaign questions in natural language.”

If you want, I can next:
- Draft a **sample orchestrator agent prompt** that coordinates the social agent + internal query tools, or  
- Sketch a minimal **schema + example SQL tool definition** suitable for BigQuery/Postgres in your ADK setup.