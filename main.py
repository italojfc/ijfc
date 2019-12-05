import matplotlib.pyplot as plt
from   random     import  randint
from   population import  Population 
from   selection  import  Select

family                  = [[],[],[],[],[],[]]
bestsIndividuos         = [[],[]]
bestsIndividuosCrossing = [[],[]]
individuoMutation       = [[],[]]
fits                    = []
fit1                    = []
fit2                    = []
porcent                 = 3
meta                    = 28
quantGenes              = 36
quantIndividuos         = 100
geracao                 = 300
contGeracao             = 0   
melhorFit1              = 0           
melhorFit2              = 0
individuo               = Population()
selecao                 = Select()



def convert_bin(listaBits):
        
        copylistaBits = listaBits.copy()
        copylistaBits.reverse()
        new_list = []
        count    = 0
        decimal  = 0
        newlist  = []
        base     = 0
        for bit in copylistaBits:
                base = bit * 2
                if base != 0 :
                        decimal  = decimal + base ** count
                count+= 1
                if count >= 4:
                        new_list.append(decimal)
                        decimal  = 0
                        count    = 0
        newlist = new_list.copy()
        newlist.reverse()
        return newlist
    
def size_population(sizePopulation):
    population = []
    i          = 0
    while i < sizePopulation:
        population.insert(i,[])
        i = i + 1
    return population

def gera_population(family,quantIndividuos):
     
     populacao         = size_population(quantIndividuos)
     cont              = 0
     while cont < quantIndividuos:
           populacao[cont] = individuo.criar_individuo(quantGenes)
           fit             = individuo.fitness(populacao[cont])
           fits.append(fit) 
           cont = cont + 1
     if   contGeracao != 0:
          i = 0
          quantIndividuos = quantIndividuos - 7 
         
          while i < 6:
                 ind = randint(0,quantIndividuos)
                 populacao[ind+i] = family[i]
                 fits[ind+i]      = individuo.fitness(family[i])
                 i = i + 1                                 
     return populacao

#________________________________________________________________________________________________________________________________
while contGeracao < geracao: 
    
    print("*GERACÃO ",contGeracao)

    pop = gera_population(family,quantIndividuos)
 
    bestsIndividuos  = selecao.select_bests(fits,pop,quantIndividuos)
    
    family[0]        = bestsIndividuos[0].copy()
    family[1]        = bestsIndividuos[1].copy()
    
    print("MELHOR IND 1:  ",convert_bin(bestsIndividuos[0]))
    print("MELHOR IND 2:  ",convert_bin(bestsIndividuos[1]))

    bestsIndividuosCrossing = selecao.crossing(bestsIndividuos[0],bestsIndividuos[1])
    
    family[2]               = bestsIndividuosCrossing[0].copy()
    family[3]               = bestsIndividuosCrossing[1].copy()
   
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("IND 1 CRUZADO: ",convert_bin(bestsIndividuosCrossing[0]))
    print("IND 2 CRUZADO: ",convert_bin(bestsIndividuosCrossing[1]))
    
    individuoMutation  = selecao.mutation(bestsIndividuosCrossing[0],bestsIndividuosCrossing[1],quantGenes,porcent)
       
    family[4]          = individuoMutation[0].copy()
    family[5]          = individuoMutation[1].copy()
    
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("IND 1 MUTADO:  ",convert_bin(individuoMutation[0]))
    print("IND 2 MUTADO:  ",convert_bin(individuoMutation[1]))
    
    melhorFit1 = individuo.fitness(individuoMutation[0])
    melhorFit2 = individuo.fitness(individuoMutation[1])
    
    fit1.append(melhorFit1)
    fit2.append(melhorFit2)
    
    print("*MELHORES FITNESS: ",melhorFit1,",",melhorFit2)
    print("========================================================================================================================================")
     
    fits.clear()
    pop.clear()                       
    bestsIndividuos.clear()
    individuoMutation.clear()
    bestsIndividuosCrossing.clear()
    contGeracao = contGeracao + 1

plt.xlabel("GERAÇÕES")
plt.ylabel("FITNESS")
plt.grid(True)
plt.plot(fit1)
#plt.plot(fit2)
plt.show()

