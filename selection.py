from random import  randint

class Select:
      
       
      def select_bests(self,fits,individuos,quanIndividuoas):
          self.quanIndividuoas = quanIndividuoas
          self.individuos = individuos
          self.fits       = fits
          i               = 0
          goodFitOne      = 0
          goodFitTwo      = 0
          count           = 0
          auxFits1        = []
          f               = []
          fitsAndIndex   = []
          melhoresIndividuos    = [[],[]]
          indexMelhor1          = -1
          indexMelhor2          = 0
          #flag1                  = 0
          #fitMelhor               = []
          while count <  self.quanIndividuoas:
                 f.append(fits[count])
                 f.append(count)
                 fitsAndIndex.append(f) 
                 #print("teste:",fitsAandIndex)
                 f = []
                 count = count + 1
          fitOrdenadosfilter    =  sorted(self.fits)
          
          goodFitOne            =  fitOrdenadosfilter[len(fitOrdenadosfilter)-1] 
          goodFitTwo            =  fitOrdenadosfilter[len(fitOrdenadosfilter)-2]
          x = 1
          if goodFitTwo == goodFitOne:
             while goodFitTwo == goodFitOne:
                   goodFitTwo  =  fitOrdenadosfilter[len(fitOrdenadosfilter)-x]   
                   x = x + 1
          while i < self.quanIndividuoas:
                  auxFits1 = fitsAndIndex[i].copy()
                  
                  if auxFits1[0] == goodFitOne  :
                       indexMelhor1 = auxFits1[1]
                       #print("MEL-1:",auxFits1)
                  if auxFits1[0] == goodFitTwo :
                       indexMelhor2 = auxFits1[1]
                       #print("MEL-2:",auxFits1)
                       
                           
                  i = i + 1
          print("ind melhor 1:",indexMelhor1)
          print("ind melhor 2:",indexMelhor2)
          melhoresIndividuos[0] =  self.individuos[indexMelhor1]
          melhoresIndividuos[1] =  self.individuos[indexMelhor2]
          return melhoresIndividuos
       
      def crossing(self,gene1,gene2): 
           self.gene1 = gene1
           self.gene2 = gene2
           
           paiDeTodos    = [[],[]]
           point         = randint(0,35)
           paiDeTodos[0] = self.gene1[:point] + self.gene2[point:]
           paiDeTodos[1] = self.gene2[:point] + self.gene1[point:]
       
           return paiDeTodos
       
      def mutation(self,paisGeracao1,paisGeracao2,quantGenes,porcentMutation):
            self.paisGeracao1    = paisGeracao1 
            self.paisGeracao2    = paisGeracao2
            self.quantGenes      = quantGenes
            self.porcentMutation = porcentMutation
            porcentagem = self.quantGenes * (self.porcentMutation/100)
            index1 = 0
            index2 = 0
            i = 0
            mutados = [[],[]]
            while  i < int(porcentagem):
                  index1 = randint(0,35)
                  if self.paisGeracao1[index1] == 0:
                     self.paisGeracao1[index1] =  1
                  else:
                     self.paisGeracao1[index1] =  0
              
                  index2 = randint(0,35)
                  if self.paisGeracao2[index2] == 0:
                     self.paisGeracao2[index2] =  1
                  else:
                     self.paisGeracao2[index2] =  0
            
                  i = i + 1
            mutados[0] = self.paisGeracao1
            mutados[1] = self.paisGeracao2
            return mutados
     
      
            
            
            
            