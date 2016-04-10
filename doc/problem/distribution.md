Project 6: Power Laws & Universality
=======================================

## Background Knowledge
- In statistics, a power law, also known as a scaling law, is a functional relationship between two quantities, where a relative change in one quantity results in a proportional relative change in the other quantity, independent of the initial size of those quantities: one quantity varies as a power of another. $$Y=kx^a$$.
- Universality: The equivalence of power laws with a particular scaling exponent can have a deeper origin in the dynamical processes that generate the power-law relation.

## Purpose
- Find out the distribution of inter-event distance for home base mice and non home base mice.
- How could power law apply to other variables and features in mouse behaviour?

## Key Questions
- How to define inter-event distance for each mouse.
	- We should read through the paper to find out the definition of “inter-event distance”.
- What is the meaning of home based/non home based.
	- "Home base": a favored location at which long periods of inactivity (ISs) occur.
- How to choose the interval of distance to make the histogram plot.
	- To make the histogram look better, we can try different interval of distance.
- What is the expectation of the distribution of the distance.
	- Based the habit of mice, we would expect mice would have more short distance movements rather than more long distance movement.
- What is the expectation of the relation between home-based and non-home-based distance.
	- We would expect positive or negative relationship between home and non-home distance of movement patterns.

## Exploratory Questions
-  What does power law suggest in those graphs?
-  What are the internal connections between those behaviors?
-  Is it possible to ap any models to discover power law connection in data?

## Data:
- Our primary data source will be mouse behavioral data from Tecott Lab. Each record contains the position of each mouse and the time stamp. 
- We want to use the data to establish the Home base location. The HCM cages were spatially discretized into a 2*4 array of cells, and occupancy times of each MD were calculated in each cell. Usually the cell containing the niche area displays largest occupancy times, which was considered to be Home base location. For MDs in which largest occupancy times occurred outside the niche, the cell with occupancy greater than half the total time was considered to be Home base.

## Reference reading:
- https://en.wikipedia.org/wiki/Power_law
