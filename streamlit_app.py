
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.metrics import mean_squared_error, r2_score

# Dữ liệu giả định: bạn cần load hoặc truyền df, X, y_test, y_pred, model
# df = pd.read_csv('your_dataset.csv')

st.title("Phân tích dữ liệu sản phẩm và mô hình dự đoán")

# 1. Ma trận tương quan
st.header("1. Ma trận tương quan")
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.heatmap(df[['discounted_price', 'discount_percentage', 'rating_count', 'rating']].corr(),
            annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax1)
st.pyplot(fig1)

# 2. Phân phối giá sau giảm
st.header("2. Phân phối giá sau giảm")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.histplot(df['discounted_price'], bins=30, kde=True, color='#1f77b4', ax=ax2)
ax2.set_xlabel("Giá (INR)")
st.pyplot(fig2)

# 3. Điểm đánh giá trung bình theo danh mục
st.header("3. Điểm đánh giá trung bình theo danh mục")
fig3, ax3 = plt.subplots(figsize=(12, 6))
avg_rating = df.groupby('category_level_1')['rating'].mean().sort_values()
sns.barplot(x=avg_rating.index, y=avg_rating.values, color='#ff7f0e', ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig3)

# 4. Mối quan hệ giữa mức giảm giá và số lượng đánh giá
st.header("4. Mối quan hệ giữa mức giảm giá và số lượng đánh giá")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='discount_percentage', y='rating_count', data=df, color='#2ca02c', alpha=0.6, ax=ax4)
st.pyplot(fig4)

# 5. Top 5 sản phẩm có số lượng đánh giá cao nhất
st.header("5. Top 5 sản phẩm có số lượng đánh giá cao nhất")
top_products = df.nlargest(5, 'rating_count')[['product_name', 'rating_count']]
fig5, ax5 = plt.subplots(figsize=(12, 6))
sns.barplot(x='rating_count', y='product_name', data=top_products, color='#d62728', ax=ax5)
st.pyplot(fig5)

# 6. Giá sau giảm vs Điểm đánh giá
st.header("6. Giá sau giảm vs Điểm đánh giá")
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='discounted_price', y='rating', data=df, color='#9467bd', alpha=0.6, ax=ax6)
st.pyplot(fig6)

# 7. Đánh giá mô hình
st.header("7. Đánh giá mô hình dự đoán")
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
st.write(f"**Mean Squared Error (MSE):** {mse:.4f}")
st.write(f"**R² Score:** {r2:.4f}")

# Hệ số đặc trưng
st.subheader("Hệ số đặc trưng")
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
st.dataframe(coefficients)

# 8. So sánh giá trị thực tế và dự đoán
st.header("8. So sánh giá trị thực tế và dự đoán")
fig7, ax7 = plt.subplots(figsize=(10, 6))
ax7.scatter(y_test, y_pred, color='#1f77b4', alpha=0.6)
ax7.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
st.pyplot(fig7)

# 9. Phân phối lỗi dự đoán
st.header("9. Phân phối lỗi dự đoán")
errors = y_test - y_pred
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.histplot(errors, bins=30, kde=True, color='#ff7f0e', ax=ax8)
st.pyplot(fig8)
