import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Tiêu đề ứng dụng
st.title("Trực Quan Hóa Dữ Liệu Web Bán Laptop")

# Tạo dữ liệu mẫu (thay thế bằng dữ liệu crawl từ web nếu có)
data = {
    "Thương hiệu": ["Dell", "HP", "Lenovo", "Asus", "Acer", "MacBook", "Dell", "HP", "Asus", "Lenovo"],
    "Giá (triệu VND)": [15.5, 12.9, 14.2, 18.7, 11.5, 29.9, 20.5, 13.8, 17.9, 16.4],
    "RAM (GB)": [8, 4, 8, 16, 4, 16, 8, 8, 16, 8],
    "CPU": ["Intel i5", "Intel i3", "Intel i5", "Intel i7", "Intel i3", "Apple M1", "Intel i7", "Intel i5", "Intel i7", "Intel i5"],
    "Dung lượng ổ cứng (GB)": [512, 256, 512, 1000, 256, 512, 512, 256, 1000, 512],
    "Điểm đánh giá": [4.2, 3.8, 4.0, 4.5, 3.7, 4.8, 4.3, 3.9, 4.4, 4.1]
}
df = pd.DataFrame(data)

# Hiển thị dữ liệu gốc
st.subheader("Dữ liệu Laptop")
st.dataframe(df)

# Sidebar để lọc dữ liệu
st.sidebar.header("Bộ lọc")
brand_filter = st.sidebar.multiselect("Chọn thương hiệu", options=df["Thương hiệu"].unique(), default=df["Thương hiệu"].unique())
min_price, max_price = st.sidebar.slider("Khoảng giá (triệu VND)", float(df["Giá (triệu VND)"].min()), float(df["Giá (triệu VND)"].max()), (float(df["Giá (triệu VND)"].min()), float(df["Giá (triệu VND)"].max())))
ram_filter = st.sidebar.multiselect("RAM (GB)", options=df["RAM (GB)"].unique(), default=df["RAM (GB)"].unique())

# Lọc dữ liệu
filtered_df = df[
    (df["Thương hiệu"].isin(brand_filter)) &
    (df["Giá (triệu VND)"] >= min_price) &
    (df["Giá (triệu VND)"] <= max_price) &
    (df["RAM (GB)"].isin(ram_filter))
]

# Hiển thị dữ liệu đã lọc
st.subheader("Dữ liệu đã lọc")
st.dataframe(filtered_df)

# Trực quan hóa
st.subheader("Phân tích dữ liệu")

# Biểu đồ phân bố giá theo thương hiệu
fig1 = px.box(filtered_df, x="Thương hiệu", y="Giá (triệu VND)", title="Phân bố giá theo thương hiệu")
st.plotly_chart(fig1)

# Biểu đồ phân tán giá và điểm đánh giá
fig2 = px.scatter(filtered_df, x="Giá (triệu VND)", y="Điểm đánh giá", color="Thương hiệu", size="RAM (GB)", title="Giá vs Điểm đánh giá")
st.plotly_chart(fig2)

# Biểu đồ số lượng laptop theo CPU
fig3 = px.histogram(filtered_df, x="CPU", title="Số lượng laptop theo CPU")
st.plotly_chart(fig3)

# Thống kê cơ bản
st.subheader("Thống kê")
st.write(f"Giá trung bình: {filtered_df['Giá (triệu VND)'].mean():.2f} triệu VND")
st.write(f"RAM trung bình: {filtered_df['RAM (GB)'].mean():.2f} GB")
st.write(f"Điểm đánh giá trung bình: {filtered_df['Điểm đánh giá'].mean():.2f}")

# Hướng dẫn
st.markdown("""
### Hướng dẫn sử dụng
- Sử dụng bộ lọc ở thanh bên trái để chọn thương hiệu, khoảng giá, và RAM.
- Xem các biểu đồ để phân tích giá, điểm đánh giá, và cấu hình.
- Dữ liệu hiện tại là mẫu, có thể thay bằng dữ liệu crawl từ web.
""")


