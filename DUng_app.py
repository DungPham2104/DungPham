

import streamlit as st
import pandas as pd

# Sample data for laptops
laptops = [
    {"Brand": "Dell", "Model": "XPS 13", "Price": 25000000, "RAM": "16GB", "Storage": "512GB SSD"},
    {"Brand": "HP", "Model": "Spectre x360", "Price": 27000000, "RAM": "16GB", "Storage": "1TB SSD"},
    {"Brand": "Apple", "Model": "MacBook Air M2", "Price": 32000000, "RAM": "8GB", "Storage": "256GB SSD"},
    {"Brand": "Asus", "Model": "ROG Zephyrus", "Price": 38000000, "RAM": "32GB", "Storage": "1TB SSD"},
    {"Brand": "Lenovo", "Model": "ThinkPad X1 Carbon", "Price": 29000000, "RAM": "16GB", "Storage": "512GB SSD"}
]

df = pd.DataFrame(laptops)

# App title
st.title("💻 Web Bán Laptop")

# Sidebar filters
st.sidebar.header("🔍 Bộ lọc tìm kiếm")
brand_filter = st.sidebar.multiselect("Hãng sản xuất", options=df["Brand"].unique(), default=df["Brand"].unique())
max_price = st.sidebar.slider("Giá tối đa (VNĐ)", 20000000, 50000000, 40000000)

# Apply filters
filtered_df = df[(df["Brand"].isin(brand_filter)) & (df["Price"] <= max_price)]

# Display products
st.subheader("🛒 Danh sách Laptop")
st.dataframe(filtered_df)

# Simulate order form
st.subheader("📦 Đặt hàng")
with st.form("order_form"):
    selected_model = st.selectbox("Chọn mẫu laptop", filtered_df["Model"])
    customer_name = st.text_input("Họ tên")
    customer_email = st.text_input("Email")
    customer_address = st.text_area("Địa chỉ giao hàng")
    submit = st.form_submit_button("Đặt mua")

    if submit:
        st.success(f"Cảm ơn {customer_name}! Đơn hàng {selected_model} của bạn đã được ghi nhận.")

# Footer
st.markdown("---")
st.markdown("© 2025 Web Bán Laptop - Streamlit Demo by [YourName]")


