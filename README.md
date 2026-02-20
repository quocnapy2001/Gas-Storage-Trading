# Gas Trading

## Data:
- Monthly natural gas prices. Each data point is:
    + the market purchase price of natural gas.
    + for delivery at the end of that month.
    + from 31/10/2020 to 30/09/2024

## Price Modelling
### Idea:
- Simple Linear Regression for annual cyclicality using months
- Bilinear Regression for cyclicality by combining a trigonometric and linear model


### Steps:
 1. Estmiate the purchase price for any data in the past => Interpolate.
 2. Extrapolate prices for one more year beyong the last available month-end point
 3. Provide a function: input a date => output an estimated price
 4. Visualise patterns and comment

### Improvement ideas:
- Fit a seasonal ARIMA (SAMIRA) model.
- Hol-Winters expoential smoothing
- External Regressors

## Contract Valuation:
### Context: 
- Any trade agreement is as valuable as:
        The price we can sell - The price we are able to buy - cost
- Example: Purchase in summer at MMBtu $2/MMBtu and store for 4 months, and ensure to sell at $3/MMBtu, with $0.1 Storage cost per month, $0.01 injection/withdrawal cost per 1MMBtu and $0.05 transportation cost to and from facility =>
        Value of contract = (3-2) - 0.1*4 - 0.01 - 0.05*2 = 0.490 ($)
- 
  
### Idea:
- 

### Steps:
1. 

