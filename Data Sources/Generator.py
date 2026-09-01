import pandas as pd

# Orders
orders = pd.DataFrame({
    'Order_ID': [1001, 1002, 1003, 1004, 1005, 1006],
    'Customer_ID': [1, 2, 3, 1, None, 2],
    'Amount': [250.00, 180.50, None, 420.00, 150.00, 310.00],
    'Order_Date': ['2026-08-01', '2026-08-02', '2026-08-03', '2026-08-04', '2026-08-05', '2026-08-06']
})

# Customers
customers = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'Customer_Name': ['ahmed ali', 'sara ibrahim', 'mohamed hassan'],
    'City': ['Cairo', 'Alexandria', 'Giza']
})

# حفظ الملفات
orders.to_excel("orders.xlsx", index=False)
customers.to_excel("customers.xlsx", index=False)

print("Done")