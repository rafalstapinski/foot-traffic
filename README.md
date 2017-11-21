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

The unweighted rate is given by a regression of the increase in check-ins across every venue per chain.
The weighted rate is given by a regression of the increase in check-ins across every venue per chain when adjusted for the amount of checkins relative to other venues in the chain.
The change-only weighted rate is given by a regression of the increase in weighted check-ins only for the venues that showed an increase in traffic over the course of the quarter.

Chain | Unweighted Rate | Weighted Rate | Weighted Rate CO |  Revenue
--- | --- | --- | ---
Starbucks | 3648.683 | 2.7434 | 3.5254 | $5.7B
Bojangles | 105.1 | 0.6914 | 1.0010 | $133.43M
Dennys | 243.883 | 0.5360 | 0.8746 | $132.38M
Panera | 840.13 | 2.2404 | 2.3800 |
Chipotle | 663.63 | 1.7888 | 1.9180 | $1.13B
Wendys | 595.63 | 0.5780 | 0.7577 |
Flanigans | 1.73 | 0.2476 | 0.5778 |
Jamba | 95.916 | 0.7211 | 0.9896 |
Sonic | 407.016 | 0.5493 | 0.9857 | $123.57M
