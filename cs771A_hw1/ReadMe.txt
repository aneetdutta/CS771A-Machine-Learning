Method1:  convex.py
1) Mean of each seen classes is computed.  (40,4096) matrix is returned.
2)  Similarity  matrix  is  computed  using  the  seen  class  attribute  matrix(ak)  and  unseen  class attribute matrix(ac).
similaritymatrix[i,j] =ac[i].T∗ak[j].  
3) Similarity matrix is normalized such that sum of each row of similarity matrix equals 1.
4) Mean of unseen classes are computed.
meanunseen[j] =meanunseen[j] + (similaritymatrix[j][i]∗meanseen[i] where i ranges from 1 to 40.  
5) Euclidean Distance of each test data point is calculated from the mean of unseen classes and the class closest to the test data point is predicted to be the class label of test data
point.
6)Accuracy is calculated by number of correctly classified points/total number of points.

The accuracy achieved is 46.89 percent.

Method2:  regerssion.py
1) Mean of each seen classes is computed.  (40,4096) matrix is returned.
2) W is calculated by performing matrix multiplications.
3) mean of unseen classes is computed using Wac where ac is unseen class attribute matrix.
4) Euclidean Distance of each test data point is calculated from the mean of unseen classes and the class closest to the test data point is predicted to be the class label of test data point.
5)Accuracy is calculated by number of correctly classified points/total number of points.
The accuracy achieved for different values of λ are:

Value of λ Accuracy(%)
0.01        58.09
0.1         59.54
1.0         67.39
10.0        73.28
20.0        71.68
50.0        65.08
100.0       56.47
