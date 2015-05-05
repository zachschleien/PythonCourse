##################
#name: Zach Schleien
#date: April 27, 2015
#python version: 2.7.9
#program description: The user can quickly and easily create a cover letter within minutes.
##################

from Tkinter import *
import datetime

def windowOpen(winname, winlabel):
    newwin = Toplevel()
    newwin.title(winname)
    newwin.minsize(width=150,height=50)
    showlabel = Label(newwin, text=winlabel)
    showlabel.grid(row=0,column=0)

def writeletter():
    outFile = file(str(datetime.datetime.utcnow()) + ".txt", 'w')
    printstreet = streetvar.get()
    printlocation = locationvar.get()
    printcompany = companyvar.get()
    printsubject = subjectvar.get()
    printsalutation = salutationvar.get()
    printnews = newsvar.get()
    printmission = missionvar.get()
    printeducation = educationvar.get()
    printwhyyou = whyyouvar.get()
    printexperiences = experiencesvar.get()
    printother = othervar.get()
    printsignoff = signoffvar.get()


    outFile.write(printstreet + "\n")
    outFile.write(printlocation + "\n" "\n") 
    outFile.write(printcompany + "\n") 
    outFile.write(printsubject + "\n" "\n") 
    outFile.write(printsalutation + "\n" "\n") 
    outFile.write(printnews) 
    outFile.write(" " + printmission + "\n" "\n")  
    outFile.write(printeducation + "\n" "\n") 
    outFile.write(printwhyyou + "\n" "\n") 
    outFile.write(printexperiences + "\n" "\n") 
    outFile.write(printother + "\n" "\n") 
    outFile.write("Sincerely," "\n" + printsignoff ) 

    outFile.flush()

#create a main window with a title
winspace = Tk()
winspace.title("Cover Letter")

#set the minimum size of the window
winspace.minsize(width=600, height=550)

#create the label and buttons for the window
menuLabel = Label(winspace, text="Select An Option")

#create a second window
frame1 = Frame(winspace)

#create the buttons for the window
streetButton = Button(frame1, text="Template")

#Set the command of the buttons
streetButton.configure(command=lambda:windowOpen("Template","321 Comstock Ave"))

#Use a label to instruct the user to type in a name
instruct = Label(frame1,text="Enter your Street Address", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
streetvar = StringVar()

#create an entry box for the string variable
enterstreet = Entry(frame1, textvariable=streetvar)
enterstreet.pack(side = LEFT)

#pack buttons in default position in window
streetButton.pack(side = LEFT)

#pack frame
frame1.pack()

#create a second window
frame2 = Frame(winspace)

#create the buttons for the window
locationButton = Button(frame2, text="Template")

#Set the command of the buttons
locationButton.configure(command=lambda:windowOpen("Template","Syracuse, NY 13201"))

#Use a label to instruct the user to type in a name
instruct = Label(frame2,text="Enter your City, State, and Zip code", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
locationvar = StringVar()

#create an entry box for the string variable
enterlocation = Entry(frame2, textvariable=locationvar)
enterlocation.pack(side = LEFT)

#pack buttons in default position in window
locationButton.pack(side = LEFT)

#pack frame
frame2.pack()

#create a second window
frame3 = Frame(winspace)

#create the buttons for the window
companyButton = Button(frame3, text="Template")

#Set the command of the buttons
companyButton.configure(command=lambda:windowOpen("Template","Deloitte"))

#Use a label to instruct the user to type in a name
instruct = Label(frame3,text="Enter the Company Name", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
companyvar = StringVar()

#create an entry box for the string variable
entercompany = Entry(frame3, textvariable=companyvar)
entercompany.pack(side = LEFT)

#pack buttons in default position in window
companyButton.pack(side = LEFT)

#pack frame
frame3.pack()

#create a second window
frame4 = Frame(winspace)

#create the buttons for the window
subjectButton = Button(frame4, text="Template")

#Set the command of the buttons
subjectButton.configure(command=lambda:windowOpen("Template","RE: Consulting Intern"))

#Use a label to instruct the user to type in a name
instruct = Label(frame4,text="Enter Subject Line", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
subjectvar = StringVar()

#create an entry box for the string variable
entersubject = Entry(frame4, textvariable=subjectvar)
entersubject.pack(side = LEFT)

#pack buttons in default position in window
subjectButton.pack(side = LEFT)

#pack frame
frame4.pack()

#create a second window
frame5 = Frame(winspace)

#create the buttons for the window
salutationButton = Button(frame5, text="Template")

#Set the command of the buttons
salutationButton.configure(command=lambda:windowOpen("Template","Dear Hiring Manager,"))

#Use a label to instruct the user to type in a name
instruct = Label(frame5,text="Enter Your Salutation", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
salutationvar = StringVar()

#create an entry box for the string variable
entersalutation = Entry(frame5, textvariable=salutationvar)
entersalutation.pack(side = LEFT)

#pack buttons in default position in window
salutationButton.pack(side = LEFT)

#pack frame
frame5.pack()

#create a second window
frame6 = Frame(winspace)

#create the buttons for the window
newsButton = Button(frame6, text="Template")

#Set the command of the buttons
newsButton.configure(command=lambda:windowOpen("Template","Congratulations on closing last quarter up 23%"))

#Use a label to instruct the user to type in a name
instruct = Label(frame6,text="Enter Any Recent News About the Company", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
newsvar = StringVar()

#create an entry box for the string variable
enternews = Entry(frame6, textvariable=newsvar)
enternews.pack(side = LEFT)

#pack buttons in default position in window
newsButton.pack(side = LEFT)

#pack frame
frame6.pack()

#create a second window
frame7 = Frame(winspace)

#create the buttons for the window
missionButton = Button(frame7, text="Template")

#Set the command of the buttons
missionButton.configure(command=lambda:windowOpen("Template","I am a huge fan of Deloitte and fully invested in your mission of aspiring to excellence and the first choice of the most sought-after clients and talent."))

#Use a label to instruct the user to type in a name
instruct = Label(frame7,text="Their Mission and/or Values", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
missionvar = StringVar()

#create an entry box for the string variable
entermission = Entry(frame7, textvariable=missionvar)
entermission.pack(side = LEFT)

#pack buttons in default position in window
missionButton.pack(side = LEFT)

#pack frame
frame7.pack()

#create a second window
frame8 = Frame(winspace)

#create the buttons for the window
educationButton = Button(frame8, text="Template")

#Set the command of the buttons
educationButton.configure(command=lambda:windowOpen("Template","I am currently enrolled in a Master of Science in Information Management program at the School of Information Studies at Syracuse University (Dec '15). My focus is in project management and data science. I have taken courses such as, Project Management, Database Management, Systems Analysis and currently taking Python, Marketing Analytics and Applied Data Science. "))

#Use a label to instruct the user to type in a name
instruct = Label(frame8,text="Your Education", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
educationvar = StringVar()

#create an entry box for the string variable
entereducation = Entry(frame8, textvariable=educationvar)
entereducation.pack(side = LEFT)

#pack buttons in default position in window
educationButton.pack(side = LEFT)

#pack frame
frame8.pack()

#create a second window
frame9 = Frame(winspace)

#create the buttons for the window
whyyouButton = Button(frame9, text="Template")

#Set the command of the buttons
whyyouButton.configure(command=lambda:windowOpen("Template","Given my character and experiences as a student as well as an entrepreneur, I believe I would be a great fit for Deloitte. I consider myself to be analytical, detail-oriented as well as a team player. This summer my goal is to intern for a consulting company as well as to be in a strong learning environment."))

#Use a label to instruct the user to type in a name
instruct = Label(frame9,text="Why Would You be a Great Fit", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
whyyouvar = StringVar()

#create an entry box for the string variable
enterwhyyou = Entry(frame9, textvariable=whyyouvar)
enterwhyyou.pack(side = LEFT)

#pack buttons in default position in window
whyyouButton.pack(side = LEFT)

#pack frame
frame9.pack()

#create a second window
frame10 = Frame(winspace)

#create the buttons for the window
experiencesButton = Button(frame10, text="Template")

#Set the command of the buttons
experiencesButton.configure(command=lambda:windowOpen("Template","My passion lies in digital marketing, user acquisition, and providing solutions to meet challenging business demands. Recently, I launched a website called Rotoworld.com. I manage the Google Analytics, drive growth and write the content. I prioritize consumer needs based on quantitative as well as qualitative research when writing content. To date, I have grown Rotoworld.com from an idea to a bustling blog that now receives upwards of 20,000 unique views/week."))

#Use a label to instruct the user to type in a name
instruct = Label(frame10,text="Previous Experiences / Achievements", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
experiencesvar = StringVar()

#create an entry box for the string variable
enterexperiences = Entry(frame10, textvariable=experiencesvar)
enterexperiences.pack(side = LEFT)

#pack buttons in default position in window
experiencesButton.pack(side = LEFT)

#pack frame
frame10.pack()

frame11 = Frame(winspace)

#Use a label to instruct the user to type in a name
instruct = Label(frame11,text="Other Passions / Achievements", pady=10)
instruct.pack(side = LEFT)

#create the buttons for the window
otherButton = Button(frame11, text="Template")

#Set the command of the buttons
otherButton.configure(command=lambda:windowOpen("Template","I am also involved on campus. I have taken a leadership position in iSGO, a graduate student organization, serving as Vice President."))

#create a variable of the StringVar() class to hold the data
othervar = StringVar()

#create an entry box for the string variable
enterother = Entry(frame11, textvariable=othervar)
enterother.pack(side = LEFT)

#pack buttons in default position in window
otherButton.pack(side = LEFT)

#pack frame
frame11.pack()

frame12 = Frame(winspace)

#create the buttons for the window
signoffButton = Button(frame12, text="Template")

#Set the command of the buttons
signoffButton.configure(command=lambda:windowOpen("Template","Michael Smith"))

#Use a label to instruct the user to type in a name
instruct = Label(frame12,text="Enter First and Last Name", pady=10)
instruct.pack(side = LEFT)

#create a variable of the StringVar() class to hold the data
signoffvar = StringVar()

#create an entry box for the string variable
signoff = Entry(frame12, textvariable=signoffvar)
signoff.pack(side = LEFT)

#pack buttons in default position in window
signoffButton.pack(side = LEFT)

#pack frame
frame12.pack()

#create buttons
okButton = Button(winspace, text = "Submit", command = writeletter, pady=20)

#pack buttons in default position in window
okButton.pack()

#display the window
winspace.mainloop()

#close file
outFile.close() 




