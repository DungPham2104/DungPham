import streamlit as st
import pandas as pd
import plotly.express as px

# Dữ liệu mẫu
data = [
    {"Brand": "Dell", "Model": "XPS 13", "Price": 25000000, "RAM": "16GB", "Storage": "512GB SSD", "Sold": 120},
    {"Brand": "HP", "Model": "Spectre x360", "Price": 27000000, "RAM": "16GB", "Storage": "1TB SSD", "Sold": 95},
    {"Brand": "Apple", "Model": "MacBook Air M2", "Price": 32000000, "RAM": "8GB", "Storage": "256GB SSD", "Sold": 150},
    {"Brand": "Asus", "Model": "ROG Zephyrus", "Price": 38000000, "RAM": "32GB", "Storage": "1TB SSD", "Sold": 60},
    {"Brand": "Lenovo", "Model": "ThinkPad X1 Carbon", "Price": 29000000, "RAM": "16GB", "Storage": "512GB SSD", "Sold": 80},
    {"Brand": "Dell", "Model": "Inspiron 15", "Price": 22000000, "RAM": "8GB", "Storage": "256GB SSD", "Sold": 110},
    {"Brand": "HP", "Model": "Pavilion 14", "Price": 21000000, "RAM": "8GB", "Storage": "512GB SSD", "Sold": 105}
]

df = pd.DataFrame(data)

# Cấu hình giao diện
st.set_page_config(page_title="Laptop Sales Dashboard", layout="wide")
st.title("📊 Web Bán Laptop - Trực Quan Hóa Dữ Liệu")

# Sidebar - Bộ lọc
st.sidebar.header("🔍 Bộ lọc")
selected_brands = st.sidebar.multiselect("Chọn hãng laptop", options=df["Brand"].unique(), default=df["Brand"].unique())
max_price = st.sidebar.slider("Giá tối đa (VNĐ)", 15000000, 40000000, 35000000)

# Áp dụng bộ lọc
filtered_df = df[(df["Brand"].isin(selected_brands)) & (df["Price"] <= max_price)]

# Hiển thị dữ liệu
st.subheader("📋 Danh sách sản phẩm đã lọc")
st.dataframe(filtered_df)

# Biểu đồ 1: Tổng số sản phẩm bán ra theo hãng
st.subheader("📈 Biểu đồ số lượng bán ra theo hãng")
sales_by_brand = filtered_df.groupby("Brand")["Sold"].sum().reset_index()
fig1 = px.bar(sales_by_brand, x="Brand", y="Sold", title="Sản phẩm bán ra theo Hãng", color="Brand", text="Sold")
st.plotly_chart(fig1, use_container_width=True)

# Biểu đồ 2: Phân bố số lượng bán theo Model
st.subheader("📊 Biểu đồ phân phối doanh số theo mẫu laptop")
fig2 = px.pie(filtered_df, names="Model", values="Sold", title="Tỉ lệ bán theo mẫu")
st.plotly_chart(fig2, use_container_width=True)

# Biểu đồ 3: Mối quan hệ giữa Giá và Số lượng bán
st.subheader("💡 Biểu đồ Giá vs Số lượng bán")
fig3 = px.scatter(filtered_df, x="Price", y="Sold", color="Brand", size="Sold",
                  hover_data=["Model"], title="Giá và số lượng bán theo sản phẩm")
st.plotly_chart(fig3, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("📍 © 2025 Dashboard Web Bán Laptop - Made with ❤️ using Streamlit")



