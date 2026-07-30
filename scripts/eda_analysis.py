import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("../dataset/Cleaned_Sales_Dataset.xlsx")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Columns
print("\n========== COLUMN NAMES ==========")
print(df.columns)

# Info
print("\n========== DATASET INFO ==========")
print(df.info())

# Statistics
print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Unique values
print("\n========== UNIQUE VALUES ==========")
print(df.nunique())

# ==========================
# AGE DISTRIBUTION HISTOGRAM
# ==========================

plt.figure(figsize=(8,5))

plt.hist(df['Age'], bins=10, edgecolor='black')

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.savefig("../images/age_distribution.png")

plt.show()

# ==========================
# GENDER DISTRIBUTION BAR CHART
# ==========================

plt.figure(figsize=(6,4))

df['Gender'].value_counts().plot(
    kind='bar',
    color=['skyblue', 'lightpink']
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.savefig("../images/gender_distribution.png")

plt.show()

# ==========================
# CATEGORY DISTRIBUTION
# ==========================

plt.figure(figsize=(8,5))

df['Category'].value_counts().plot(
    kind='bar',
    color='lightgreen',
    edgecolor='black'
)

plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig("../images/category_distribution.png")

plt.show()

# ==========================
# CITY-WISE SALES
# ==========================

city_sales = df.groupby('City')['Total_Sales'].sum()

plt.figure(figsize=(10,5))

city_sales.plot(
    kind='bar',
    color='orange',
    edgecolor='black'
)

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("../images/city_sales.png")

plt.show()

# ==========================
# SALES BY CATEGORY
# ==========================

category_sales = df.groupby('Category')['Total_Sales'].sum()

plt.figure(figsize=(8,5))

category_sales.plot(
    kind='bar',
    color='purple',
    edgecolor='black'
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("../images/category_sales.png")

plt.show()

# ==========================
# MONTHLY SALES TREND
# ==========================

df['Month'] = df['Order_Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(12,5))

monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../images/monthly_sales.png")

plt.show()

# ==========================
# CORRELATION HEATMAP
# ==========================

plt.figure(figsize=(6,5))

sns.heatmap(
    df[['Age','Quantity','Unit_Price','Total_Sales']].corr(),
    annot=True,
    cmap='Blues'
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("../images/correlation_heatmap.png")

plt.show()