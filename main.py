from product_reader import load_products
from export_excel import (
    export_products_to_sapo_normal_product,
)
from datetime import datetime
import sys



if __name__ == "__main__":
    # allow passing filename via CLI, default to product_export.json
    input_file = sys.argv[1] if len(sys.argv) > 1 else "product_export.json"
    products = load_products(input_file)

    # Export ra Excel (timestamped filenames)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename_normal = f"sapo_normal_{ts}.xlsx"

    # Call the normal Sapo exporter
    export_products_to_sapo_normal_product(products, filename_normal)

    print("Done. Files: ", filename_normal)