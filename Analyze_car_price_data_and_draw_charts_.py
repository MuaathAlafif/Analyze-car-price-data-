import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# إنشاء البيانات باستخدام numpy
np.random.seed(0)
car_brands = ['Toyota', 'Honda', 'BMW', 'Mercedes', 'Ford', 'Chevrolet']
prices = np.random.randint(15000, 70000, size=100)
mileage = np.random.randint(5000, 150000, size=100)
brands = np.random.choice(car_brands, size=100)

# إنشاء DataFrame باستخدام pandas
df = pd.DataFrame({
    'Brand': brands,
    'Price': prices,
    'Mileage': mileage
})

# عرض أول 5 صفوف من البيانات
print(df.head())

# تحليل بيانات الأسعار باستخدام pandas
average_price_per_brand = df.groupby('Brand')['Price'].mean()
print("\nمتوسط سعر السيارات لكل علامة تجارية:")
print(average_price_per_brand)

# رسم البيانات باستخدام matplotlib
plt.figure(figsize=(10, 6))

# رسم توزيع الأسعار
plt.subplot(1, 2, 1)
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Car Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')

# رسم الأسعار مقابل الأميال
plt.subplot(1, 2, 2)
plt.scatter(mileage, prices, c='green', alpha=0.5)
plt.title('Car Prices vs. Mileage')
plt.xlabel('Mileage')
plt.ylabel('Price ($)')

plt.tight_layout()
plt.show()