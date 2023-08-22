from flask import Flask, render_template, request
from email.message import EmailMessage
import smtplib
import pandas as pd
app = Flask(__name__ )


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/Project', methods=["GET", "POST"])
def Project():
    return render_template('Project.html')


@app.route('/Event', methods=["GET", "POST"])
def Event():
    return render_template('Event.html')


@app.route('/Resourses', methods=["GET", "POST"])
def Resourses():
    return render_template('Resourses.html')


@app.route('/Media', methods=["GET", "POST"])
def Media():
    return render_template('Media.html')


@app.route('/ROutcome', methods=["GET", "POST"])
def ROutcome():
    return render_template('ROutcome.html')

@app.route('/Contact', methods=["GET", "POST"])
def Contact():

    if(request.method=='POST'):
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        msg = EmailMessage()
        msg['Subject'] = "GET IN TOUCH"
        s.starttls()
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        print(name,email,message)
        message=message+"\n"+"Name :-"+str(name)+"\n"+"Email :-"+str(email)
        msg.set_content(message)
        
        
        msg['From'] = "tempethno@gmail.com"
        # msg['From'] = "ethnographylab@iiitd.ac.in"

        msg['To'] = "paro.mishra@iiitd.ac.in"
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("tempethno@gmail.com", "ndunlhrhpqzxacdn") 
        # server.login("ethnographylab@iiitd.ac.in", "ethnographylabsssh")    
        
        server.send_message(msg)
        server.quit()
        return render_template('Confirmation.html')
        

    return render_template('Contact.html')


df=pd.read_csv('profile_data.csv')
names=df['Name'].values
# print(df['Name'])
emails=df['Email Address'].values
# print(df['Email Address'])
pics=df['Please upload your picture for the ethnography lab website '].values
# print(df['Please upload your picture for the ethnography lab website '])
areas=df['PhD Research Topic/ Area (Tentative topics are also fine)'].values
# print(df['PhD Research Topic/ Area (Tentative topics are also fine)'])
rollnos=df['Roll No.'].values


data=[]
for i in range(len(names)):
    k=(names[i],rollnos[i],pics[i],areas[i],emails[i])
    data.append(k)
print(data)

@app.route('/People', methods=["GET", "POST"])
def People():
    
    return render_template('People.html',data=data)


@app.route('/Publications', methods=["GET", "POST"])
def Publications():
    return render_template('Publications.html')


@app.route('/Conference', methods=["GET", "POST"])
def Conference():
    return render_template('Conference.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
