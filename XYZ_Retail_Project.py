#!/usr/bin/env python
# coding: utf-8

# In[35]:


#Task 1: Sales Data Summary

#Assigning units sold to categories
Category_A=780
Category_B=550

#Total units sold
Total_units_sold=Category_A+Category_B

#Difference between category
Difference= Category_A-Category_B

#Ratio of units sold
Ratio=Category_A/Category_B

#Print the results
print("Sales Data Summary:")
print(f"The total units sold in two categories are {Total_units_sold}")
print(f"The difference between the categories are {Difference}")
print(f"The ratio between two categories are {Ratio:.2f}")


# In[37]:


#Task 2: Customer Age Data

#Store customer data
customer_age= 30
customer_name = "John Doe"

#Convert age to string and create a personalized message
personalized_marketing_message= f"Dear {customer_name}, at {customer_age}, you’re eligible for our premium loyalty program"

#Pront the personalized message for email campaigns
print(personalized_marketing_message)


# In[3]:


#Task 3: Product List Management

#Product prices list
product_prices_list= [23.50,25.50,60.00,45.00,50.00]

#Highest and Lowest price
min_price=min(product_prices_list)
max_price=max(product_prices_list)

#mid-range products
mid_range_products = []
for prices in product_prices_list:
    if min_price < prices < max_price:
        mid_range_products.append(prices)

#New premium product price
new_product_price_list= 189.00
#New Product price list
product_prices_list.append(new_product_price_list)

#Print the final results
print(f"Product Prices : {product_prices_list} ")
print(f"The lowest price is {min_price}")
print(f"The highest price is {max_price}")
print("Mid-Range Products:", mid_range_products)
print(f"The updated price is {new_product_price_list}")
print(f"The updated price list: {product_prices_list}")



# In[39]:


#Task 4: Inventory Lookup

#Product information dictionary
product_details= [
    {
        "product_name": "Samsung M51",
        "SKU" : "SKU5678",
        "price": 29.99,
        "category": "Electronics"
    },
    { "product_name": "Apple Iphone",
        "SKU" : "SKU6789",
        "price": 150.99,
        "category": "Electronics"
    },
     { "product_name": "Google Pixel",
        "SKU" : "SKU2546",
        "price": 100.78,
        "category": "Electronics"
     }
]

# Step 2: Print product names and SKUs
for product in product_details:
    print(f'Product Name: {product["product_name"]}, SKU: {product["SKU"]}')


# In[40]:


#Task 5: Stock Level Alert System

#Defining stock threshold
stock_threshold=200

#Input box to enter the level of stock
current_stock_level=int(input("Please enter the current stock level: "))

#To check whether stock level is below the threshold
if(current_stock_level<stock_threshold):
    print("Reorder now")
else:
    print("Stock is sufficient")


# In[41]:


#Task 6: Sales Report Formatting

#List of products sold
product_list= ["samsung M51","apple Iphone","google Pixel"]

#For loop in uppercase
print("Sales report(for loop)")
for product in product_list:
    print(product.upper())
    
#while loop in uppercase
print("Sales report(while loop)")
i=0
while i <len(product_list):
    print(product_list[i].upper())
    i += 1


# In[43]:


#Task 7: Area Calculation for Store Layout

#Function to calculate area of the section
def calculate_area(length,width):
    return length*width

#store sections with dimensions
store_sections = [
    # Section name, length, width
    ("Appliances", 30, 10),  
    ("Kitchen needs", 60, 60),
    ("Groceries", 80, 70),
    ("Home decor", 45, 55)
]

#Tp print the area of different store sections
for store in store_sections:
    area = calculate_area(store[1], store[2])
    print(f"The area of the {store[0]} section is: {area} square units")


# In[44]:


#Task 8: Customer Feedback Analysis

#To count the number of vowels in a customer feedback message.
customer_feedback=input("Enter customer feedback message: ")

#Initialising variables
vowels="aeiouAEIOU"
vowel_count=0

#Looping through the feedback
for i in customer_feedback:
    if i in vowels:
        vowel_count=vowel_count+1

#Print the number of vowels
print(f"Number of vowels: {vowel_count}")

#To reverse the the feedback message 
reverse_feedback= customer_feedback[::-1]
print(f"The reversed feedback message is : {reverse_feedback}")


# In[45]:


#Task 9: Price Filtering Tool

# List of products with their prices
products = [
    {"product_name": "Samsung M51", "price": 100},
    {"product_name": "Apple Iphone", "price": 850},
    {"product_name": "Google Pixel", "price": 170},
    {"product_name": "Motorola Edge", "price": 89},
    {"product_name": "OnePlus Nord", "price": 650},
]

# Define the price threshold
price_threshold = 150

# Use list comprehension to filter products priced above the threshold
eligible_products = [i for i in products if i["price"] >= price_threshold]

# Print the list of eligible products for the discount campaign
print("Eligible products for discount campaign:")

for i in eligible_products:
    print(f"{i['product_name']} - ${i['price']}")



    


# In[47]:


#Task 10: Sales Log File Management

#To store daily sales summaries in a text file.
with open("sales_log.txt","w") as file:
    
#summarizing the daily sales performance in a file.
    file.write("Daily sales revenue: $5000\n")
    file.write("Average sales unit sold:100\n")

#Read and print the content of the file
with open("sales_log.txt","r") as file:
    content=file.read()
    print(content)


# In[48]:


#Task 11: Daily Sales Average

#Declaring list of sales for the last 7 days and calculating total sales and average sales.

sales_figure=[3000,7890,2345,6784,6501,3478,5109]
total_sales=sum(sales_figure)
average_sales= total_sales/len(sales_figure)

#Print the average sales.
print(f"The average sales for the past week is ${average_sales:.2f}")


# In[5]:


#Task 12: Customer Segmentation

#list of customer spending amounts.
customer_spending_amt=[400,500,157,908,450]

#For loop to categorize customers based on their spending amount.
for customer in customer_spending_amt:
    if customer < 400:
        category="low"
    elif customer >= 400 and customer < 599:
        category="medium"
    else:
        category="high"
        
     #Print the categorized results
    print(f"Spending amount :{customer}, Category: {category}")


# In[6]:


#Task 13: Discount Calculation

#List of products with orginal price,discount_percent,discount_amt and final_price
orginal_price= 560
discount_percent=10
discount_amount=orginal_price * (discount_percent/100)
final_price=orginal_price-discount_amount
print(f"The orginal price is ${orginal_price}")
print(f"The discounted price is ${discount_amount}")
print(f"The final price is ${final_price}")
      
#list of products with different discounts 
products = [
    {'product_name': 'Samsung M51', 'price': 350, 'discount': 25},
    {'product_name': 'Apple Iphone', 'price': 950, 'discount': 10},
    {'product_name': 'Motorola Edge', 'price': 550, 'discount': 45},
    {'product_name': 'OnePlus Nord', 'price': 450, 'discount': 20}
]

#Iterating through the product dictionary to print the final price
for product in products:
    discount_amount = product['price'] * (product['discount'] / 100)
    print(f"The orginal price for {product['product_name']} - ${product['price']} ")
    print(f"The discounted price for {product['product_name']} - ${discount_amount}")
    final_price = product['price'] - discount_amount
    print(f"The final price for {product['product_name']} is ${final_price}")



# In[7]:


#Task 14: Customer Feedback Sentiment Analysis

#Positive and negative words list
positive_feedback = ["good", "happy", "satisfied", "fine", "amazing"]
negative_feedback = ["bad", "unhappy", "disappointed", "worst", "hopeless"]

#Text input to enter the feedback
customer_feedback = input("Enter the feedback for the product: ")

# Default sentiment
sentiment = "Neutral"  

#iterate through list to check if it's positive and negative
for word in customer_feedback.split():
    if word.lower() in positive_feedback:
        sentiment = "Positive"
        break
    elif word.lower() in negative_feedback:
        sentiment = "Negative"
        break

print(sentiment)


# In[8]:


#Task 15: Employee Salary Increment Calculator

#dictionary with employee details
employee_details=[
    {'employee_name':'Ivaan', 'Rating': 'Excellent', 'Base Salary': 5000},
    {'employee_name':'Zayne', 'Rating': 'Good', 'Base Salary': 10000},
    {'employee_name':'Ananya', 'Rating': 'Average', 'Base Salary': 4000},
    {'employee_name':'Beatrice', 'Rating': 'Poor', 'Base Salary': 6000}
        ]
#Loop through dictionary items to find increment percentage based on the rating.
for employee in employee_details:
    if employee['Rating']=="Excellent":
        increment= 0.15 #(15%)
    elif employee['Rating']=="Good":
        increment=0.10 #(10%)
    elif employee['Rating']=="Average":
        increment=0.05 #(5%)
    else:
        increment=0.0

    new_salary= employee['Base Salary'] + (employee['Base Salary'] * increment)
        
        #Print the updated salary for each employee.
    print(f"{employee['employee_name']}'s updated salary: {new_salary}")


# In[ ]:


#Task 16: Monthly Sales Report Generator

#list of daily sales figures
daily_sales=[4500, 8900,2345,7812,9076,56789]

#total and average sales for the month.
total_sales=sum(daily_sales)
average_sales=total_sales/ len(daily_sales)

#summary of statistics to a text file
with open ("monthly_report.txt", "w") as file:
    file.write("Monthly Sales Report\n")
    file.write("--------------------\n")
    file.write(f"Daily Sales: {daily_sales}\n")
    file.write(f"Total Sales: {total_sales}\n")
    file.write(f"Average Sales: {average_sales:.2f}\n")

#Print in console 
print("Report generated successfully!")


# In[10]:


#Task 17: Stock Replenishment Planning

#list of products with names and their current stock levels
product_details = [
    {'product_name': 'Samsung M51', 'stock_level': 50},
    {'product_name': 'Apple Iphone', 'stock_level': 95},
    {'product_name': 'Motorola Edge', 'stock_level': 115},
    {'product_name': 'OnePlus Nord', 'stock_level': 150},
]

#default threshold level
threshold=100

#print which needs replenishment
for product in product_details:
    if product['stock_level'] < threshold:
        print(f"Product {product['product_name']} needs replenishment.")
        


# In[11]:


#Task 18: Data Cleaning Utility

#list of customer names with inconsistency
names=["meriam Alex ","  Aparna murali   ", "  ZAYNE thomas"]

#trimming spaces and standardizing the capitalization & Printing the edited names.
for name in names:
    edited_names=name.strip().title()
    print(edited_names)


# In[12]:


#Task 19: Simple Sales 

#import statistics module
import statistics

#monthly avy sales.
monthly_average_sales=[1500,1450,8064]

#future sales
future_sales=statistics.mean(monthly_average_sales)


#forecasted sales figures for budget planning.
print(f"The forecasted sale for next month is {future_sales:.2f}")


# In[23]:


#Task 20: Customer Loyalty Points Calculator

#details of the customers with their names and total purchase amount.
customers=[
    {'customer_name':'Varkey George', 'total_spent':4500},
    {'customer_name':'Thomas Punnen', 'total_spent':6500.90},
    {'customer_name':'Luke Alex', 'total_spent':1500.85}
]

#tiered system where different spending levels earn different point multipliers.
for customer in customers:
    if customer['total_spent']<= 2000:
        loyalty_points=customer['total_spent']  * 0.01
    elif customer['total_spent'] > 2000 and customer['total_spent'] <= 5000:
        loyalty_points= customer['total_spent'] * 0.02
    else:
        loyalty_points=customer['total_spent'] * 0.03
#Print the loyalty points for a list of customers.   
    print(f"{customer['customer_name']} earned ${loyalty_points:.2f} points" )


# In[ ]:




