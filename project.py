import speech_recognition as sr
import speech_recognition as s_r
import spacy
import pyttsx3
import mysql.connector
import smtplib
import re
nlp = spacy.load("en_core_web_sm")
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize
vectorizer = CountVectorizer()
filename = "Voice012.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
doc = nlp(text)
#print(doc.ents)

file_object = open('pro.txt', 'a')
file_object.write(text)

engine = pyttsx3.init()

def Diff1(li1, li2):                  
    return (list(set(li1) - set(li2)))                                       
    
def missing_words(status):
    match status:
        case 'name':
            return insert_name()
        case "address":
            return insert_address()
        case "NIC":
            return insert_nic()
        case "email":
            return insert_email()
        case "complain":
            return insert_complaint()
        case "mobile":
            return insert_mobile()
        case _:
            return "...."
            
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=2)
            
#from playsound import playsound
            
def insert_name():
  engine.say("Please tell your name")
  engine.runAndWait()
  with my_mic as source:
    print("Say your name!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  print(r.recognize_google(audio))
  file_object.write(" My name is "+ r.recognize_google(audio))
  return "name is added"
  
def insert_address():
  engine.say("Please tell your address")
  engine.runAndWait()
  #address = input("Enter address: ")
  with my_mic as source:
    print("Say your address!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  print(r.recognize_google(audio))
  file_object.write(" My address is "+ r.recognize_google(audio))
  return "address is added"
  
def insert_nic():
  engine.say("Please tell your id number")
  engine.runAndWait()
  #nic = input("Enter nic: ")
  with my_mic as source:
    print("Say your id!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  print(r.recognize_google(audio))
  file_object.write(" My NIC number is "+ r.recognize_google(audio))
  return "nic is added"
  
def insert_email():
  engine.say("Please tell your email")
  engine.runAndWait()
  #email = input("Enter mail: ")
  with my_mic as source:
    print("Say your email!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  print(r.recognize_google(audio)+"@gmail.com")
  file_object.write(" My email is "+ r.recognize_google(audio)+"@gmail.com")
  return "email is added"
  
def insert_complaint():
  engine.say("Please tell your complaint")
  engine.runAndWait()
  #complaint = input("Enter complaint : ")
  with my_mic as source:
    print("Say your complaint!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  print(r.recognize_google(audio))
  file_object.write(" Complaint is "+ r.recognize_google(audio))
  return "complaint is added"
  
def insert_mobile():
  engine.say("Please tell your telephone number")
  engine.runAndWait()
  #mobile = input("Enter mobile : ")
  with my_mic as source:
    print("Say your telno!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  mobile = "0"+ r.recognize_google(audio)
  print(mobile)
  if re.match("^0[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", mobile) :
	  print(mobile)
  else :
	  engine.say("Yout number is incorrect so Please type your telephone number")
	  engine.runAndWait()
	  mobile = input("Enter mobile : ")		
  #print(r.recognize_google(audio))
  file_object.write(" My contact number is "+ mobile)
  return "mobile is added"
            
if __name__ == "__main__":
	t_list=text.split()
c_list='name','address','NIC','email','complain','mobile'
print(Diff1(c_list,t_list))
x=Diff1(c_list,t_list)
for y in x: print(missing_words(y))
file_object.close()

readfile = open('pro.txt', 'r')
for line in readfile:
        d_list = line.split()
        n_index=d_list.index("name")
        ad_index=d_list.index("address")
        e_index=d_list.index("email")
        m_index=d_list.index("contact")
        nic_index=d_list.index("NIC")
        c_index=d_list.index("complain")
#print(n_index)
d_name=""+d_list[n_index + 2]+" "+d_list[n_index + 3]
print("Name - "+d_name)
d_address=""+d_list[ad_index + 2]#+" "+d_list[ad_index + 4]+" "+d_list[ad_index + 5]
print("Address - "+d_address)
d_email=""+d_list[e_index + 2]
print("Email - "+d_email)
d_mobile=""+d_list[m_index + 3]
print("Mobile - "+d_mobile)
d_nic=""+d_list[nic_index + 3]+""+d_list[nic_index + 4]+""+d_list[nic_index + 5]+"V"
print("NIC - "+d_nic)
d_com=""+d_list[c_index + 3]
print("Complain - "+d_com)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employee"
)

mycursor = mydb.cursor()
#print(mycursor.lastrowid)

sql = "INSERT INTO tbl_complaint (id,fullname, address, email, mobile, nic, complaintdetails) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (12, d_name, d_address, d_email, d_mobile, d_nic, d_com)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

'''
server= smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("complaintpolice66@gmail.com","police@123")
server.sendmail("complaintpolice66@gmail.com","vbmarambe@gmail.com","Your complaint is sucessfully filed")
server.quit()
'''




    
    


