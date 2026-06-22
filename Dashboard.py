import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('car_selling_dataset.csv')

# 2. Performance Summary Metrics
total_revenue = df[df['Status'] == 'Sold']['Selling_Price_Lakhs'].sum()
avg_price = df['Selling_Price_Lakhs'].mean()
total_cars_sold = df[df['Status'] == 'Sold']['Car_ID'].count()

print("--- CAR SELLING METRICS SUMMARY ---")
print(f"Total Revenue Generated: ₹{total_revenue:.2f} Lakhs")
print(f"Average Car Listing Price: ₹{avg_price:.2f} Lakhs")
print(f"Total Number of Cars Sold: {total_cars_sold}\n")

# 3. Setting Up Dashboard Visualization Plots
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")

# Plot 1: Top Brands by Volume
plt.subplot(2, 2, 1)
sns.countplot(data=df, x='Brand', order=df['Brand'].value_counts().index, palette='viridis')
plt.title('Car Counts by Brand')
plt.xticks(rotation=45)

# Plot 2: Average Selling Price by Fuel Type
plt.subplot(2, 2, 2)
sns.barplot(data=df, x='Fuel_Type', y='Selling_Price_Lakhs', estimator=lambda x: sum(x)/len(x), palette='coolwarm')
plt.title('Avg Price vs Fuel Type')

# Plot 3: Transmission Distribution (Manual vs Automatic)
plt.subplot(2, 2, 3)
df['Transmission'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff','#99ff99'], startangle=90)
plt.title('Transmission Market Share')
plt.ylabel('')

# Plot 4: Price vs Kilometers Driven
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x='Kms_Driven', y='Selling_Price_Lakhs', hue='Status', alpha=0.7)
plt.title('Price Distribution vs Kms Driven')

plt.tight_layout()
plt.savefig('car_sales_dashboard.png', dpi=300)
print("Dashboard saved successfully as 'car_sales_dashboard.png'!")