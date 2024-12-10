#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Task 1: Sales Data Summary

#Assigning variables to units
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


# In[12]:


#Task 2: Customer Age Data

#Store customer data
customer_age= 30
customer_name = "John Doe"

#Convert age to string and create a personalized message
personalized_marketing_message= f"Dear {customer_name}, at {customer_age}, you’re eligible for our premium loyalty program"

#Pront the personalized message for email campaigns
print(personalized_marketing_message)


# In[22]:


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



# In[12]:


#Task 4: Inventory Lookup
product_details= []
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


# In[18]:


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


# In[24]:


#Task 6: Sales Report Formatting

#List of products sold
product_list= ["samsung M51","apple Iphone","google Pixel"]

#For loop
print("Sales report(for loop)")
for product in product_list:
    print(product.upper())
    
#while loop
print("Sales report(while loop)")
i=0
while i <len(product_list):
    print(product_list[i].upper())
    i += 1


# In[35]:


#Task 7: Area Calculation for Store Layout

#Area of the section
def calculate_area(length,width):
    return length*width

#store sections with dimensions
store_sections = [
    ("Appliances", 30, 10),  # Section name, length, width
    ("Kitchen needs", 60, 60),
    ("Groceries", 80, 70),
    ("Home decor", 45, 55)
]

#Function to calculate the area of different store sections
for i in store_sections:
    area = calculate_area(i[1], i[2])
    print(f"The area of the {i[0]} section is: {area} square units")


# In[39]:


#Task 8: Customer Feedback Analysis

#To count the number of vowels in a customer feedback message.
customer_feedback=input("Enter customer feedback message: ")


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


# In[48]:


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



    


# In[49]:


#Task 10: Sales Log File Management

#To store daily sales summaries in a text file.
with open("sales_log.txt","w") as file:
    
#summarizing the daily sales performance.
    file.write("Daily sales revenue: $5000\n")
    file.write("Average sales unit sold: 100\n")

#Read and print the content of the file
with open("sales_log.txt","r") as file:
    content=file.read()
    print(content)


# In[54]:


#Task 11: Daily Sales Average

#Given a list of sales figures for the last 7 days, calculate the average sales.

sales_figure=[3000,7890,2345,6784,6501,3478,5109]
total_sales=sum(sales_figure)
average_sales= total_sales/len(sales_figure)

#Print the average sales to help the finance team understand the weekly performance.
print(f"The average sales for the past week is ${average_sales:.2f}")


# In[9]:


#Task 12: Customer Segmentation

#list of customer spending amounts.
customer_spending_amt=[400,500,157,908,450]

#loop to categorize customers based on their spending amount.
for customer in customer_spending_amt:
    if customer < 400:
        category="low"
    elif customer >= 400 and customer < 599:
        category="medium"
    else:
        category="high"
#Print the categorized results to assist in targeted marketing.
print(f"Spending amount :{customer}, Category: {category}")


# In[38]:


#Task 13: Discount Calculation

#Write a code that calculates the final price after applying a discount percentage to a product’s original price.
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

for product in products:
    discount_amount = product['price'] * (product['discount'] / 100)
    print(f"The orginal price for {product['product_name']} - ${product['price']} ")
    print(f"The discounted price for {product['product_name']} - ${discount_amount}")
    final_price = product['price'] - discount_amount
    print(f"The final price for {product['product_name']} is ${final_price}")

#print the final prices.


# In[65]:


#Positive and negative words list
positive_feedback = ["good", "happy", "satisfied", "fine", "amazing"]
negative_feedback = ["bad", "unhappy", "disappointed", "worst", "hopeless"]

#Text input to enter the feedback
customer_feedback = input("Enter the feedback for the product: ")

# Default sentiment
sentiment = "Neutral"  

for word in customer_feedback.split():
    if word.lower() in positive_feedback:
        sentiment = "Positive"
        break
    elif word.lower() in negative_feedback:
        sentiment = "Negative"
        break

print(sentiment)


# In[ ]:





# In[ ]:




