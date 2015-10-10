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

treat = ["chemo","drugA","drugB","drugC","drugD","drugE",]
eth = ["white","black","hispanic","asian"]
side = ["Pain","Vomiting","Fatigue","Anemia","Lymphedema"]
can = ["Breast","Lung"]

# for n in patients:
#     u = User(name=n.replace('\xc2\xa0',''), email='dummy@dummy' + str(randint(0,2353453)) + '.com', is_patient=1,\
#              type_cancer=random.choice(can),is_male=0,age=randint(40,65),\
#               treatment=random.choice(treat),ethnicity=random.choice(eth),\
#               side_effects=random.choice(side),expectancy=randint(0,10))
#     u.save()

users = [u for u in User.objects.all()]

# class Genetic_info(models.Model):
#     chr        = models.IntegerField()
#     pos        = models.IntegerField()
#     users      = models.ManyToManyField(User)
#     gene       = models.CharField(max_length=200)

for n in random.sample(users,10):
    print n

for k in g.keys():
    for case in g[k]: 
        gg = Genetic_info(chr=case[0], pos=case[1],gene=k)
        print gg
        gg.save()
        for n in random.sample(users,10):
            n.genetic_info_set.add(gg)
            n.save()
