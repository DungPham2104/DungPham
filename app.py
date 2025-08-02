
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Giả sử bạn đã có dữ liệu df, X, y_test, y_pred, model
# df = pd.read_csv('your_dataset.csv')

# Biểu đồ 1: Ma trận tương quan
plt.figure(figsize=(8, 6))
sns.heatmap(df[['discounted_price', 'discount_percentage', 'rating_count', 'rating']].corr(), 
            annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Ma trận tương quan')
plt.show()

# Biểu đồ 2: Phân phối giá sau giảm
plt.figure(figsize=(10, 6))
sns.histplot(df['discounted_price'], bins=30, kde=True, color='#1f77b4')
plt.title('Phân phối giá sau giảm', fontsize=14)
plt.xlabel('Giá (INR)', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Biểu đồ 3: Điểm đánh giá trung bình theo danh mục
plt.figure(figsize=(12, 6))
avg_rating = df.groupby('category_level_1')['rating'].mean().sort_values()
sns.barplot(x=avg_rating.index, y=avg_rating.values, color='#ff7f0e')
plt.title('Điểm đánh giá trung bình theo danh mục', fontsize=14)
plt.xlabel('Danh mục', fontsize=12)
plt.ylabel('Điểm đánh giá trung bình', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y', alpha=0.3)
plt.show()

# Biểu đồ 4: Mối quan hệ giữa mức giảm giá và số lượng đánh giá
plt.figure(figsize=(10, 6))
sns.scatterplot(x='discount_percentage', y='rating_count', data=df, color='#2ca02c', alpha=0.6)
plt.title('Mức giảm giá vs Số lượng đánh giá', fontsize=14)
plt.xlabel('Mức giảm giá (%)', fontsize=12)
plt.ylabel('Số lượng đánh giá', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Biểu đồ 5: Top 5 sản phẩm có số lượng đánh giá cao nhất
top_products = df.nlargest(5, 'rating_count')[['product_name', 'rating_count']]
plt.figure(figsize=(12, 6))
sns.barplot(x='rating_count', y='product_name', data=top_products, color='#d62728')
plt.title('Top 5 sản phẩm có số lượng đánh giá cao nhất', fontsize=14)
plt.xlabel('Số lượng đánh giá', fontsize=12)
plt.ylabel('Tên sản phẩm', fontsize=12)
plt.grid(True, axis='x', alpha=0.3)
plt.show()

# Biểu đồ 6: Giá sau giảm vs Điểm đánh giá
plt.figure(figsize=(10, 6))
sns.scatterplot(x='discounted_price', y='rating', data=df, color='#9467bd', alpha=0.6)
plt.title('Giá sau giảm vs Điểm đánh giá', fontsize=14)
plt.xlabel('Giá sau giảm (INR)', fontsize=12)
plt.ylabel('Điểm đánh giá', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Hệ số đặc trưng
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nHệ số đặc trưng:")
print(coefficients)

# Biểu đồ 7: Giá trị thực tế vs Dự đoán
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='#1f77b4', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title('Giá trị thực tế vs Dự đoán (Rating)', fontsize=14)
plt.xlabel('Rating thực tế', fontsize=12)
plt.ylabel('Rating dự đoán', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Biểu đồ 8: Phân phối lỗi dự đoán
errors = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(errors, bins=30, kde=True, color='#ff7f0e')
plt.title('Phân phối lỗi dự đoán', fontsize=14)
plt.xlabel('Lỗi (Rating thực tế - Dự đoán)', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
