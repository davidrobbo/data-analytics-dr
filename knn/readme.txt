KNN

Simple, yet powerful method.

Consider a dataset with two labels. We are given a new entry and must classify
into one of the two labels.
All training data is plotted (consider in 2D). The new label is added to the plot.
First, we must calculate the distance between the new entry and all points. Then,
we identify the k nearest neighbours thus giving us our best estimate.

Pros
Easy, quick (requires no training on data), only two parameters (k and distance [euc vs man])
Cons
Doesn't work well with high-dimensionality (complicates distance measure), not great with cat.data

Notes
No ideal value for k - traditionally start with 5 and test/change