# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Diwali Sales Data_Row.csv")

# Step 1: Data Cleaning
# Drop unnecessary columns
df.drop(["Status", "unnamed1"], axis=1, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'Amount' to integer type
df["Amount"] = df["Amount"].astype("int")

# Step 2: Gender Analysis
# Count plot for Gender
ax = sns.countplot(x="Gender", data=df)
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution of Buyers")
plt.show()

# Bar plot for total amount spent by Gender
sales_gender = df.groupby("Gender", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sns.barplot(x="Gender", y="Amount", data=sales_gender)
plt.title("Total Amount Spent by Gender")
plt.show()
## Female buyers are dominant in both purchase count and amount spent.

# Step 3: Age Group Analysis
# Count plot for Age Group with Gender
ax = sns.countplot(x="Age Group", data=df, hue="Gender")
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Age Group Distribution by Gender")
plt.show()

# Bar plot for total amount spent by Age Group
sales_age = df.groupby("Age Group", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sns.barplot(x="Age Group", y="Amount", data=sales_age)
plt.title("Total Amount Spent by Age Group")
plt.show()
## The age group 26-35 accounts for the highest spending.

# Step 4: State Analysis
# Top 10 states by Orders
sales_state_orders = df.groupby("State", as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False).head(10)
plt.figure(figsize=(15, 6))
ax = sns.barplot(x="State", y="Orders", data=sales_state_orders)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Top 10 States by Orders")
plt.xticks(rotation=30)
plt.show()

# Top 10 states by Amount Spent
sales_state_amount = df.groupby("State", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10)
plt.figure(figsize=(15, 6))
ax = sns.barplot(x="State", y="Amount", data=sales_state_amount)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Top 10 States by Amount Spent")
plt.xticks(rotation=30)
plt.show()
## Uttar Pradesh, Maharashtra, and Karnataka lead in terms of orders and spending.

# Step 5: Marital Status Analysis
# Count plot for Marital Status
ax = sns.countplot(x="Marital_Status", data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Marital Status Distribution")
plt.show()

# Bar plot for amount spent by Marital Status and Gender
sales_marital_gender = df.groupby(["Marital_Status", "Gender"], as_index=False)["Amount"].sum()
plt.figure(figsize=(15, 6))
sns.barplot(x="Marital_Status", y="Amount", hue="Gender", data=sales_marital_gender)
plt.title("Amount Spent by Marital Status and Gender")
plt.show()
## Married women are the most significant contributors to sales.

# Step 6: Occupation Analysis
# Count plot for Occupation
ax = sns.countplot(x="Occupation", data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Occupation Distribution of Buyers")
plt.xticks(rotation=45)
plt.show()

# Bar plot for amount spent by Occupation
sales_occupation = df.groupby("Occupation", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10)
plt.figure(figsize=(15, 6))
sns.barplot(x="Occupation", y="Amount", data=sales_occupation)
plt.title("Amount Spent by Occupation")
plt.xticks(rotation=45)
plt.show()
## IT, Healthcare, and Aviation professionals are the top buyers.

# Step 7: Product Category Analysis
# Count plot for Product Categories
plt.figure(figsize=(20, 8))
ax = sns.countplot(x="Product_Category", data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Distribution of Product Categories")
plt.xticks(rotation=90)
plt.show()

# Bar plot for top Product Categories by Amount Spent
sales_product_category = df.groupby("Product_Category", as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10)
plt.figure(figsize=(15, 6))
sns.barplot(x="Product_Category", y="Amount", data=sales_product_category)
plt.title("Top Product Categories by Amount Spent")
plt.xticks(rotation=45)
plt.show()
## Food, Clothing & Apparel, and Electronics & Gadgets are the most popular.