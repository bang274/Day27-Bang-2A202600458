# 00 · User Journey Simulation — Đóng vai Tourist

> **Mục tiêu**: Trước khi tính chi phí, nhóm phải hình dung được khách hàng thật sự hỏi gì, hỏi như thế nào, và 1 conversation thực tế trông ra sao.
>
> **Thời gian**: 8 phút (trong 15 phút phần Setup)

---

## Tại sao phải làm bước này?

Nếu nhóm bắt đầu tính cost mà chưa biết tourist hỏi gì → mọi con số chỉ là lý thuyết. Bước này buộc nhóm "chạm" sản phẩm trước khi mở Excel.

---

## Bước 1 — Mỗi người đóng vai 1 tourist (4 phút)

Tưởng tượng mình là 1 khách du lịch nước ngoài đang plan trip Việt Nam. Bạn vừa mở website công ty du lịch, thấy có chatbot ở góc màn hình. Bạn sẽ hỏi gì?

Trước khi viết, tự hỏi:

- Mình từ đâu đến? Mỹ, Anh, Hàn, Nhật, Úc?
- Đi 1 mình hay đi nhóm? Budget khoảng bao nhiêu?
- Đã biết gì về Việt Nam? Lần đầu đến hay đã đến rồi?
- Mình lo lắng điều gì nhất? (visa, an toàn, ngôn ngữ, thời tiết, ẩm thực, lừa đảo...)

Viết **5–7 câu hỏi bằng tiếng Anh** mình sẽ thật sự gửi cho chatbot. Viết câu hỏi tự nhiên, đúng giọng tourist — không phải đặt câu hỏi "nghe có vẻ technical".

→ Mỗi người viết vào ô dưới (chưa có gì sẵn — đừng nhìn người bên cạnh):

### Tourist #1 (Tên thành viên: Bang)

```text
1. Hi there! Do I need a visa if I'm visiting from the US for two weeks?
2. What are the top places to visit in Northern Vietnam?
3. What will the weather be like in Sapa in November?
4. I want to book a 3-day Halong Bay cruise, what are the options?
5. How do I get from Noi Bai airport to the Old Quarter in Hanoi?
```

### Tourist #2 (Tên thành viên: Minh)

```text
1. I’m arriving from the UK next month, is the e-visa process fast?
2. Are there any cool events happening in Ho Chi Minh City this weekend?
3. Could you recommend a good local street food tour in Hoi An?
4. My flight got delayed and I missed the tour bus, what do I do?
5. What is the average cost of a nice hotel in Da Nang?
```

### Tourist #3 (Tên thành viên: Lan)

```text
1. Is it safe for a solo female traveler to walk around Hanoi at night?
2. Can you help me book a sleeper train from Hanoi to Hue?
3. The tour guide didn't show up for our Sapa trekking tour! Please help.
4. What's the weather like in Phu Quoc during August?
5. Do Australian citizens get visa exemption in Vietnam?
```

---

## Bước 2 — Gom lại và phân loại (4 phút)

Cả nhóm chụm vào, gom tất cả câu hỏi lại. Trước khi điền bảng, thảo luận 1 phút:

- Có câu hỏi nào lặp lại giữa các tourist không?
- Có chủ đề nào không ai trong nhóm nghĩ tới ban đầu nhưng quan trọng?
- Câu nào chatbot có thể trả lời được? Câu nào cần chuyển sang nhân viên thật?

5 intent có sẵn (tham khảo `cost-reference-card.md` mục 2):

- **Visa/Policy** — chính sách, thủ tục nhập cảnh
- **Điểm đến/Guide** — gợi ý đi đâu, làm gì, ăn gì
- **Thời tiết/Sự kiện** — info real-time
- **Tour/Booking** — đặt vé, đặt tour, đặt phòng → chuyển sales
- **Khiếu nại** — phàn nàn → chuyển manager

Sau khi gom, điền bảng phân loại:

| # | Câu hỏi (1 dòng) | Intent thuộc loại nào | Cần bao nhiêu lượt chat để xong? | Bot trả lời hay chuyển người? |
|---|---|---|---|---|
| 1 | Visa requirement for US citizen (2 weeks) | Visa/Policy | 3 | ☑ Bot · □ Người |
| 2 | Top places in Northern Vietnam | Điểm đến/Guide | 4 | ☑ Bot · □ Người |
| 3 | Sapa weather in November | Thời tiết/Sự kiện | 2 | ☑ Bot · □ Người |
| 4 | Book a 3-day Halong Bay cruise | Tour/Booking | 1 | □ Bot · ☑ Người |
| 5 | UK e-visa process time | Visa/Policy | 3 | ☑ Bot · □ Người |
| 6 | HCMC events this weekend | Thời tiết/Sự kiện | 3 | ☑ Bot · □ Người |
| 7 | Missed tour bus due to flight delay | Khiếu nại | 1 | □ Bot · ☑ Người |
| 8 | Book sleeper train Hanoi to Hue | Tour/Booking | 1 | □ Bot · ☑ Người |
| 9 | Tour guide didn't show up in Sapa | Khiếu nại | 1 | □ Bot · ☑ Người |
| 10 | Australian visa exemption in Vietnam | Visa/Policy | 3 | ☑ Bot · □ Người |

---

## Bước 3 — Rút insight cho nhóm (cuối phần Setup)

Trả lời nhanh 4 câu — sẽ dùng lại ở các bước sau:

**Tổng số câu hỏi nhóm gom được**:

```text
15 câu hỏi (nhưng phân loại 10 câu tiêu biểu)
```

**Phân bố intent thực tế của nhóm** (% mỗi intent):

```text
Guide: 30%
Visa: 30%
Weather: 20%
Booking: 10%
Khiếu nại: 10%
```

**Số lượt chat trung bình để xong 1 chủ đề**:

```text
Khoảng 3-4 lượt cho hỏi info, và chỉ 1 lượt cho booking/khiếu nại trước khi handoff.
```

**Đối chiếu với đề bài** (Scenario A = 4 lượt, Scenario B = 7 lượt):

```text
Khá hợp lý vì trong low season khách chủ yếu hỏi cơ bản (khoảng 3-4 lượt). Trong high season khách có thể thảo luận sâu hơn về lịch trình, dẫn đến 7 lượt.
```

**Insight bất ngờ — điều gì nhóm chỉ hiểu sau khi đóng vai?**

```text
Khách hàng thường có intent rõ ràng. Booking và Khiếu nại thường xảy ra rất nhanh trong 1 lượt (khách không kiên nhẫn chat với AI) nên chi phí cho AI trong các intent này gần như bằng 0. Trong khi đó, nhóm Guide và Visa tốn khá nhiều context để bot hiểu đúng situation.
```

---

## Bảng kiểm trước khi sang file tiếp theo

- [x] Mỗi người trong nhóm đã viết ≥5 câu hỏi tourist
- [x] Đã gom + phân loại intent cho ≥10 câu (bảng trên)
- [x] Đã có phân bố intent % của nhóm (so với đề bài)
- [x] Có ít nhất 1 insight về cách tourist thật sự dùng chatbot

Xong → mở `01-base-flow.md`.
