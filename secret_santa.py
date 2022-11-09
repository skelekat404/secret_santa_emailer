from random import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import numpy as np
import pandas as pd

#IMPORTANT SETUP TO FOLLOW:
# you must turn on "Allow less secure apps" to "ON" at:  https://myaccount.google.com/lesssecureapps 
# from the email you are sending from
#number of participants must be an EVEN number
#must: pip install numpy 
#must: pip install pandas

#email that it will be sent from
myEmail = 'YOUR EMAIL HERE'
#password of your email
myPassword = 'YOUR EMAIL PASSWORD HERE'

#Dictionary of participants - MODIFY AND ADD PEOPLE AS NEEDED, MUST BE EVEN
participantDictionary = {
'Participant1' : 'Participant1@gmail.com',
'Participant2' : 'Participant2@gmail.com',
'Participant3' : 'Participant3@gmail.com',
'Participant4' : 'Participant4@gmail.com',
}
#minimum amount for gift
minBudget = '25'
#maximum amount for gift
maxBudget = '30'

#subject of the email
emailSubject = 'Your Secret Santa Assignment'

#algorithm for secret santa assignments
pairing = list(np.random.choice(list(participantDictionary.keys()), len(list(participantDictionary.keys())), replace = False))
receiver = []
for i in range(-1, len(pairing)-1):
	receiver.append(pairing[i]) 

#connection to Google's SMTP email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, myPassword)

#sending out an email to each person
for i in range(len(participantDictionary)):
    msg = MIMEMultipart()
    msg['From'] = myEmail
    msg['Subject'] = emailSubject
    #this line is extremely long in order to print a python at the end of the email, because why not
    message = 'Happy Secret Santa ' + str(pairing[i]) + '! \n\nYou\'re the secret santa of: ' + str(receiver[i]).upper() + '\n\nYou should spend between $' + minBudget + '-' + maxBudget + ' buying them a gift(s). \n\nMAKE SURE TO KEEP YOUR ASSIGNMENT A SECRET! \n\nWith Cheers,\nThe Python Script >:)\n\n       ---_ ......._-_--.\n      (|\ /      / /| \  \\\n      /  /     .\'  -=-\'   `.\n     /  /    .\'             )\n   _/  /   .\'        _.)   /\n  / o   o        _.-\' /  .\'\n  \          _.-\'    / .\'*|\n   \______.-\'//    .\'.\' \*|\n    \|  \ | //   .\'.\' _ |*|\n     `   \|//  .\'.\'_ _ _|*|\n      .  .// .\'.\' | _ _ \*|\n      \`-|\_/ /    \ _ _ \*\\\n       `/\'\__/      \ _ _ \*\\\n      /^|            \ _ _ \*\n     \'  `             \ _ _ \\\n                       \_'
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server.sendmail(myEmail, participantDictionary[pairing[i]],
	text)

#end the connection
server.quit()

# csv storage for testing or record keeping
santadf = pd.DataFrame({'pairing':pairing, ' receiver':receiver})
santadf.to_csv('SecretSantaList' + '.csv')