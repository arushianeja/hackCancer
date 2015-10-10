from random import randint
from patient.models import *
import random

base = "/home/mkallberg/workspace/hackaton/hackCancer/openCancer/patient/"
names = open(base + 'name_data.txt')
genes = open(base + 'list_of_genes.txt')

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

#     name = models.CharField(max_length=200)
#     email       = models.EmailField('email address', unique=True, db_index=True)
#     joined      = models.DateTimeField(auto_now_add=True)
#     is_active   = models.BooleanField(default=True)
#     is_admin    = models.BooleanField(default=False)
#     is_patient  = models.BooleanField(default=False) 
#     type_cancer = models.CharField(max_length=200)
#     expectancy  = models.CharField(max_length=200)
#     treatment   = models.CharField(max_length=200)
#     side_effects= models.CharField(max_length=200)
#     ethnicity   = models.CharField(max_length=200)
#     is_male     = models.BooleanField(default=True)
#     age   

treat = ["chemo","drugA","drugB","drugC","drugD","drugE",]
eth = ["white","black","hispanic","asian"]
side = ["Pain","Vomiting","Fatigue","Anemia","Lymphedema"]
can = ["Breast","Lung"]

for n in patients:
    u = User(name=n.replace('\xc2\xa0',''), email='dummy@dummy' + str(randint(0,2353453)) + '.com', is_patient=1,\
             type_cancer=random.choice(can),is_male=0,age=randint(40,65),\
              treatment=random.choice(treat),ethnicity=random.choice(eth),\
              side_effects=random.choice(side),expectancy=randint(0,10))
    u.save()
