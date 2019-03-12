import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1

class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):
        

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        
        return self.maxBirthProb

    def getClearProb(self):
       
        return self.clearProb

    def doesClear(self):
       
        clr_prob= random.random()
        if self.clearProb == 1.0:
            return True
        if clr_prob <= self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        
        to_reproduce_prob = random.random()
        if to_reproduce_prob <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else:
            raise NoChildException()
            
            



class Patient(object):
   
    def __init__(self, viruses, maxPop):
       
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
       
        return self.viruses


    def getMaxPop(self):
        
        return self.maxPop


    def getTotalPop(self):
         
        return len(self.viruses)


    def update(self):
        
        curr_virus_list=self.viruses.copy()
        for index in range(len(self.viruses)):
            #to_clear= random.random()
            if self.viruses[index].doesClear() ==  True:
                #print('this virus will be removed')
                curr_virus_list.remove(self.viruses[index])
            
            else:
                curr_pop_density= float(len(curr_virus_list)/self.getMaxPop())
                try:
                   curr_virus_list.append(self.viruses[index].reproduce(curr_pop_density))
                except NoChildException :
                   continue
        self.viruses =  curr_virus_list
        return len(self.viruses)
    
    
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):

    # TODO
    
    
    # summation of all viruses in a time step//no division here
    avg_virus_pop = 300*[0]
    for trials in range(numTrials):
        viruses=[]
        for i in range(numViruses):
          viruses.append(SimpleVirus(maxBirthProb, clearProb))
        patient = Patient(viruses,maxPop)
        virus_growth_list = []
        for timesteps in range(300):
            virus_growth_list.append(patient.update())
        
        #virus_growth_list = np.array(virus_growth_list)
        avg_virus_pop = [avg_virus_pop[i] + virus_growth_list[i] for i in range(len(virus_growth_list))]    
    y_axis = [x/numTrials for x in avg_virus_pop]
    #x_axis = list(range(300))
    pylab.plot(y_axis, label = "Simple Virus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

#simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
    
    

#v1 = SimpleVirus(1.0, 0.25)
#v2 = SimpleVirus(1.0, 0.38)
#v3 = SimpleVirus(1.0, 0.45)
#patient = Patient([v1,v2,v3],100)
#for trials in range(100):
#    patient.update()
#    #print(patient.viruses)
#
#print(patient.getTotalPop())

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        
        #intializing attributes from parent(super) class
        super().__init__(maxBirthProb,clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        
        return self.resistances

    def getMutProb(self):
       
        return self.mutProb

    def isResistantTo(self, drug):
 
        if drug in self.resistances:
            return self.resistances[drug]==True
        else:
            return False
    
    def isSuperBug(self,drugs):
        
        resistanceBool = []
        for drug in drugs:
            if drug in self.resistances:
                resistanceBool.append(self.resistances[drug])
            else:
                resistanceBool.append(False)
                
        if resistanceBool.count(False)==0:
            return True
        else:
            return False
        
    def getOffspringResistance(self,mutProb):
        
        drug_resistances=self.resistances.copy()
        
        for drug in drug_resistances:
            mut_chance = random.random()
            if mut_chance <= mutProb:
                drug_resistances[drug] = not(drug_resistances[drug])
        
        return drug_resistances
            
            
    def reproduce(self, popDensity, activeDrugs):
        
        if self.isSuperBug(activeDrugs) == True:
            to_reproduce_prob = random.random()
            if to_reproduce_prob <= self.maxBirthProb * (1 - popDensity):
                return ResistantVirus(self.maxBirthProb,self.clearProb,\
                                      self.getOffspringResistance(self.mutProb),self.mutProb)
            else:
                raise NoChildException()
                
        else:
            raise NoChildException()
            
        
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        
        # TODO
        #self.viruses = viruses
        #self.maxPop = maxPop
        super().__init__(viruses,maxPop)
        self.druglist=[]


    def addPrescription(self, newDrug):
      
        # TODO
        if newDrug not in self.druglist:
            self.druglist.append(newDrug)


    def getPrescriptions(self):  

        # TODO
        return self.druglist


    def getResistPop(self, drugResist):
      
        # TODO
        resist_virus_pop=0
        for virus in self.viruses:
            if virus.isSuperBug(drugResist) == True:
                resist_virus_pop += 1
        return resist_virus_pop
                


    def update(self):
     
        # TODO
        curr_virus_list=self.viruses.copy()
        for index in range(len(self.viruses)):
            
            if self.viruses[index].doesClear() == True:
                #print('this virus will be removed',self.viruses[index])
                curr_virus_list.remove(self.viruses[index])
            
            else:
                curr_pop_density= float(len(curr_virus_list)/self.getMaxPop())
                try:
                   curr_virus_list.append(self.viruses[index].reproduce(curr_pop_density,\
                                          self.druglist))
                except NoChildException :
                   continue
        self.viruses =  curr_virus_list
        return len(self.viruses)
        
        
#virus = ResistantVirus(1.0, 0.0, {}, 0.0)
#patient = TreatedPatient([virus], 100)
#
#for steps in range(45):
#  viruses = patient.update()
#  if steps==44:
#      print(viruses)
        
 # test cases for Resistant Virus and patient class   
#virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
#virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
#patient = TreatedPatient([virus1, virus2, virus3], 100)
#patient.getResistPop(['drug1'])
#patient.getResistPop(['drug2'])
#patient.getResistPop(['drug1','drug2'])

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):

    # TODO

    avg_virus_pop = 300*[0]
    resist_virus_pop = 300*[0]
    
    for trials in range(numTrials):
        viruses=[]
        for i in range(numViruses):
          viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        treated_patient = TreatedPatient(viruses,maxPop)
        total_virus_growth_list = []
        resist_virus_growth_list = []
        
        for timesteps in range(300):
            if timesteps ==150:
                treated_patient.addPrescription('guttagonol')
            total_virus_growth_list.append(treated_patient.update())
            resist_virus_growth_list.append(treated_patient.getResistPop(['guttagonol']))
        
        #virus_growth_list = np.array(virus_growth_list)
        avg_virus_pop = [avg_virus_pop[i] + total_virus_growth_list[i] for \
                         i in range(len(total_virus_growth_list))]
        
        resist_virus_pop = [resist_virus_pop[i] + resist_virus_growth_list[i] for\
                            i in range(len(resist_virus_growth_list))]
        
    y_axis_total = [x/numTrials for x in avg_virus_pop]
    y_axis_resist = [x/numTrials for x in resist_virus_pop]
    

    
    
    
    #x_axis = list(range(300))
    pylab.plot(y_axis_total, label = "Simple Virus")
    pylab.plot(y_axis_resist, label = "Resist Virus")
    
    pylab.title("Resistant Virus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
    
random.seed(0)
#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100) 
        
        
        
        
