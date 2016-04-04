Project 5: Application of Machine Learning Algorithms
===============================================
The mouse style research investigates mouse behaviors of different genes. The researchers hope to gain insight to human behaviors using mouse data, since experimenting directly on human is difficult. One question of interest is on whether genetic affects psychological disorders such as depression, or overeating. 

The researchers design the experiment as follow: they have 16 different strains of mice, and each strain has 12 almost identical mice in term of genetic. If we observe that each mouse behaves very similarly to its twins, but differently from other strains of mice, we can conclude that genetic affect mouse behaviors. The researchers record the daily activities of each mouse, for example the time it spends eating, drinking, sleeping, and wondering around its habitat. 

One way to detect this relationship between genes and behaviors is to use supervised machine learning models, and see whether we can use mouse daily habit to predict its gene. If we can get high accuracy, we can conclude that there is an association between the gens and behaviors, or nature trumps nurture. In addition, if we can use unsupervised machine learning models to cluster the daily mouse activities into clusters that corresponds to the genes, that can be an even stronger proof to the close relationship between genes and mouse behaviors. 

From our limited understanding, the result of this research might have meaningful implication on the way we treat psychological disorders. If it turns out that nature does influence these disorders, we can probably conclude that psychological disorders is not that much different from physical disabilities. Otherwise, if it turns out that nature has little influences over these disorders, we can try to find way to prevent these disorders from happening. 

Some initial tasks to be done: 

1. Clean up the existing strain_classification.py: create functions and objects.
2. Adding new models: knn, random forests, neural networks.
3. Doing unsupervised learning: k-means.
4. Compute confidence interval for the accuracy of each model.
5. Give insights about how mice behavior is related to their genetic heritage.
