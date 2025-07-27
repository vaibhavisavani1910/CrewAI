# 📈 AI-Powered Stock Trading Crew (CrewAI)

This project is an **AI-native multi-agent system** built using [CrewAI](https://crewai.com/) to automatically:

- Discover companies trending in the news
- Conduct financial research
- Analyze investment potential
- Recommend top stock picks
- Send push notifications for selected investments

---

## 🧠 Tech Stack & Tools Used

- **CrewAI** – Multi-agent orchestration
- **Serper.dev Tool** – Real-time Google web search
- **PushNotificationTool** – Sends instant notifications for selected stocks
- **OpenAI Embeddings** – `text-embedding-3-small` for vector storage
- **Memory Modules**:
  - **Long-Term Memory (LTM)**: Persistent knowledge across sessions using SQLite
  - **Short-Term Memory (STM)**: Current session context using RAG
  - **Entity Memory**: Tracks and relates company-specific data across tasks

---

## 👥 Agents & Their Responsibilities

### 🔎 `trending_company_finder`
- Uses `SerperDevTool` to search for companies trending in the news

### 📊 `financial_researcher`
- Performs deep market research, future outlook, and investment analysis

### ✅ `stock_picker`
- Picks the best company based on research and triggers a push notification

### 🧠 `manager`
- Orchestrates and delegates tasks among all agents using a hierarchical process

---

## 🧠 Why Use Memory?

- **LTM**: Remembers past company picks and insights across runs
- **STM**: Keeps short-term focus and task continuity within a session
- **Entity Memory**: Tracks important entities (e.g., company name, ticker) to ensure accurate and context-aware analysis

Memory makes the system smarter, more coherent, and capable of handling complex workflows over time.

---

## 🔍 Web Search with Serper

- Real-time news extraction using the `SerperDevTool`
- Ensures that only **currently trending** companies are analyzed

---

## 📣 Push Notifications

- After the best stock is selected, `PushNotificationTool` sends a real-time notification
- Ideal for alerting users or triggering downstream actions

---

## 🔁 Process Flow

1. **Find Trending Companies** – via `trending_company_finder`
2. **Research Each Company** – handled by `financial_researcher`
3. **Pick the Best One** – selected by `stock_picker`
4. **Managed Hierarchically** – coordinated by `manager` agent

---
