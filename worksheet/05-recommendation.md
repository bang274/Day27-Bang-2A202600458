# 05 · Recommendation + Justification — Kết luận & Chuẩn bị Present

> **Mục tiêu**: Chọn 1 config (hoặc combo) nhóm recommend deploy, viết justification ngắn gọn, và chuẩn bị 5 phút present.
>
> **Thời gian**: 10 phút (cuối phần Final) — Pens down lúc 12:00

---

## 4 câu hỏi nhóm phải trả lời

Mỗi câu trả lời 2–4 câu. Không lan man, không clichés. Mỗi câu phải justify được bằng số trong bảng so sánh.

### Câu 1 — Recommend config nào?

```text
Nhóm recommend Smart Mix là config mặc định cho công ty du lịch trong hầu hết các kịch bản. Lý do là monthly cost ở mùa cao điểm chỉ $689, quá nhỏ so với $18,000 nếu dùng nhân sự. Tuy nhiên, nếu công ty có phân hạng khách VIP, có thể trigger Premium Concierge dựa trên profile ID để chốt sales các tour đắt tiền.
```

### Câu 2 — So với human baseline $0.50/conv → tiết kiệm bao nhiêu? Có đắt hơn human ở chỗ nào không?

```text
Với Smart Mix, công ty tiết kiệm 96.93% ($4361/tháng) ở Scenario A và 96.17% ($17310/tháng) ở Scenario B. Không config nào đắt hơn chi phí human về mặt LLM tokens. Tuy nhiên, AI không thể hoàn toàn thay thế con người ở tác vụ chốt đơn Booking & Complaint, do đó thực tế chúng ta vẫn phải duy trì team sales.
```

### Câu 3 — Khi nào nên upgrade / downgrade config?

```text
Nên upgrade lên Premium Concierge khi công ty bắt đầu tung ra các gói tour hạng sang (margin cao) và cần AI có reasoning mạnh để thuyết phục khách hàng. Nên downgrade về Budget Bot trong các tình huống lưu lượng truy cập cao đột ngột (như chạy flash sale marketing) để tránh hóa đơn API tăng sốc ngoài tầm kiểm soát.
```

### Câu 4 — Rủi ro lớn nhất của config được chọn?

```text
Rủi ro chính của Smart Mix là model tầm trung (Flash) có thể thỉnh thoảng hallucinate hoặc không xử lý tinh tế các đoạn chat rất phức tạp dài 6-7 lượt. Mitigation: Đặt giới hạn theo dõi (e.g. nếu chat kéo dài >5 lượt mà khách chưa hài lòng thì handoff qua nhân viên ngay lập tức để tiết kiệm token và bảo đảm trải nghiệm khách).
```

---

## Final answer — Recommendation in 1 paragraph

```text
Nhóm chúng tôi đề xuất triển khai hệ thống chatbot dựa trên cấu hình Smart Mix. Với mô hình Flash, việc tích hợp tra cứu web có chọn lọc cho Weather và Visa cùng với lưu giữ lịch sử chat 5 lượt mang lại sự cân bằng hoàn hảo. Chi phí tối đa vào mùa cao điểm chỉ đạt $689/tháng, tiết kiệm tới 96% so với sử dụng nhân viên chăm sóc khách hàng toàn thời gian ($18,000/tháng). Smart Mix không chỉ đảm bảo mức độ thông minh vừa đủ, cung cấp thông tin cập nhật theo thời gian thực mà còn giữ được độ trễ thấp ở mức chấp nhận được. Dù vẫn cần nhóm Sales xử lý intent Booking/Complaint, AI đã đóng vai trò xuất sắc trong việc phục vụ 24/7.
```

---

## Chuẩn bị Present (5 phút)

### Nhịp 0:00 – 0:30 — Base flow + 3 knobs đã chọn

Ai trình bày: Bang

Nói gì:

```text
Chào mọi người, bài toán nhóm mình tiếp cận là tối ưu chi phí nhưng không làm giảm đi chất lượng của một chatbot tư vấn du lịch. Flow hoạt động bắt đầu bằng việc phân loại intent bằng LLM, điều hướng theo 5 nhánh chính và sau cùng là quyết định mức độ model để generate text.
```

### Nhịp 0:30 – 1:00 — Config overview

Ai trình bày: Minh

Nói gì (đọc nhanh tên + knobs 3 configs):

```text
Nhóm đưa ra 3 phương án: 
1. Budget Bot (Rẻ, Không web, Last 3) 
2. Smart Mix (Tầm trung, Web linh hoạt, Last 5) 
3. Premium Concierge (Cực mạnh, Opus, Web toàn diện, Nhớ full context)
```

### Nhịp 1:00 – 2:00 — Cost comparison

Ai trình bày: Lan

Nói gì (chiếu bảng so sánh, highlight rẻ nhất / đắt nhất):

```text
Nhìn vào bảng so sánh, Budget Bot rẻ nhất chỉ $43 mùa cao điểm. Đắt nhất là Premium lên đến ~$4100. Đáng chú ý là chi phí giữa cấu hình rẻ và đắt nhất chênh lệch nhau tới 93 lần, chủ yếu do giá model và sự phình to context window.
```

### Nhịp 2:00 – 3:00 — Key insight

Ai trình bày: Bang

Nói gì (knob nào ảnh hưởng cost nhiều nhất + tại sao):

```text
Knob quyết định 90% chi phí là Model Tier, vì giá chênh từ 50x đến 60x giữa Flash Lite và Opus. Knob phụ là History Management, càng trò chuyện lâu, token tích lũy càng tăng khiến cost mỗi turn sau đắt hơn rất nhiều so với turn trước.
```

### Nhịp 3:00 – 4:30 — Recommendation + justification

Ai trình bày: Nhóm Trưởng (Minh)

Nói gì (đọc paragraph "Final answer" ở trên):

```text
Nhóm chúng tôi đề xuất triển khai hệ thống chatbot dựa trên cấu hình Smart Mix. Với mô hình Flash, việc tích hợp tra cứu web có chọn lọc cho Weather và Visa cùng với lưu giữ lịch sử chat 5 lượt mang lại sự cân bằng hoàn hảo. Chi phí tối đa vào mùa cao điểm chỉ đạt $689/tháng, tiết kiệm tới 96% so với sử dụng nhân viên ($18,000/tháng). Smart Mix không chỉ đảm bảo mức độ thông minh vừa đủ, cung cấp thông tin cập nhật theo thời gian thực mà còn giữ được độ trễ thấp. Dù vẫn cần nhóm Sales xử lý intent Booking/Complaint, AI đã đóng vai trò xuất sắc trong việc phục vụ 24/7.
```

### Nhịp 4:30 – 5:00 — Hardest question prep

Ai trình bày: Cả nhóm hỗ trợ

Nhóm dự đoán câu hỏi khó nhất sẽ bị hỏi là gì?

```text
"Nếu Smart Mix thất bại trong việc chốt đơn do thiếu khả năng reasoning như Premium, chi phí tiết kiệm được có đáng không so với revenue mất đi?"
```

Câu trả lời sẵn:

```text
"Hoàn toàn đáng vì intent Booking đã được lập trình handoff sang cho human (người thật) 100%. Nhiệm vụ của AI lúc này là tư vấn bước đầu chứ không phải chốt sales, do đó Premium là hơi dư thừa trừ trường hợp VIP."
```

---

## Q&A — 2 phút sau khi present xong

Sẵn sàng cho 1 câu từ class + 1 câu từ instructor. Không cần lo lắng — nếu chưa biết câu trả lời, nói "đây là điểm nhóm chưa nghĩ đến — sẽ tính lại sau buổi".

**3 câu instructor thường hỏi**:

1. *"Knob nào ảnh hưởng cost nhiều nhất trong config của nhóm? Tại sao?"*
2. *"Nếu provider tăng giá API ×2 → config của nhóm còn sống được không?"*
3. *"So với nhóm X (vừa present trước) — tại sao nhóm bạn chọn khác?"*

Suy nghĩ trước câu trả lời ngắn:

```text
1. Model Tier ảnh hưởng cực mạnh vì unit cost lệch từ 20-50 lần giữa các provider.
2. Vẫn an toàn vì savings hiện đang ở mức 96%, nhân 2 chi phí thì vẫn là món hời so với human cost. Cùng lắm ta giới hạn History lại.
3. Chúng tôi tập trung vào Smart Mix thay vì Extreme Budget vì mảng Du Lịch quan trọng ở trải nghiệm người dùng, thông tin visa sai lệch sẽ gây hậu quả rất lớn.
```

---

## Bảng kiểm cuối cùng — trước 12:00 Pens Down

- [x] Đã trả lời 4 câu PM (Recommend / Savings / Threshold / Risk)
- [x] Final answer paragraph viết gọn (5–7 câu)
- [x] Phân công 5 nhịp present cho mỗi thành viên
- [x] Có sẵn câu trả lời cho 3 câu Q&A dự đoán
- [x] Comparison table có sẵn để chiếu / chuyền tay khi present
- [x] Repo đã commit + push (sẽ nộp link sau buổi học)

---

## Sau buổi học

1. **Commit + push repo** với tất cả file đã điền.
2. **Dán link repo** vào Discord `#day27-evidence-boards` trước 23:59.
3. **Chuẩn bị cho D28**: peer review giữa các nhóm — sẽ bị hỏi câu chất vấn khó hơn instructor. Polish thêm bảng + recommendation tối nay.

*Hôm nay bạn chứng minh bằng số. Ngày mai bạn bảo vệ bằng logic.*
