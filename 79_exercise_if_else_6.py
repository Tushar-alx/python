#write a program to find out which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india. 
 
 
US_SALES_TAX = 8.5            # average US sales tax (%)
EXCHANGE_RATE = 82.0          # 1 USD = 82 INR
INDIA_GST = 18.0              # India GST on phones (%)
INDIA_ALLOWANCE = 50000       # duty free INR allowance
INDIA_CUSTOMS_DUTY = 35.0     # customs duty (%) on value above allowance

# Inputs
price_usd = float(input("Enter iPhone 17 Pro Max price in USA (USD): "))
price_india = float(input("Enter iPhone 17 Pro Max price in India (INR): "))

# Calculate USA total
sales_tax_amount = price_usd * (US_SALES_TAX / 100)
total_usd = price_usd + sales_tax_amount
total_inr_before_customs = total_usd * EXCHANGE_RATE

# Customs calculation
if total_inr_before_customs > INDIA_ALLOWANCE:
    taxable_value = total_inr_before_customs - INDIA_ALLOWANCE
    customs_duty = taxable_value * (INDIA_CUSTOMS_DUTY / 100)
else:
    customs_duty = 0

total_us_inr = total_inr_before_customs + customs_duty

# Calculate India total
gst_amount = price_india * (INDIA_GST / 100)
total_india_inr = price_india + gst_amount

# Output
print("\n--- COST COMPARISON ---")
print(f"Cost if bought in USA and brought to India (INR): {round(total_us_inr, 2)}")
print(f"Cost if bought in India (INR): {round(total_india_inr, 2)}")

# Decision
if total_us_inr < total_india_inr:
    print("\n>> Buying in USA is CHEAPER!")
elif total_india_inr < total_us_inr:
    print("\n>> Buying in India is CHEAPER!")
else:
    print("\n>> Both options cost the same!")
