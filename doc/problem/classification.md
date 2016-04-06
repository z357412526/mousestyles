Project 5: Application of Machine Learning Algorithms
===============================================
## Statement of overall problem

The mouse style research investigates mouse behaviors of different genes. The researchers hope to gain insight to human behaviors using mouse data, since experimenting directly on human is difficult. One question of interest is on whether genetic affects psychological disorders such as depression, or overeating. 

## Detailed summary of statistical problem

The researchers design the experiment as follow: they have 16 different strains of mice, and each strain has 12 almost identical mice in term of genetic. If we observe that each mouse behaves very similarly to its twins, but differently from other strains of mice, we can conclude that genetic affect mouse behaviors. The researchers record the daily activities of each mouse, for example the time it spends eating, drinking, sleeping, and wondering around its habitat. 

## Data Description

We dispose of a labeled data set of 16 different strains of mice. Behavioral features are recorded for each mouse and each day. One example can be the time spent eating or drinking.  

## Methodology/ Approach Description

One way to detect this relationship between genes and behaviors is to use supervised machine learning models, and see whether we can use mouse daily habit to predict its gene. If we can get high accuracy, we can conclude that there is an association between the genes and behaviors, or nature trumps nurture. In addition, we can use unsupervised machine learning models to cluster the daily mouse activities into clusters that correspond to the genes. This can highlight an even stronger relationship between genes and mouse behaviors. 

## Testing Framework outline

From our limited understanding, the results of this research might have a meaningful implication on the way we treat psychological disorders. If it turns out that nature does influence these disorders, we can probably conclude that psychological disorders is not much different than physical disabilities. Otherwise, if nature has little influence over these disorders, we can try to find way to prevent these disorders from happening. 

## Initial tasks 

1. Clean up the existing strain_classification.py: create functions and objects.
2. Adding new models: knn, random forests, neural networks.
3. Doing unsupervised learning: k-means.
4. Compute confidence interval for the accuracy of each model.
5. Give insights about how mice behavior is related to their genetic heritage.
