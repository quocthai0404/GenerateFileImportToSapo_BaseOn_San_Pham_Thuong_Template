import openpyxl
from typing import List
from models.product import Product


def brand_text(b):
    """Return a string for brand whether b is str, dict, or dataclass-like with .text/.value."""
    if b is None:
        return ""
    if isinstance(b, dict):
        return b.get("text") or b.get("value") or str(b)
    # dataclass or object
    if hasattr(b, "text") or hasattr(b, "value"):
        try:
            return getattr(b, "text", None) or getattr(b, "value", None) or str(b)
        except Exception:
            return str(b)
    return str(b)

def export_products_to_sapo_normal_product(products: List['Product'], filename: str):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "SapoImport"


    headers = [
        "RowType",
        "Đường dẫn/Alias", 
        "Tên sản phẩm*",
        "Mô tả sản phẩm",
        "Nhãn hiệu",
        "Loại sản phẩm",
        "Tags", 
        "Yêu cầu vận chuyển",  #Có, Không
        "Hiển thị*", #Có, Không
        "Thuộc tính 1", 
        "Giá trị thuộc tính 1",
        "Thuộc tính 2",
        "Giá trị thuộc tính 2",
        "Thuộc tính 3",
        "Giá trị thuộc tính 3",
        "Áp dụng thuế",  #Có, Không
        "Mã SKU", 
        "Barcode", 
        "Đơn vị tính", 
        "Ảnh đại diện", 
        "Chú thích ảnh", 
        "Thẻ tiêu đề(SEO Title)", 
        "Thẻ mô tả(SEO Description)", 
        "Mô tả ngắn", 
        "Quản lý kho", 
        "Quản lý lô - HSD", 
        "Số ngày cảnh báo trước hết hạn", 
        "Khối lượng", 
        "Đơn vị khối lượng",  #g, kg, oz, lb
        "Ảnh phiên bản", 
        "Cho phép tiếp tục mua khi hết hàng", 
        "Giá", 
        "Giá so sánh",
        "Giá vốn", 
        # "Tên chi nhánh 1_Tồn kho", 
        # "Tên chi nhánh 2_Tồn kho", 
        # "Id phiên bản"

    ]
    ws.append(headers)

    

    for idx, p in enumerate(products, start=1):
        # SKU gốc cho product lớn
        base_sku = f"TEST{idx:04d}"  # TEST0001, TEST0002, ...

        tags_str = ", ".join(p.tags) if p.tags else ""

        # lấy ảnh đại diện product

        first_image = p.main_image
        if isinstance(p.main_image, list):
            first_image = p.main_image[0] if p.main_image else None
        else:
            first_image = p.main_image

        # --- Dòng PRODUCT ---
        # --- Dòng PRODUCT ---
        ws.append([
            "PRODUCT",
            p.alias,
            p.name,
            p.content or "",
            brand_text(p.brand),
            p.product_type,
            p.categories or "",
            "Có",
            "Có",
            "Thuộc tính",
            p.name,
            "", "", "", "",
            "Có",
            base_sku,
            "",
            "cái",
            first_image,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "Có",
            p.price_promotion,
            p.selling_price,
            ""
        ])

        # --- Dòng UNIT ---
        for u_idx, u in enumerate(p.units, start=1):
            unit_sku = f"{base_sku}-{u_idx}"

            unit_image = None
            if isinstance(u.main_image, list):
                unit_image = u.main_image[0] if u.main_image else None
            else:
                unit_image = u.main_image

            ws.append([
                "UNIT",
                "",
                "",
                "",
                "", 
                "",
                "",
                "",
                "",
                "",
                u.variant_unit_name,
                "", "", "", "",
                "Có",
                unit_sku,
                "",
                "cái",
                unit_image,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "Có",
                u.price_promotion,
                u.selling_price,
                ""
            ])


    wb.save(filename)
    print(f"Đã export {len(products)} sản phẩm ra file {filename} (sheet Products & Units)")