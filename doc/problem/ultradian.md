Project 4: Ultradian Analyses
=============================
## Description

Ultradian rhythm is widely observed in mammalian behavioural patterns. Ultradian analysis aims to find the time-specific patterns in behavioral records, without specifying the length of cycle in advance (but need to be within 1 hour to 1 day). Typical ultradian period for rats includes 4, 12 and 24 hours. For example, we expect rats to be inactive in the nighttime. Ingestions and movements mostly happened in the daytime. It would informative to study the ultradian cycle of the behaviour of mouse.

## Data
- Input:  records for each strains (total of  16), each feature of interest (food, water, distance, active_state probability ...), in a duration of 12 days (excluding 4 acclimation days) . 
- Processed: using one-minute time bins of movement records to binary score the activity into 0 (IS: inactive state) and 1 (AS: active state); using thirty-minute bins of food records to calculate the amount of chows consumed by mice; using LS periodogram technique to select the appropriate time bins for above.
- Output: different patterned visualization for each feature, with the appropriate time bins that presents the most significant ultradian pattern.

## Key questions and potential solutions
- What is the variable of interest for the periodic patterns ?
    - Summary of activity: Food and water ingestion, distance traveled , movement intensity, AS probability.
    - Spatial variable: Spatially discrete the data to cells each with its primary functions such as food cell, water cell, etc.  Examine ultradian cycle of  the spatial probability densities of the occupancy time in each cells. 
- How to subset the data?
    - Basic subset: 16 strains.
    - Strains may not be the primary influence for the variation of ultradian rhythms. We may look into the cycle for each mouse and detect the most important factors influencing the  ultradian rhythms. 
- How to choose the frequency or period ?
    - The Lomb-Scargle (LS) periodogram spectral analysis technique, a widely used tool in period detection and frequency analysis.
- How to determine the optimal bin intervals for constructing the time series?
    - The bin interval may vary according to the frequency. Bin interval examples: 5 min, 30 min, 1 hour etc. Need to look into the data. 
- What is the connection with other subprojects?
    - Ultradian rhythms could be treated as one feature for clustering the 16 strains. We may also subset the data using the results of the cluster and analysis the rhythm similarities and differences across clusters. 

## Method and models
- Seasonal decomposition.
- Longitudinal data analysis.
- autocorrelation anslysis.

## Reference
- Lloyd, David, and Ernest L. Rossi, eds. Ultradian rhythms in life processes: An inquiry into fundamental principles of chronobiology and psychobiology. Springer Science & Business Media, 2012.
- Stephenson, Richard, et al. "Sleep-Wake Behavior in the Rat Ultradian Rhythms in a Light-Dark Cycle and Continuous Bright Light." Journal of biological rhythms 27.6 (2012): 490-501.
