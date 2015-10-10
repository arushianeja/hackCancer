from random import randint
from patient.models import *

names = open('name_data.txt')
genes = open('list_of_genes.txt')

patients = []
g = {}

for l in names.readlines():
    patients.append(l.strip())
    

for gene in genes.readlines():
    k = gene.strip().replace('\xc2\xa0','')
    g[k] = []
    chr = randint(0,9)
    for i in xrange(0,5):
        pos = randint(0,103453544)
        g[k].append([chr,pos])

    name = models.CharField(max_length=200)
    email       = models.EmailField('email address', unique=True, db_index=True)
    joined      = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    is_patient  = models.BooleanField(default=False) 
    type_cancer = models.CharField(max_length=200)
    expectancy  = models.CharField(max_length=200)
    treatment   = models.CharField(max_length=200)
    side_effects= models.CharField(max_length=200)
    ethnicity   = models.CharField(max_length=200)
    is_male     = models.BooleanField(default=True)
    age   

for n in patients:
    u = User(name=n, email='dummy@dummy.com', is_patient=true,\
             type_cancer="Breast")
    print u
