# Gas Trading

## Data:
- Monthly natural gas prices. Each data point is:
    + the market purchase price of natural gas.
    + for delivery at the end of that month.
    + from 31/10/2020 to 30/09/2024

## Analyze Price Data
### Idea:
- Simple Linear Regression for annual cyclicality using months
- Bilinear Regression for cyclicality by combining a trigonometric and linear model.


### Steps:
 1. Estmiate the purchase price for any data in the past (Interpolate).
 2. Extrapolate prices for one more year beyong the last available month-end point
 3. Provide a function to input a date => output an estimated price
    
### Output:
<img width="392" height="278" alt="image" src="https://github.com/user-attachments/assets/ae59a239-492b-4e97-a17a-7cfad08cf5bc" />
<img width="382" height="278" alt="image" src="https://github.com/user-attachments/assets/6d4e6ccd-2fd7-4b50-b859-87decaaf3311" />
<img width="615" height="333" alt="image" src="https://github.com/user-attachments/assets/86ceeebd-7302-4d25-a12e-2a5d4020e633" />
<img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/8f41a141-936a-4b0c-91a3-f6c722b0cd17" />

## Contract Valuation:
### Context: 
- Any trade agreement is as valuable as:
    The price we can sell - The price we are able to buy - cost
- Profit <= Sell > Price + Cost
- Example: Purchase in summer at MMBtu $2/MMBtu and store for 4 months, and ensure to sell at $3/MMBtu, with $0.1 Storage cost per month, $0.01 injection/withdrawal cost per 1MMBtu and $0.05 transportation cost to and from facility =>
    Value of contract = (3-2) - 0.1*4 - 0.01 - 0.05*2 = 0.490 ($)
- Storage Trade Process:
    + Buy (Injection Date) => Outflow = Injected * Buy Price
    + Store.
    + Sell (Withdrawal Date) => Inflow = Withdraw * Sell Price    
  
### Needed Inputs:
- Injection Date.
- Withdrawal Date.
- Prices on those dates
- Injection/withdrawl rate.
- Storage Capacity.
- Cost.

### Steps:


### Output (Example):
<img width="551" height="269" alt="image" src="https://github.com/user-attachments/assets/04fda629-9a1c-43ac-b3f1-3ca544b2d9e1" />
<img width="1016" height="144" alt="image" src="https://github.com/user-attachments/assets/27d0f3e5-79c9-43f3-b7ff-fa83821ffc28" />

