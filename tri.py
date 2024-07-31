from django.shortcuts import render, get_object_or_404
import sqlite3, random, os,django
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trial.settings')
django.setup()
from exam.models import phy_easy
i=1
j=1
row_count = phy_easy.objects.count()
c=[]
while j<=row_count:
    c.append(j)
    j=j+1
print(f'Total nu{c}mber of rows: {row_count}')
array = []
questno=random.choice(c)
questno=str(questno)
# Iterate through the dictionary and add each item to the array
row = phy_easy.objects.filter(pk=1)
print(row, questno)
for item in row:
    array.append((item))

print(array)    
while i<3:
    questno=random.choice(c)
    print(questno)

    #row = get_object_or_404(phy_easy, pk=questno)
    print("not equal")
    print(row.question)
    x=[]
    x.append(row.question)
    x.append(row.option1)
    x.append(row.option2)
    x.append(row.option3)
    x.append(row.option4)
    x.append(row.answer)
    i=i+1    
print(x)
x=str(x)
x=x.replace("['", "")
x=x.replace("']", "")
print(x)
