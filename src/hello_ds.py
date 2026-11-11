import pandas as pd

sales = pd.DataFrame({
    "region": ["Norte", "Norte", "Sur"],
    "revenue": [1200, 800, 950],
    "orders": [12, 8, 10],
})

summary = (sales.groupby("region", as_index=False)
           .agg(revenue=("revenue", "sum"),
                orders=("orders", "sum")))
summary["average_order_value"] = summary["revenue"] / summary["orders"]
print(summary)