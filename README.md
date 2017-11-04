# Foot Traffic Research

The aim of this project is to predict revenues for publicly traded food chains using foot traffic as a proxy metric.

Foot traffic data was collected daily throughout Q3 and Q4 using the Foursquare API. It will be used with Q3 earnings reports to predict the earnings for Q4.

### The nine chains are:
- Starbucks
- Bojangles
- Dennys
- Panera
- Chipotle
- Wendys
- Flanigans
- Jamba
- Sonic


### Analysis:

I am taking 9 week samples from the third quarter across these chains. I aggregated the data, and found the rate of increase and the weighted rate of increase (based on total location foot traffic) for each chain assuming a linear regression.

### Q3 Summary:

Empty revenues reflect unreleased earnings. 

Chain | Unweighted Rate | Weighted Rate | Revenue
--- | --- | --- | ---
Starbucks | 3648.683 | 2.7434 | $5.7B
Bojangles | 105.1 | 0.6914 | $133.43M
Dennys | 243.883 | 0.5360 | $132.38M
Panera | 840.13 | 2.2404 |
Chipotle | 663.63 | 1.7888 | $1.13B
Wendys | 595.63 | 0.5780 |
Flanigans | 1.73 | 0.2476 |
Jamba | 95.916 | 0.7211 |
Sonic | 407.016 | 0.5493 | $123.57M
