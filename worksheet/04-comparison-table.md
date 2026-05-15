# 04 · Comparison Table — Bảng so sánh đầy đủ

> **Mục tiêu**: Tổng hợp tất cả số đã tính ở `03-cost-calculation.md` thành 1 bảng so sánh duy nhất — đây là artifact chính nhóm sẽ present.
>
> **Thời gian**: 10 phút (đầu phần Final)

---

## Bảng chính

| | Config 1 | Config 2 | Config 3 |
|---|---|---|---|
| **Tên** | Budget Bot | Smart Mix | Premium Concierge |
| **① Model** | Gemini 2.5 Flash-Lite | Gemini 2.5 Flash | Claude Opus 4.7 |
| **② Web search** | OFF | Selective | Broad |
| **③ History** | Last 3 | Last 5 | Full |
| **Intent classifier** | LLM (Flash-Lite) | LLM (Flash-Lite) | LLM (Flash) |
| **Cost / conv (Scenario A — 4 turns)** | $0.00102 | $0.01535 | $0.09394 |
| **Cost / conv (Scenario B — 7 turns)** | $0.00122 | $0.01915 | $0.11386 |
| **Monthly A** (300 conv/day × 30) | $9.20 | $138.18 | $845.42 |
| **Monthly B** (1,200 conv/day × 30) | $43.89 | $689.30 | $4099.05 |
| **vs human $4,500/mo (A)** | rẻ 490× | rẻ 32.5× | rẻ 5.3× |
| **vs human $18,000/mo (B)** | rẻ 409× | rẻ 26.1× | rẻ 4.4× |
| **Savings % (A)** | 99.80% | 96.93% | 81.21% |
| **Savings % (B)** | 99.76% | 96.17% | 77.23% |
| **Quality estimate** | Low | Med | High |
| **Speed estimate** | High | Med | Low |
| **Điểm yếu chính** | Thiếu thông tin real-time và quên ngữ cảnh xa. | Đội chi phí nhẹ nếu khách chat quá dài. | Rất đắt và tốc độ trả lời chậm. |
| **Best for** | Mới ra mắt, volume cực lớn, budget tối thiểu. | Config mặc định cho hầu hết use-cases du lịch. | Chăm sóc khách VIP hoặc chốt sales premium. |

---

## Quan sát nhanh từ bảng

Trước khi sang file recommendation, trả lời 4 câu — đây là material để present:

### Câu 1 — Config rẻ nhất là gì? Đắt nhất là gì?

```text
Rẻ nhất: Budget Bot — monthly B = $43.89
Đắt nhất: Premium Concierge — monthly B = $4099.05
Chênh: 93× lần
```

### Câu 2 — Knob nào ảnh hưởng cost nhiều nhất?

```text
Model tier quyết định chi phí lớn nhất. Đổi từ Flash-Lite lên Opus làm giá base token tăng tới 50x (input) và 62x (output). Sau đó là History Management vì giữ Full history (Turn 7) làm tốn thêm rất nhiều context window token trong khi Web Search (selective vs broad) chỉ tác động cố định ở mức nhỏ vào query cost.
```

### Câu 3 — Tại sao Scenario B không đắt ×4 lần Scenario A?

```text
Mặc dù volume tăng 4x và số turn dài hơn, nhưng Scenario B có intent mix với số lượng Booking + Complaint lên tới 45%. Nghĩa là gần một nửa số hội thoại ở cao điểm chỉ tốn duy nhất chi phí LLM classifier ở turn đầu (vài chục token) sau đó handoff ngay cho sales/manager ($0 LLM).
```

### Câu 4 — Có config nào AI đắt hơn human không?

```text
Cả 3 config đều rẻ hơn human. Kể cả Premium Concierge tốn >$4000/tháng ở mức cao điểm vẫn tiết kiệm được 77% ($18,000/tháng human cost). AI giúp phục vụ 24/7 đa ngôn ngữ, không cần tốn chi phí tuyển dụng hay nghỉ phép mà vẫn có khả năng handle spike workload.
```

---

## Bảng kiểm trước khi sang file tiếp theo

- [x] Bảng đầy đủ — không còn ô trống
- [x] Đã có 4 câu trả lời cho 4 quan sát ở trên
- [x] Nhóm đồng thuận về số trong bảng (đã sanity check)

Xong → mở `05-recommendation.md` để viết recommendation cuối + chuẩn bị present.
