import pandas as pd
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
#print(df)
#print(df.describe())   #What do the numbers look like? stats
#print(df.head(5))      #What kind of data am I working with? print the first 5 rows
#print(df.tail(5))      #print the last 5 rows
#print(df.info())       #Are there missing values? Data types correct?
#print(df.columns.tolist())   #What are the column names? List of columns
#print(df.Country) #get the country column
#print(df.Country.value_counts())   #How many unique values are in the country column? How many times does each value appear?
#---------------------------------------------
#rows,colummns = (df.shape)         #How big is the dataset? rows x col
#print(rows, colummns)
#print(df.columns.tolist())
#---------------------------------------------
#print(df["Category"].value_counts())   #How many unique values are in the category column? How many times does each value appear?
#total_category = df["Category"].value_counts()
#print(total_category)

#---------------------------------------------
#print(df["Category"]) #Select columns
#print(df[['Customer ID', 'Customer Name']]) #Select multiple columns

#---------------------------------------------
#Filter rows
# 1. Orders with high sales
high_sales_orders = df[df.Sales > 5000] #Select rows where sales is greater than 5000
# 2. Orders from the United States  
technology_orders = df[df.Category == "Technology"] #Select rows where category is Technology
# 3. Orders from the United States with high sales
technology_high_sales_orders = df[(df.Category == "Technology") & (df.Sales > 5000)] #Select rows where category is Technology and sales is greater than 5000
#print(technology_high_sales_orders)
#print(technology_orders)
#print(high_sales_orders)    

#print(df[df.Profit>200])

#---------------------------------------------
# GROUP BY

cat_type = df.groupby('Category')
'''
print("categories are:", cat_type)
for category, group in cat_type:
    print("Category name:", category)
    print(group.head(2))  # Print the first 2 rows of each category group

print(cat_type.get_group("Furniture")) #Get the group of rows where category is Furniture
print(cat_type.max()) #Get the maximum value for each column in each category group
'''  
#Group by category and calculate total sales for each category  
category_sales = df.groupby("Category")["Sales"].sum()
#print(category_sales)


#Group by category and calculate total profit for each category
profit_by_category = df.groupby("Category")["Profit"].sum()
#print(profit_by_category)


#Group by category and calculate total sales and profit for each category
sales_n_profit = df.groupby("Category")[["Sales","Profit"]].sum() #Group by category and calculate total sales and profit for each category
#print(sales_n_profit)

#Group by region and calculate total sales for each region
sales_by_region = df.groupby("Region")[["Sales","Profit"]].sum()
#print(sales_by_region)


#---------------------------------------------
'''
print(df.groupby("Category")["Discount"].mean(),'\n')
print(df[["Sales","Profit","Discount"]].corr()) #Calculate the correlation between sales, profit, and discount
print(df[df["Discount"]>0.5])
'''
#---------------------------------------------

#DATA CLEANING
#Check for missing values
'''
print("Missing values: ",df.isnull().sum()) #Check for missing values in each column

print("Duplicate values: ",df.duplicated().sum()) #Check for duplicate rows
#df=df.drop_duplicates() #Remove duplicate rows

print(df.dtypes) #Check data types of each column
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")#Convert order date column to datetime format
print(df.dtypes) #Check data types again to confirm the change

print("Earliest order date: ",df["Order Date"].min(), "Latest order date: ", df["Order Date"].max()) #Find the earliest and latest order date in the dataset
'''

#replace function
import numpy as np
#just an example of how to replace values
'''
new_df = df.replace(-999, np.nan) #Replace all instances of -999 with NaN
new_df = df.replace([-999, -888], np.nan) #Replace all instances of -999 and -888 with NaN
print(new_df)
'''
'''
new_df = df.replace({
    -999: np.nan,
    'no event': 'sunny day'
})
print(new_df)
'''

#---------------------------------------------

#print(df.head(5))
#s = df.groupby("State")
'''
for State, state_df in s:
    print("State name:", State)
    print(state_df)
'''
#print(s.get_group("California")) #Get the group of rows where state is California

#SPLIT-APPLY-COMBINE
#print(s.max()) #Get the maximum value for each column in each state group
#print(s.describe()) #Get the descriptive statistics for each column in each state group
#------------------------------------------------

#SORTING
'''
df_sort = df.sort_values(by = "Quantity", ascending = False) #Sort the dataframe by quantity in descending order
print(df_sort.head(10)) #Print the first 10 rows of the sorted dataframe

df_sort1 = df.sort_values(by = ["Category", "Sales"], ascending = [True, False]) #Sort the dataframe by category in ascending order and then by sales in descending order
print(df_sort1.head(10)) #Print the first 10 rows of the sorted dataframe
'''
#------------------------------------------------
#FILTERING
# 1. Orders with high sales
'''
high_sales_orders = df[df.Sales > 5000] #Select rows where sales is greater than 5000
print(high_sales_orders)
'''
# 2. multiple conditions
'''
technology_orders = df[df.Category == "Technology"] #Select rows where category is Technology
technology_high_sales_orders = df[(df.Category == "Technology") & (df.Sales > 5000)] #Select rows where category is Technology and sales is greater than 5000
print(technology_high_sales_orders)
'''
'''
customers_with_high_orders_profit = df[(df.Quantity>10) & (df.Profit > 3000)] #Select rows where profit is greater than 3000
print(customers_with_high_orders_profit)
'''
#------------------------------------------------
#AGGREGATION
#------------------------------------------------
#Group by category and region and calculate total sales and profitfor each category and region
category_sales = df.groupby(["Category", "Region"])[["Sales", "Profit"]].sum()
#print(category_sales)

region_summary = df.groupby("Region").agg({
    "Sales": ["sum", "mean", "max"],
    "Profit": ["sum", "mean", "max"]
})
#print(region_summary)

#print(df.columns.tolist())

customer_summary = df.groupby("Customer Name").agg({
    "Sales": ["sum", "mean", "max"],
    "Profit": ["sum", "mean", "max"]
})
#print(customer_summary)

segment_summary = df.groupby(["Segment", "Region","Customer Name"])["Sales"].agg(["sum","mean","count"])
#print(segment_summary)

#----------------------------------------------
#TIME SERIES ANALYSIS
#----------------------------------------------
#Convert order date column to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed")
#Group by order date and calculate total sales for each date
daily_sales = df.groupby("Order Date").agg({
    "Sales": ["sum", "mean", "max"],
    "Profit": ["sum", "mean", "max"]
})
#print(daily_sales)

#Group by month and calculate total sales for each month

df["Month"] = df["Order Date"].dt.month_name() #Extract month from order date
#print(df.Month)
monthly_sales_profit = df.groupby("Month")[["Sales","Profit"]].sum() #Group by month and calculate total sales for each month
#print(monthly_sales_profit)
monthly_sales_profit = df.groupby("Month")[["Sales","Profit"]].sum().sort_values('Sales', ascending=False)
#print(monthly_sales_profit)

#Group by year and calculate total sales for each year

df["Year"] = df["Order Date"].dt.year #Extract year from order date
#print(df.Year)
yearly_sales_profit = df.groupby("Year")[["Sales","Profit"]].sum() #Group by year and calculate total sales for each year
#print(yearly_sales_profit)

# TIME TAKEN TO DELIVER
df["Delivery_time"] = (df["Ship Date"]-df["Order Date"]).dt.days #Calculate delivery time in days
#print(df[["Order Date", "Ship Date", "Delivery_time","Category"]].head(10)) #Print the first 10 rows of order date, ship date, and delivery time

#PLOTTING TIME SERIES
import matplotlib.pyplot as plt

#monthly sales and profit plot
'''
plt.bar(monthly_sales_profit.index, monthly_sales_profit["Sales"], color="blue", alpha=0.5) #Plot total sales by month
plt.bar(monthly_sales_profit.index, monthly_sales_profit["Profit"], color="orange", alpha=0.5) #Plot total profit by month
plt.title("Monthly Sales and Profit")
plt.xlabel("Month")
plt.ylabel("Total Sales and Profit")
plt.xticks(rotation=45)
plt.legend(["Sales", "Profit"])
plt.show()
'''
#----------------------------------------------
#ADVANCE FILTERING + DEEP DIVE
#---------------------------------------------
#Orders with high sales and profit
high_sales_profit_orders = df[(df["Sales"] > 5000) & (df["Profit"] > 3000)] #Select rows where sales is greater than 5000 and profit is greater than 3000
#print(high_sales_profit_orders[["Customer Name", "Category", "Sales", "Profit"]]) #Print customer name, category, sales, and profit for orders with high sales and profit
#print(df[["Customer Name", "Category", "Sales", "Profit"]]) #Print customer name, category, sales, and profit for orders with high sales and profit


#orders from office supplies category with high sales
office_high_sales = df[(df["Category"] == "Office Supplies") & (df["Sales"]>5000)]
#print(office_high_sales[["Customer Name", "Category", "Sales", "Profit"]]) #Print customer name, category, sales, and profit for orders from office supplies category with high sales

#----------------------------------------------
# isin function
# orders from California, Texas, and New York
states_of_interest = ["California","Texas", "New York"]
state_orders = df[df["State"].isin(states_of_interest)] #Select rows where state is in the list of states of interest
#print(state_orders.groupby("State")[["Sales","Profit"]].sum())


#most orders from which category
most_popular_category = df["Category"].value_counts().idxmax() #Find the most popular category by finding the index of the maximum value in the category value counts
#print("Most popular category:", most_popular_category)
'''
plt.bar(df["Category"].value_counts().index, df["Category"].value_counts().values) #Plot the count of each category
plt.title("Count of Each Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
'''

#which segmett buys the most
segment_buying_most = df.groupby("Segment")["Sales"].sum().idxmax() #Find the segment that buys the most by finding the index of the maximum value in the segment sales sum
#print("Segment buying the most:", segment_buying_most)     

#---------------------------------------------------------
#CORELATION
#---------------------------------------------------------
correlation = df[["Sales", "Profit", "Discount"]].corr() #Calculate the correlation between sales, profit, and discount
#print(correlation)

#Does discount affect profit?
discount_profit_correlation = df[["Discount", "Profit"]].corr() #Calculate the correlation between discount and profit
#print(discount_profit_correlation)

#value counts and unique values
df["Category"].value_counts()
df["Region"].value_counts()
df["Segment"].value_counts()

df["Category"].unique()
#print(df["Region"].unique())

#-----------------------------------------------------------------
#difference between pivot table and cross tab
#Pivot table allows for multiple aggregation functions and can handle missing values with fill_value, 
# while cross tab is limited to a single aggregation function and does not handle missing values. 
# Pivot table also allows for multi-level indexing, while cross tab does not.
#-----------------------------------------------------------------

# PIVOT TABLE
#-----------------------------------------------------------------
pivot_table_region = df.pivot_table(index = "Category", columns = "Region", values = "Sales", aggfunc = "sum", margins = True, margins_name = "Total") #Create a pivot table with category as index, region as columns, and sum of sales as values
#print(pivot_table_region)

pivot_table_segment = df.pivot_table(index = "Category", columns = "Segment", values = "Sales", aggfunc = "sum") #Create a pivot table with category as index, segment as columns, and sum of sales as values
#print(pivot_table_segment)

pivot_table_year = df.pivot_table(index = "Category", columns = "Year", values = "Sales", aggfunc = ['sum','max','min']) #Create a pivot table with category as index, year as columns, and sum of sales as values
#print(pivot_table_year)

pivot_table_year_region = df.pivot_table(
    index = ['Year', 'Region'], 
    columns = "Segment", 
    values = "Sales", 
    aggfunc = "sum",
    #fill_value = 0, #Fill missing values with 0
    margins = True, #Add a total column and row
    margins_name = "Total" #Name of the total column and row
)
#print(pivot_table_year_region)

pivot_table_region_profit = df.pivot_table(
                            index = "Region", 
                            columns = "Category", 
                            values = "Profit", 
                            aggfunc = "sum"
)
#print(pivot_table_region_profit)








#---------------------------------------------------------
#CROSS TAB
#-----------------------------------------------------------------
cross_tab = pd.crosstab(df["Category"], df["Region"], values=df["Sales"], aggfunc="sum", margins=True, margins_name="Total") #Create a cross tab with category as rows, region as columns, and sum of sales as values
#print(cross_tab)   


