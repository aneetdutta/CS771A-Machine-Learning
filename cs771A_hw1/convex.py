
# coding: utf-8

# # Method 1: Computing Mean of known and Unknown classes:

# In[266]:


import numpy as np
X_seen=np.load('X_seen.npy')
mean_seen=np.zeros((40,4096),dtype='float')
#print(X_seen.shape)
for i in range(0,40):
    #print(i)
    #print(X_seen[i].shape)
    mean_seen[i]=np.mean(X_seen[i],axis=0)
print(mean_seen.shape)
ak=np.load('class_attributes_seen.npy')
#print(ak.shape)
ac=np.load('class_attributes_unseen.npy')
sim=np.concatenate((ak,ac),axis=0)
#print(sim.shape)
#x=np.dot(ac[0].T,ak[0])
#print(x)
sck=np.zeros((10,40),dtype='float')
for i in range(0,10):
    for j in range(0,40):
        sck[i][j]=np.dot(ac[i].T,ak[j])
print(sck.shape)
#print(np.sum(sck[0]))
#print(sck)
sum_l=np.zeros((10,1),dtype='float')
for i in range(0,10):
        sum_l[i]=np.sum(sck[i])
print(sum_l.shape)
for i in range(0,10):
    for j in range(0,40):
        #print(sum_l[i])
        sck[i][j]=sck[i][j]/sum_l[i]

print(sck[1].shape)       
for i in range(0,10):
        sum_l[i]=np.sum(sck[i])
print(sum_l)
mean_unseen=np.zeros((10,4096),dtype='float')
for j in range(0,10):
        for i in range(0,40):
            mean_unseen[j]=mean_unseen[j]+(sck[j][i]*mean_seen[i])
#print(mean_unseen)


# In[226]:





# In[267]:


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
print(p.any()==10)
   # predict[i]=np.argmin(d[j])
#print(predict[55])
ytest=np.load('Ytest.npy')
ytest=ytest.reshape(6180)
#ytest1=np.zeros(6180)
#print(ytest[6179])

    #print(ytest[i])
#print(ytest.any()==[10])
print(ytest.any()==10)
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
        print(p[i])
        print(ytest1[i])
        incorrect=incorrect+1
print(correct)
print(incorrect)
accuracy=float(correct)/float(len(x_test))
print(accuracy)



