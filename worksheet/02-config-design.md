# 02 · Configuration Design — Đặt tên + Chốt knobs cho ≥3 Configs

> **Mục tiêu**: Biến phác thảo ở `01-base-flow.md` thành ≥3 configurations chi tiết, mỗi config có tên + 3 knobs đã chốt + lý do chọn.
>
> **Thời gian**: 15 phút (đầu phần Main, trước khi tính cost)

---

## Tại sao đặt tên + viết lý do?

Khi present, nhóm sẽ nói "Config 1, Config 2, Config 3" → người nghe sẽ chán ngay. Đặt tên gợi mở (Budget Bot, Premium Concierge, Smart Mix...) giúp memorable + cho thấy nhóm hiểu rõ tradeoff. Viết lý do giúp nhóm tự kiểm tra: "Mình chọn config này vì lý do gì? Có justify được không?"

---

## Cách điền

Với mỗi config: đặt tên + chốt 3 knobs + viết 2–3 câu lý do chọn. Mỗi câu lý do phải gắn với 1 tình huống thực tế (volume thấp / khách hỏi visa nhiều / budget bị siết...).

Tham khảo bảng pricing chi tiết tại `cost-reference-card.md` mục **3. Decision Points**.

---

## Config 1

**Tên config** (gợi mở: "Budget Bot", "Bare Minimum", "Lean Mode", "Night Mode" — đặt tên có cá tính):

```text
Budget Bot
```

### 3 Knobs

**① Model tier**:

```text
Response model: Gemini 2.5 Flash-Lite → giá $0.10 / $0.40  per 1M tokens (input/output)
Classifier model: Gemini 2.5 Flash-Lite → giá $0.10 / $0.40  per 1M tokens (hoặc keyword = $0)
```

**② Web search**:

```text
☑ OFF
□ ON selective — bật cho intent: __________________
□ ON broad
```

**③ History management**:

```text
☑ Last 3
□ Last 5
□ Full
□ Summarize every ___ turns
```

### Lý do nhóm chọn config này

Trước khi viết, tự hỏi:

- Config này phục vụ tình huống nào tốt nhất? (mùa thấp điểm? night-time? volume cao đột biến?)
- Trade-off chính là gì? (Rẻ nhưng kém chất lượng? Đắt nhưng chính xác?)
- Khách hàng nào sẽ hài lòng nhất với config này? Khách nào sẽ thất vọng?

```text
Config này tiết kiệm chi phí tối đa, rất phù hợp khi traffic tăng cao đột biến hoặc để thử nghiệm sản phẩm lúc mới launch.
Trade-off lớn nhất là thiếu thông tin web real-time (như visa, thời tiết), nên có thể cung cấp thông tin cũ.
Khách hàng chỉ có câu hỏi cơ bản (chỉ dẫn đơn giản) sẽ hài lòng, nhưng khách muốn advice phức tạp sẽ thấy thiếu sót.
```

### Rủi ro lớn nhất của config này

```text
Visa info có thể outdated vì Web OFF, dẫn đến rủi ro hành khách gặp rắc rối xuất nhập cảnh.
```

---

## Config 2

**Tên config**:

```text
Smart Mix
```

### 3 Knobs

**① Model tier**:

```text
Response model: Gemini 2.5 Flash → giá $0.30 / $2.50  per 1M tokens
Classifier model: Gemini 2.5 Flash-Lite → giá $0.10 / $0.40  per 1M tokens (hoặc keyword)
```

**② Web search**:

```text
□ OFF
☑ ON selective — bật cho intent: Visa/Policy, Weather/Event
□ ON broad
```

**③ History management**:

```text
□ Last 3
☑ Last 5
□ Full
□ Summarize every ___ turns
```

### Lý do nhóm chọn config này

```text
Config này hướng đến điểm cân bằng giữa chi phí và chất lượng cho phần lớn user.
Bật web search chọn lọc giúp đảm bảo các câu hỏi nhạy cảm như visa luôn chính xác, còn model Mid giúp ngôn ngữ được mượt mà hơn model Cheap.
Sử dụng history 5 lượt đảm bảo đa số các cuộc hội thoại đều giữ được trọn context.
```

### Rủi ro lớn nhất của config này

```text
Cost có thể tăng nếu lượt chat vượt quá 5 lượt ở mùa cao điểm do web search tốn thêm token cho history.
```

---

## Config 3

**Tên config**:

```text
Premium Concierge
```

### 3 Knobs

**① Model tier**:

```text
Response model: Claude Opus 4.7 → giá $5.00 / $25.00  per 1M tokens
Classifier model: Gemini 2.5 Flash → giá $0.30 / $2.50  per 1M tokens (hoặc keyword)
```

**② Web search**:

```text
□ OFF
□ ON selective — bật cho intent: __________________
☑ ON broad
```

**③ History management**:

```text
□ Last 3
□ Last 5
☑ Full
□ Summarize every ___ turns
```

### Lý do nhóm chọn config này

```text
Cung cấp dịch vụ tốt nhất có thể, thay thế hoàn toàn nhân viên sales giỏi.
Được dùng cho các cuộc chat VIP hoặc khi margin doanh thu trên booking rất cao.
Sử dụng Opus 4.7 kết hợp với full web search đảm bảo độ thông minh, reasoning và thông tin luôn cập nhật cho mọi câu hỏi.
```

### Rủi ro lớn nhất của config này

```text
Chi phí tăng theo cấp số nhân trong các cuộc đối thoại dài (có thể lên tới $4000/tháng), ảnh hưởng đến biên lợi nhuận của dịch vụ booking rẻ.
```

---

## Bảng kiểm trước khi tính cost

- [x] ≥3 configs đã đặt tên (không chỉ "Config 1/2/3")
- [x] Mỗi config đã chốt rõ 3 knobs (không còn ô trống)
- [x] Mỗi config có ≥2 câu lý do
- [x] 3 configs đủ khác biệt — không phải chỉ đổi mỗi 1 knob nhỏ
- [x] Nhóm đồng thuận đây là 3 configs đáng so sánh

Xong → mở `03-cost-calculation.md` để bắt đầu tính cost.
