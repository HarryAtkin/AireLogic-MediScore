# AireLogic-MediScore
Breaking down the task:

MediScore ranges from 0 to 14.

Different properties
1. respiration rate
2. oxygen saturation
3. level of consciousness or new confusion (whether the patient is newly confused, disorientated or agitated)
4. temperature
All added together.
Function needs to take in each measures as parameter can take in an object:
- Separate variables easier to read and keep track of.
- List has index's and keeps all the parameters together.
- Class allows for easy storage of all the variables and allows for multiple tests easier (scalability).
The function needs to return an integer.

While calculating the MediScore any of the data that == score 0 can be disregarded as it doesn't effect the final score.
To make the code more efficient for all apart from oxygen and consciousness I could use if statements to determine if the data
is less than or more than the upper bounds of the score 0 values. This stops the code from having to run through large amounts
of if/elif statements.

Bonus tasks:
Use datetime to store each test performed in the last 24 hours and the time. This would allow for me to check for any increase
more than 2 in the MediScore within 24 hours.

## Notes:
- During this I assumed that a MediScore test is performed each hour and have set up the code for the first bonus task to work as such. Which is the reason for me generating 24 different tests for patient 1. The code does work for any test interval as seen by Patient 2 which is performed once every two hours however, the code will still hold 24 lots of MediScore test and their times.
- I used a class to store the data in called patient this allowed me to make my code more concise by not having to repeat sections such as displaying all the patient data, declaring new variables for each test and allows me to change the data about each patient without effecting any of the other patients. It also allows me to easily add some simply validation to the data being inputted to ensure that it is correct.

### The Patient class's constructor takes in 8 parameters
- An Id for the patient: so they can be easily reconginsed (int).
- If the paitent is on air or oxygen: needs to be 0 or 2 as per the requirements. 0 for on Air and 2 for Oxygen (int).
- The patients consciousness: if 0 means the patient is Alert and anything else means they are CVPU.
- The paitents respiration rate per minute (int).
- The paitnets SpO2 % (int).
- The patients temperature: The temperature is rounded to 1 dp (float).
- If the patient is fasting or not: This needs to be 0 if they are fasting and 1 is they'arent.
- The patients CBG level: The CBG level is rounded to 1 dp (float).

### Test cases:

#### Test case 1:
This case performs 24 different MediScore tests each with a time that has been increased by an hour to simulate hourly tests. The purpose of this test is to show what happens if a users MediScore increases by 2 or more points within 24 hours. This is done by changing the patient to being unconscious resulting in their score being increase by 3. This caused a message to be displayed saying "Alert Patient 1's MediScore has increased by more than 2 in less than 24 hours".

#### Test case 2:
This case perfroms 12 different MediScore tests each with a time that has been increased by 2 hours to simulate bi-hourly tests. The purpose of this test was to show that the program works for different test time frames and also shows what happens if the MediScore doesn't increase by 2 or more. The result of this is the correct output of MediScore.

#### Test case 3:
This case is to test that it accurately calculates the MediScore. I passed in the values listed below:
- Air or Oxygen = 2 (+2)
- Consiousness = 1 (+3)
- Respiration Rate = 23 (+2)
- SpO2 % = 88 (+0)
- Temperature °C = 38.5 (+1)
- CBG (Fasting) = 5 (+2)
- 2+3+2+1+2 = 10 which == the output.
The result of this test shows that it is accurately calculating the MediScore based on the given values.

#### Test case 4:
This case tests if the validation for the inputs of air or oxygen, consciousness, and fasting are working. This is done by passing in incorrect values as for air or oxygen I gave it the value 3 (needs to be 0 or 2), consciousness I gave it 6 (more on this later), and fasting I entered 3 (needs to be 0 or 1). For air or oxygen and fasting this resulted in a prompt being displayed telling the user that there is an invalid input for the patient and lists the valid inputs until the user enters a valid input. For consciousness the requirements stats that any non-zero input is CVPU so this resulted in the patient being marked as CVPU indicating that the validation works.
