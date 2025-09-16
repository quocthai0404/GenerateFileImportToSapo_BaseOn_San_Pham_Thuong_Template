# 🚀 Product Export & Import Guide

## 1️⃣ Export product data từ API
- API endpoint:  
  ```
  /api/products/paginateProducts?limit=10000&page=1&published=true
  ```
- Lưu dữ liệu trả về vào file:  
  ```
  product_export.json
  ```
- Đặt file **product_export.json** ở cùng cấp với thư mục **root** trong project.  

📂 Ví dụ:
```
read_json_paste_to_sapo_excel_pattern/
│── product_export.json
```

---

## 2️⃣ Chạy lệnh để xử lý dữ liệu
Trong terminal, chạy lệnh sau:

```bash
py main.py
```

---

## 3️⃣ Mở file kết quả
- Sau khi chạy, file kết quả sẽ được tạo (ví dụ: `result.xlsx`).
- Mở file Excel này.

---

## 4️⃣ Copy dữ liệu sang file import
1. Trong file kết quả vừa mở, chọn từ **ô đầu tiên (B2)** đến **ô cuối cùng (góc phải dưới cùng)**.  
   *(Hình minh họa: top-left → bottom-right)*  

   ![select-range](https://github.com/user-attachments/assets/68767959-566d-44bb-abf5-f4a3fc6072d0)

2. Copy toàn bộ vùng dữ liệu.

3. Paste vào file **pattern_import_product.xlsx** theo đúng định dạng.

---

✅ Vậy là bạn đã chuẩn bị xong file import sản phẩm.
