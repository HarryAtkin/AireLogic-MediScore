from enum import Enum
import datetime

#Creates enum for if the patient needs air or oxygen.
class AirOxygenEnum(Enum):
    AIR = 0
    OXYGEN = 2

#Creates enum for if the patient is conscious.
class ConsciousnessEnum(Enum):
    ALERT = 0
    CVPU = 1

#Creates enum for if the patient is fasting or not.
class FastingEnum(Enum):
    FASTING = 0
    NOTFASTING = 1


class PatientDetails:

    #Constructor initialises the attributes
    def __init__(self, patient_id : int, air_oxygen: int, consciousness: int, respiration_rate: int, spo2: int, temperature: float, fasting : int, cbg : float):

        # these attributes types are validated when passed into the function.
        self.PatientId = patient_id
        self.RespirationRate = respiration_rate
        self.SpO2 = spo2
        # Rounds the below to 1 dp.
        self.Temperature = round(temperature, 1)
        self.CBG = round(cbg, 1)

        #Validation
        #Checks that the input is one of the values in the AirOxygenEnum.
        if air_oxygen == AirOxygenEnum.OXYGEN.value or air_oxygen == AirOxygenEnum.AIR.value:
            self.AirOxygen = air_oxygen

        else:
            #Runs until a valid input is entered.
            while air_oxygen != 0 and air_oxygen != 2:
                air_oxygen = int(input(f'Patient {self.PatientId} has Invalid input for Air or Oxygen\n'
                                           f'please enter 0 for Air or 2 for Oxygen\n'))
                self.AirOxygen = air_oxygen


        #Checks if the input is 0 or non-zero.
        if consciousness == 0:
            self.Consciousness = consciousness
        else:
            #Sets their consciousness to the value of CVPU from the ConsciousnessEnum.
            self.Consciousness = ConsciousnessEnum.CVPU.value

        #Checks if the fasting input is valid or not.
        if fasting == FastingEnum.FASTING.value or fasting == FastingEnum.NOTFASTING.value:
            self.Fasting = fasting

        else:
            #Runs until a valid input is entered.
            while fasting != 0 and fasting != 1:
                fasting = int(input(f'Patient {self.PatientId} has Invalid input for if the patient is fasting or not\n'
                                           f'please enter 0 for Fasting or 1 for not Fasting\n'))
                self.Fasting = fasting



        #Sets this variable to none so it can be set later.
        self.MediScore = None
        self.MediScoreList = [[],[]]
        self.MediScoreTime = None

    #This function exists to update the mediscore and check if it has been updated by two or more in the last 24hrs
    def SetMediScore(self, mediscore : int, date : datetime.datetime):

        self.MediScore = mediscore
        self.MediScoreTime = date

        #Deletes any items from the list that are more than 24 hours old.
        if len(self.MediScoreList[0]) == 24:
            del self.MediScoreList[0][0]
            del self.MediScoreList[1][0]

        self.MediScoreList[0].append(self.MediScore)
        self.MediScoreList[1].append(self.MediScoreTime)



        if len(self.MediScoreList[0]) > 1:
            for x in range (len(self.MediScoreList[0])):
                if(self.MediScoreList[0][x] - self.MediScoreList[0][x-1] >= 2) and (self.MediScoreList[1][x] - self.MediScoreList[1][x-1] < datetime.timedelta(days=1)):
                    print(f'Alert Patient {self.PatientId}\'s MediScore has increased by more than 2 in less than 24 hours')
                    break

    #To string method (human-readable class when printed).
    def __str__(self):
        return (f'PatientId: {self.PatientId}\n'
                f'Time tested: {self.MediScoreTime}\n'
                f'Air or Oxygen: {AirOxygenEnum(self.AirOxygen).name}\n'
                f'Consciousness: {ConsciousnessEnum(self.Consciousness).name}\n'
                f'Respiration Rate: {self.RespirationRate} per minute\n'
                f'SpO2: {self.SpO2}%\n'
                f'Temperature: {self.Temperature}°C\n'
                f'CBG: {self.CBG}mmol/L : {FastingEnum(self.Fasting).name}\n'
                f'MediScore: {self.MediScore}\n'
                
                
                f'-------------------------------------------------------')



#Calculates the Mediscore.
def mediscore(patient: PatientDetails):
    FinalScore = 0

    #These two check if the patient is on oxygen and if they are unconscious

    if patient.AirOxygen == AirOxygenEnum.OXYGEN.value:
        FinalScore += 2

    if patient.Consciousness == ConsciousnessEnum.CVPU.value:
        FinalScore += 3

    #This checks for respiration rates and gives a score accordingly
    if patient.RespirationRate < 12:
        if patient.RespirationRate >= 9:
            FinalScore += 1
        else:
            FinalScore += 3

    elif patient.RespirationRate > 20:
        if patient.RespirationRate <= 24:
            FinalScore += 2
        else:
            FinalScore += 3

    # This checks for SpO2 (%) and gives a score accordingly
    if patient.SpO2 < 88:
        if patient.SpO2 >= 86:
            FinalScore += 1
        elif patient.SpO2 >= 84:
            FinalScore += 2
        else:
            FinalScore += 3

    elif patient.SpO2 > 93 and patient.AirOxygen == AirOxygenEnum.OXYGEN.value:
        if patient.SpO2 <= 94:
            FinalScore += 1
        elif patient.SpO2 <= 96:
            FinalScore += 2
        else:
            FinalScore += 3

    # This checks for temperature (°C) and gives a score accordingly
    if patient.Temperature < 36.0:
        if patient.Temperature >= 35.1:
            FinalScore += 1
        else:
            FinalScore += 3

    elif patient.Temperature >= 38:
        if patient.Temperature <= 39:
            FinalScore += 1
        else:
            FinalScore += 2

    #This checks for if the Patient is fasting and calculates their score based on that.
    if patient.Fasting == FastingEnum.FASTING.value:
        if patient.CBG < 4:
            if patient.CBG >= 3.5:
                FinalScore += 2
            else:
                FinalScore += 3

        elif patient.CBG > 5.4:
            if patient.CBG <= 5.9:
                FinalScore += 2
            else:
                FinalScore += 3

    #Runs when the patient is not fasting.
    else:
        if patient.CBG < 5.9:
            if patient.CBG > 4.5:
                FinalScore += 2
            else:
                FinalScore += 3

        elif patient.CBG > 7.8:
            if patient.CBG <= 8.9:
                FinalScore += 2
            else:
                FinalScore += 3

    return FinalScore


print("Test Case 1\n============")
#====================================================================================================================================#
#Creates patient 1, calculates MediScore.
Patient1 = PatientDetails(1,0, 0, 15, 95, 37.19, 1, 5.98)

#This creates 24 tests of patient 1. 1 For each hour of the day to test the alert system for the increase of Mediscore.
#This test will cause the alert to go off.
for x in range (24):
    Patient1.SetMediScore(mediscore(Patient1), datetime.datetime.strptime(f'2025-02-28 00:{x}:10', "%Y-%m-%d %H:%M:%S"))
print(Patient1)

#This increases Patient 1's Mediscore by 3. And will trigger an alert that their score has increased quickly within 24 hours.
Patient1.Consciousness = 1
Patient1.SetMediScore(mediscore(Patient1), datetime.datetime.strptime("2025-03-01 00:01:10", "%Y-%m-%d %H:%M:%S"))
print(Patient1)
#====================================================================================================================================#
print("Test Case 2\n============")
#====================================================================================================================================#
#Creates patient 2, calculates MediScore.
Patient2 = PatientDetails(2, 2, 0, 17, 95, 37.1, 0, 5)

#This creates 12 tests of patient 1. 1 For every other hour of the day to test the alert system for the increase of Mediscore.
#This test will not cause the alert to go off as the MediScore only increased by 1.
for x in range (12):
    Patient2.SetMediScore(mediscore(Patient2), datetime.datetime.strptime(f'2025-02-28 00:{x+1}:10', "%Y-%m-%d %H:%M:%S"))
print(Patient2)

Patient2.RespirationRate = 11
Patient2.SetMediScore(mediscore(Patient2), datetime.datetime.strptime("2025-03-01 00:01:10", "%Y-%m-%d %H:%M:%S"))
print(Patient2)
#====================================================================================================================================#
print("Test Case 3\n============")
#====================================================================================================================================#
#Creates patient 3, calculate MediScore then prints the patient.
#Tests to see if the MediScore is calculated accurately.
#Air or Oxygen = 2 (+2)
#Consiousness = 1 (+3)
#Respiration Rate = 23 (+2)
#SpO2 % = 88 (+0)
#Temperature °C = 38.5 (+1)
#CBG (Fasting) = 5 (+2)
# 2+3+2+1+2 = 10 which == the output.

Patient3 = PatientDetails(3, 2, 1, 23, 88, 38.5, 1, 5)
Patient3.SetMediScore(mediscore(Patient3), datetime.datetime.now())
print(Patient3)
#====================================================================================================================================#
print("Test Case 4\n============")
#====================================================================================================================================#
#Creates patient 4, then prints the patient.
#Patient 4 contains an error to test the validation on the air or oxygen field with an input of 3.
#It also tests that any number that isn't 0 means CVPU
Patient4 = PatientDetails(4, 3, 6, 22, 95, 38.5, 3, 6)
Patient4.SetMediScore(mediscore(Patient4), datetime.datetime.now())
print(Patient4)



