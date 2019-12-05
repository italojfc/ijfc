from random import  randint
import numpy  as np
class Population:
 
  def fitness(self,bits):
       self.bits = bits
       saida = 0
       saida = 9
       saida += (self.bits[1]*self.bits[4])
       saida -= (self.bits[22]*self.bits[13])
       saida += (self.bits[23] * self.bits[3])
       saida -= (self.bits[20] * self.bits[9])
       saida += (self.bits[35] * self.bits[14])
       saida -= (self.bits[10] * self.bits[25])
       saida += (self.bits[15] * self.bits[16])
       saida += (self.bits[2]  * self.bits[32])
       saida += (self.bits[27] * self.bits[18])
       saida += (self.bits[11] * self.bits[33])
       saida -= (self.bits[30] * self.bits[31])
       saida -= (self.bits[21] * self.bits[24])
       saida += (self.bits[34] * self.bits[26])
       saida -= (self.bits[28] * self.bits[6])
       saida += (self.bits[7]  * self.bits[12])
       saida -= (self.bits[5]  * self.bits[7])
       saida += (self.bits[17] * self.bits[19])
       saida -= (self.bits[0]  * self.bits[29])
       saida += (self.bits[22] * self.bits[3])
       saida += (self.bits[20] * self.bits[14])
       saida += (self.bits[25] * self.bits[15])
       saida += (self.bits[30] * self.bits[11])
       saida += (self.bits[24] * self.bits[18])
       saida += (self.bits[6]  * self.bits[7])
       saida += (self.bits[8]  * self.bits[17])
       saida += (self.bits[0]  * self.bits[32])
       return saida
      
  def criar_individuo(self,quantGenes):
         self.quantGenes = quantGenes
         cromos = []
         while len(cromos) != self.quantGenes:
                valorRandomico = randint(0, 1)
                cromos.append(valorRandomico)
         return cromos 
      
 
