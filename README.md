# Gas Trading

## Guide to run file:
    Data => Interpolation => Extralopation

## Data:
- Monthly natural gas prices. Each data point is:
    + the market purchase price of natural gas.
    + for delivery at the end of that month.
    + from 31/10/2020 to 30/09/2024

## Idea:
- Simple Linear Regression for annual cyclicality using months
- Bilinear Regression for cyclicality by combining a trigonometric and linear model


## Steps:
 1. Estmiate the purchase price for any data in the past => Interpolate.
 2. Extrapolate prices for one more year beyong the last available month-end point
 3. Provide a function: input a date => output an estimated price
 4. Visualise patterns and comment

## Improvement ideas:
- Fit a seasonal ARIMA (SAMIRA) model.
- Hol-Winters expoential smoothing
- External Regressors



