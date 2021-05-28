S=[[0,0,1,1,1,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,1],[0,1,1,0,1,1,0,1,1,1],
   [0,1,0,1,1,1,0,0,1,1],[0,0,1,0,1,1,1,1,1,1],[0,0,1,0,1,1,0,1,1,1]]
print("S=",S)
def calfitness(S):
  fit=[]
  total=0
  print("Fitness")
  for i in S:
    fit.append(i.count(1))
    total+=i.count(1)
    print(fit)
    print(total)
    return fit;
fit=calfitness(S)
print("Arranging in Descending order")
desc=S
for i in range(len(desc)):
  j=i + 1
  for j in range(len(desc)):
    if desc[i].count(1)>desc[j].count(1):
       desc[j],desc[i]=desc[i],desc[j]

print("s =" , desc)
print("Cross over after 4 points")
desc[1],desc[2]=desc[2],desc[1]

for i in range(5):
  desc[1][i],desc[2][i]=desc[2][i],desc[1][i]

print("S2 and S3")
print("S2=", desc[1], "S3=", desc[2])

print("S=", desc)
print("Mutation")
for i in range(6):
   
   //wants change in this code
  for j in range(2):
    if(desc[i][j]==0):
       desc[i][j]=1
    else:
       desc[i][j]=0

print("s=",desc)
fit2=calfitness(desc)
if fit<fit2:
  print("Fitness is greater after applying Genetic Algorithm")
else:
  print("Fitness is greater before applying Genetic Algorithm")

//Edit to this file
