
# coding: utf-8

# In[39]:


import numpy as np
X_seen=np.load('X_seen.npy')
mean_seen=np.zeros((40,4096),dtype='float')
for i in range(0,40):
    mean_seen[i]=np.mean(X_seen[i],axis=0)
As=np.load('class_attributes_seen.npy')
print(As.shape)
c1=np.matmul(As.T,As)
print(c1.shape)
I=np.identity(85)
lam=100
I_lam=lam*I
#print(I_lam)
c2=c1+I_lam
inv=np.linalg.inv(c2)
#print(inv)
#print(c2)
c_l=np.matmul(As.T,mean_seen)
#print(c_l.shape)
W=np.matmul(inv,c_l)
#print(W.shape)
ac=np.load('class_attributes_unseen.npy')
mean_unseen=np.matmul(W.T,ac.T)
mean_unseen=mean_unseen.T
print(mean_unseen.shape)


# In[40]:


from scipy.spatial import distance
x_test=np.load('Xtest.npy')
#print(len(x_test))
#predict=np.zeros((len(x_test)),dtype='int')
#d=np.zeros(50,dtype='float')
d=np.zeros((1,10),dtype='float')
p=np.zeros((len(x_test),1),dtype='float')
#print(x_test[0])
#d=distance.euclidean(x_test[0],mean[0])
#print(d)
for i in range(0,len(x_test)):
    for j in range(0,10):
        d1=distance.euclidean(x_test[i],mean_unseen[j])
        d[0][j]=d1
    #print(d[0])
    p[i]=np.argmin(d[0])
    d[0]=0
    #print(d[0])
#dist = distance_matrix(x_test,mean_unseen)
p=p.reshape(6180)
#print(p.any()==10)
   # predict[i]=np.argmin(d[j])
#print(predict[55])
ytest=np.load('Ytest.npy')
ytest=ytest.reshape(6180)
#ytest1=np.zeros(6180)
#print(ytest[6179])

    #print(ytest[i])
#print(ytest.any()==[10])
#print(ytest.any()==10)
#c=predict==ytest
#print(c.shape)
correct=0
incorrect=0
for i in range(0,len(x_test)):
    if(p[i]+1==ytest[i]):
       #print('hi')
       # print(p[i])
       
        correct=correct+1
    else:
       # print(p[i])
        #print(ytest1[i])
        incorrect=incorrect+1
print(correct)
print(incorrect)
accuracy=float(correct)/float(len(x_test))
print(accuracy)

