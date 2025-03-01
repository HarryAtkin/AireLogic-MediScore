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

Note:
During this I assumed that a MediScore test is performed each hour and have set up the code for the first bonus task to work as such.
Which is the reason for me generating 24 different tests for patient 1. The code does work for any test interval as seen by Patient 2
which is performed once every two hours however, the code will still hold 24 lots of MediScore test and their times.
I used a class to store the data in called patient this allowed me to make my code more concise by not having to repeat sections
such as displaying all the patient data, declaring new variables for each test and allows me to change the data about each patient
without effecting any of the other patients. It also allows me to easily add some simply validation to the data being inputted to ensure
that it is correct.

The Patient class's constructor takes in 8 parameters
-An Id for the patient: so they can be easily reconginsed (int).
-If the paitent is on air or oxygen: needs to be 0 or 2 as per the requirements. 0 for on Air and 2 for Oxygen (int).
-The patients consciousness: if 0 means the patient is Alert and anything else means they are CVPU.
-The paitents respiration rate per minute (int).
-The paitnets SpO2 % (int).
-The patients temperature: The temperature is rounded to 1 dp (float).
-If the patient is fasting or not: This needs to be 0 if they are fasting and 1 is they'arent.
-The patients CBG level: The CBG level is rounded to 1 dp (float).
