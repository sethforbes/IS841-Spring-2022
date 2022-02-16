# Learning Goals

- Kaggle-like Competition - More Practice with Supervised ML
- Unsupervised ML Part 1 - Clustering

Slides:  https://docs.google.com/presentation/d/1W6WbFw4gh6QFjJ7LPx32AgOvTgXyS2S79HCBpmE2Mvg/edit?usp=sharing

## Warmup Supervised Data Challenge

> The datasets are in the `/challenges/` folder.

1.  Fit a supervised model with the dataset `train` and apply it to the test set.  
2.  The `test` set does not have the known value.  The leaderboard will compare the known value to your prediction and score your entire submission for accuracy.
3.  The `sample-submission` file highlights what your dataset should look like before you submit to the leaderboard.
4.  Write your submission file as a `csv` file.  NOTE:  Be careful, you need to change the seperator.  The leaderboard might get angry if the file is not submitted in the expected format.

> Start small and iterate.  I recommmend getting a small analytical pipeline together so that you can iterate.  Have fun!

- Server address:  http://34.150.129.108:8501/
- Keep only the id and prediction column.  There is a sample file for you to review.


## Unsupervised ML - Clustering

> NOTE:  Please install the Operator Toolbox Extension if you haven't already for the caching operator.

- [Notebook to demonstrate distances](https://docs.google.com/spreadsheets/d/1h0XTvPbGlmYkKuEdFvX0AD96Yv8So4elnBRY4pCepwc/edit?usp=sharing)
- KMeans - We define the clusters based on K.  This will introduce our ability to interate 
- Hierarchical Clulstering (Agglomerative) - Bottom-up approach, clusters all records and we determine what is the correct number of clusters for our problem
- DBSCAN - Can determine outliers but requires my tuning (not as clear cut as Kmeans and HClust)


