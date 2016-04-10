Project 1: Behavioral Model
===========================

## Project Propose:
In order to differentiate mice, we can create behavior profile to describe 
- how they drink, feed or move and 
- how they translate between active state or inactive state. 

![alt tag](http://cenzhuoyao.com/wp-content/uploads/2016/04/project1_behavior_profile.png)

## Background Knowledge:
- Mouses react differently during Active state and Inactive states and all behavioral record should be classified into 2 mutually exclusive categories, Active States (ASs) and Inactive States (ISs). To designate ISs, we examined all time intervals occurring between movement, feeding, and drinking events while the animal was outside the Home base. Those time intervals exceeding an IS Threshold (IST) duration value were classified as ISs; the set of ASs was then defined as the complement of these ISs. Equivalent mathematically, ASs can also be defined as those intervals resulting from connecting gaps between events outside the Home base of length at most IST; ISs are then defined as the complement of these ASs. (*Active State Organization of Spontaneous Behavior Patterns*, C. Hillar et al.)


## Behavioral Profile:

For In/Active State:
- AS Probability: the probability of AS among all time period 
- AS Duration: the length of time of AS
- AS Rate: the reciprocal of average length of time of AS 

Events: Drinking, Feeding and Locomotion
- AS Event Intensity: the average consumption size or distance in one minute of AS
- Event size, Event rate: the number and frequency of events in AS time

Bouts: split all the time duration to several event bout
- Bout size, Bout routine: the number and frequency of bouts in one event
- Bout duration, Bout density: the length of time and frequency of bout 

## Data Collection:
The data we have:
- the observations of location for each mice, (x, y, t) with \Delta t small.
- the aggregated time bined features about each event and its intensity.

The data we need:
- the observation of consumption size and moving distance with each event.

## Algorithms:
To get the profile for each mice aggregated in each 2 hours, here is the algorithm to fill in each features:

For Event
- Event Consumption or Distance: Already in basic time bin features.
- AS Event Intensity: Already in basic time bin features.
- AS Bout Routine: Use txy_coords within each event intervals to generate the path.
- Event Bout Size or Distance: Use observation of consumption size and moving distance data.
- Event Bout Duration: Use event intervals data.
- Event Bout Intensity: Use Event Consumption or Distance over minute of AS time
- Event Size: Use interval to get the number of event happened in bined time
- Event Bout Rate: Use Event Size over AS time.

For In/Active State:
- AS Probability: Already in basic time bin features.
- AS Duration: Already in basic time bin features.
- AS Rate: Use AS Number over AS Duration.
