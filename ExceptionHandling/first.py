prices=[559,789,"N/A",349]
print(prices)

for price in prices:
    print("Vertical List ")
    print(price)
        
try:
    print(sum(prices))
    
except TypeError:
    print("Check the prices")
finally: 
    print("Need help? Contact us ")       

 