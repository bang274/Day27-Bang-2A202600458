# 03 · Cost Calculation — Tính chi phí từng Config × 2 Scenarios

> **Mục tiêu**: Với mỗi config đã thiết kế ở `02-config-design.md`, tính cost/turn → cost/conversation → monthly cho cả 2 scenarios (low season + high season).
>
> **Thời gian**: 55 phút (phần lớn của Main phase) — checkpoint 11:00 và 11:20

---

## Trước khi gọi AI — Setup chung

**Các tham số cố định cho tất cả configs** (tham khảo `cost-reference-card.md` mục 4):

```text
System prompt:              500 tokens
User message:                80 tokens
Assistant response:         180 tokens (output)
1 prior turn (history):     260 tokens (80 user + 180 assistant)
RAG top-5 chunks:         1,250 tokens (cố định)
Web search results:         800 tokens (khi bật)
Web search API call:       $0.005 / call (Tavily)
LLM classifier:            ~170 tokens (150 in + 20 out) — nếu dùng
```

**Scenario A — mùa thấp điểm**:

```text
Volume:            300 conversations / ngày
Turns/conv:        avg 4 lượt
Intent mix:        Guide 50%, Visa 25%, Weather 10%, Booking 10%, Complaint 5%
AI-served ratio:   85% (15% là Booking + Complaint = handoff)
```

**Scenario B — mùa cao điểm**:

```text
Volume:           1,200 conversations / ngày (×4)
Turns/conv:        avg 7 lượt
Intent mix:        Guide 30%, Visa 15%, Weather 10%, Booking 35%, Complaint 10%
AI-served ratio:   55% (45% là handoff)
```

**Human baseline để so sánh**: $0.50 / conversation cố định.

---

## Điền số cho từng config

### Config 1 — Budget Bot

| Item | Scenario A (4 turns) | Scenario B (7 turns) |
|---|---|---|
| Cost / conversation (avg) | $0.00102 | $0.00122 |
| Monthly cost | $9.20 | $43.89 |
| Human baseline | $4,500 | $18,000 |
| **Rẻ hơn human ___×** | 490× | 409× |
| **Savings %** | 99.80% | 99.76% |

**Sanity check**:

```text
Cost/conv khá hợp lý cho cấu hình cheap model (xung quanh $0.001). Monthly cực rẻ ($9-44). Số quá đúng.
```

---

### Config 2 — Smart Mix

| Item | Scenario A | Scenario B |
|---|---|---|
| Cost / conversation (avg) | $0.01535 | $0.01915 |
| Monthly cost | $138.18 | $689.30 |
| Human baseline | $4,500 | $18,000 |
| **Rẻ hơn human ___×** | 32.5× | 26.1× |
| **Savings %** | 96.93% | 96.17% |

**Sanity check**:

```text
Scenario B đắt hơn A khoảng 5 lần (do volume x4 và turns cao hơn). Cost/conv ~$0.01-0.02 rất thực tế cho model tầm trung kết hợp bật selective Web Search API.
```

---

### Config 3 — Premium Concierge

| Item | Scenario A | Scenario B |
|---|---|---|
| Cost / conversation (avg) | $0.09394 | $0.11386 |
| Monthly cost | $845.42 | $4099.05 |
| Human baseline | $4,500 | $18,000 |
| **Rẻ hơn human ___×** | 5.3× | 4.4× |
| **Savings %** | 81.21% | 77.23% |

**Sanity check**:

```text
Config này đắt kinh khủng (lên tới hơn $4,000 tháng trong cao điểm) do Opus 4.7 đắt và giữ full history cho 7 turns liên tục. Tuy nhiên vẫn rẻ hơn nhân viên người ($18,000).
```

---

## Quality + Speed estimate (qualitative)

Mỗi config — estimate Low / Medium / High. Không có công cụ đo chính xác trong lab, ước tính dựa trên model tier + web search + history.

| Config | Quality (Low/Med/High) | Speed (Low/Med/High) | Lý do |
|---|---|---|---|
| 1: Budget Bot | Low | High | Model rẻ nhất và không có web search, tốc độ sinh token rất nhanh. |
| 2: Smart Mix | Med | Med | Cân bằng chất lượng qua model Mid, web search Selective có thể thêm 1s latency. |
| 3: Premium Concierge | High | Low | Dùng model cực mạnh, logic cao nhưng tốc độ chậm nhất do context lớn và latency cao. |

---

## Bảng kiểm trước khi sang file tiếp theo

- [x] Tất cả ≥3 configs đã có cost/conv + monthly cho cả 2 scenarios
- [x] Đã so sánh từng config với human baseline ($0.50/conv)
- [x] Có quality + speed estimate cho mỗi config
- [x] Đã sanity check — không có số "quá lạ" (cost <$0.001 hoặc >$1/conv)

Xong → mở `04-comparison-table.md`.
