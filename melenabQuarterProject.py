#Melena Braggs Quater Project Apr 29 19

import os
import webbrowser
from graphics import *
import random

def color():
    r= random.randint(0,255) #generates random colors
    g=random.randint(0,255)
    b=random.randint(0,255)
    c=color_rgb(r,g,b)
    return c



#This file read the data line by and seperates it into a list of lists 
def read_data():
    thedata= []
    clearlist= [] #this list will contain organized data with dates 1st and all the info after  
    fileboy= open("KMDW.csv", "r")
    for line in fileboy:
        line= line[0:len(line)-1]
        thedata.append(line)
    thedata= thedata[1:len(thedata)]

    for i in range(len(thedata)):
        smallList= thedata[i].split(",") #this seperates the items in the list by the ,
        clearlist.append(smallList)
    return clearlist





#This function finds the highest and low temperature during the year
def data_analyze_temps():
    clearlist= read_data()
    temphighs=[]
    templows=[]
    for i in clearlist:
        templows.append(i[2])
        temphighs.append(i[3])
    print("The highest temperature was", max(temphighs))
    print("The lowest temperature was", min(templows))
    
    return temphighs



    

    



#This is the function that finds the  record highest and the lowest temp
def rec_highest_and_lowestTemp():
    clearlist= read_data()
    h=0 #this is the highest temp and 0 is used as a counter`
    l=0 #the lowest temp
    hyear= 0 #the year with the highest temp
    lyear= 0 #the year with the lowest temp
    for i in clearlist:
        if eval(i[7]) > h:
            h= eval(i[7])
            hyear= eval(i[9])
        if eval(i[6]) < l:
                l= eval(i[6])
                lyear=i[8]
    print("The highest temperature was," ,h, "in the year", hyear)
    print("The lowest temperature was," ,l, "in the year", lyear)

                
def high_temp_ave():
    clearlist= read_data()
    highs= []
    for i in clearlist:
        highs.append(i[3])
    total = 0
    numofele= len(highs) #this is the number of items in the list 
    for i in highs:
        total= total+ int(i) #this gets to add up all the number in the list
    mean=total/numofele
    return mean
   
def low_temp_ave():
    clearlist= read_data()
    lows= []
    for i in clearlist:
        lows.append(i[2])
    total = 0
    numofele= len(lows) #this is the number of items in the list 
    for i in lows:
        total= total+ int(i) #this gets to add up all the number in the list
    mean=total/numofele
    return mean

def rainFall_ave():
    clearlist= read_data()
    rain= []
    for i in clearlist:
        rain.append(i[10])
    total = 0
    numofele= len(rain) #this is the number of items in the list 
    for i in rain:
        total= total+ float(i) #this gets to add up all the number in the list
    mean=total/numofele
    return mean

    
    
def rain_data():
    clearlist=read_data()
    rainhighs=[]
    rainYear=[]
    for i in clearlist:
        rainhighs.append(i[12])
        rainYear.append(i[0])
    #print("The rain",rainhighs)
    #print("The year rains occur", rainYear) #I made these lines to see the list and to make sure they did what I want them to 
    rainYear= rainYear[11]

    print("The highest rainfall was", max(rainhighs), "inches on", rainYear)



def browseLocal(): 
    contents=createHTML
    filename = "tempBrowseLocal.html"
    output = open(filename, 'w')
    output.write(webpageText)
    output.close()
    webbrowser.open('file:///' + os.path.abspath(filename))




def createHTML(): #this is the code I got from class
  bgColor = input("What color do you want your background? ")
  txtColor = input("What color do you want your text? ")
  border= input("What color do you want your border?")
  clearlist= read_data()
  recordhigh=0
  recordlow=0
  record_rainfall=0

  avehightemp= high_temp_ave()
  avelowtemp= low_temp_ave()
  averain= rainFall_ave()
  
#This loop just finds the records numbers for each type of data using clearlist
  for i in clearlist:
      if int(i[7]) > int(recordhigh):
          recordhigh= i[7]
      if int(i[6]) > int(recordlow):
          recordlow= i[6]
      if float(i[12]) > float(record_rainfall):
          record_rainfall = i[12]
          
      
      
  contents = '''
<html>
    <head>
      <title>Students and Average Scores</title>
      <style>
           body { background-color:''' +bgColor + ''';
           color:''' + txtColor + '''; font-family: courier;}
           h1 { text-align: center;}
           div { text-align:center; border: 2px solid '''+border+''';
           border-style: dashed; }
           
        
      </style>
   </head>
    <body>
        <h1> Midway Airport Weather Infomation </h1>
        <div>
        <p> My data is cooler than the average temps of Midway airport. I found the average of my temps
        and compared to the average of the average temps over time. The temps from 2014-2015 were less than the average.</p>
        <br>
        <p> The average rainfall was 0.099 inches. I found this by adding all the actual rain values to
        list and then finding the average of that list. The average yearly rainfall for Midway is,0.11 inches.
        I found this by putting the average rainfall into a list and finding the mean of that list.</p>
        <br>
        <p> I would like to wind speeds included in this data set</p>

        <br>
        <p> Here is some data about Midway Airport from 2014-2015 </p>
        </div>
        <div>
        <table>
            <tr>
                <th>Type of Data</th>
                <th> Averages </th>
                <th> Records </th>
            </tr>
            <tr>
                <td> High Temp (in F) </td>
                <td>'''+str(avehightemp)+'''</td>
                <td>'''+str(recordhigh)+'''</td>
            </tr>
            <tr>
                <td> Low Temp (in F) </td>
                <td>'''+ str(avelowtemp)+'''</td>
                <td>'''+ str(recordlow)+'''</td>
            </tr>
            <tr>
                <td>RainFall (in in.) </td>
                <td>'''+str(averain)+ '''</td>
                <td>'''+ str(record_rainfall)+'''</td>
        </div>
        <img src="graph.PNG">



    '''
  ending = '''</body>
  </html>'''
  contents=contents+ ending
  return contents 

#Opens up HTML file
def browseLocal():
    contents=createHTML()
    filename = "tempBrowseLocal.html"
    output = open(filename, 'w')
    output.write(contents)
    output.close()
    webbrowser.open('file:///' + os.path.abspath(filename))

#The Temperature Graph
def temp_graph():
    clearlist= read_data()
    win= GraphWin("Temp Graph",700,700)
    win.setCoords(0,0,500,700)
    win.setBackground(color())

   

#The axes
    ave_yaxis_top= Point(50,650)
    ave_yaxis_bottom= Point(50,50)

    ave_yaxis= Line(ave_yaxis_top, ave_yaxis_bottom)
    ave_yaxis.draw(win)

    ave_xaxis_left= ave_yaxis_bottom
    ave_xaxis_right= Point(650,50)

    ave_xaxis= Line(ave_xaxis_left, ave_xaxis_right)
    ave_xaxis.draw(win)


#The y-axis hash marks. I choose the starting point based on the graphing window and what I thought would look nice.
    zero_hash_left= Point(45,50)
    zero_hash_right= Point(55,50)
    zero_hash= Line(zero_hash_left, zero_hash_right) 
    zero_hash.draw(win)
    zero= Text(Point(40,50),"-30.0")
    zero.draw(win)

#I mislabeled the underscored ones originally 
    t_hash_left= Point(45,200)
    t_hash_right= Point(55,200)
    t_hash= Line(t_hash_left, t_hash_right)
    t_hash.draw(win)
    nthirty= Text(Point(40,200),"0.0")
    nthirty.draw(win)
    

    s_hash_left= Point(45,350)
    s_hash_right= Point(55,350)
    s_hash= Line(s_hash_left, s_hash_right)
    s_hash.draw(win)
    thirty= Text(Point(40,350),"30.0")
    thirty.draw(win)

    n_hash_left= Point(45,500)
    n_hash_right= Point(55,500)
    n_hash= Line(n_hash_left, n_hash_right)
    n_hash.draw(win)
    six= Text(Point(40,500),"60.0")
    six.draw(win)

    o_hash_left= Point(45,650)
    o_hash_right= Point(55,650)
    o_hash= Line(o_hash_left, o_hash_right)
    o_hash.draw(win)
    twenty= Text(Point(45,650),"120.0")
    twenty.draw(win)

#The x-axis hash marks
    jul_hash_top= Point(100, 53)
    jul_hash_bottom= Point(100,47)
    jul_hash= Line(jul_hash_top, jul_hash_bottom)
    jul_hash.draw(win)
    jul= Text(Point(95,47),"Jul.")
    jul.draw(win)

    a_hash_top= Point(150, 53)
    a_hash_bottom= Point(150,47)
    a_hash= Line(a_hash_top, a_hash_bottom)
    a_hash.draw(win)
    aug= Text(Point(145,47),"Aug.")
    aug.draw(win)
    

    sep_hash_top= Point(200,53)
    sep_hash_bottom= Point(200,47)
    sep_hash= Line(sep_hash_top, sep_hash_bottom)
    sep_hash.draw(win)
    sep= Text(Point(195,50),"Sep.")
    sep.draw(win)

    oct_hash_top= Point(250, 53)
    oct_hash_bottom= Point(250,47)
    oct_hash= Line( oct_hash_top, oct_hash_bottom)
    oct_hash.draw(win)
    oct_= Text(Point(245,50),"Oct.")
    oct_.draw(win)

    nov_hash_top= Point(300, 53)
    nov_hash_bottom= Point(300,47)
    nov_hash= Line( nov_hash_top, nov_hash_bottom)
    nov_hash.draw(win)
    nov= Text(Point(295,47),"Nov.")
    nov.draw(win)
    

    dec_hash_top= Point(350, 53)
    dec_hash_bottom= Point(350,47)
    dec_hash= Line(dec_hash_top, dec_hash_bottom)
    dec_hash.draw(win)
    dec= Text(Point(345,47),"Dec.")
    dec.draw(win)

    jan_hash_top= Point(400, 53)
    jan_hash_bottom= Point(400,47)
    jan_hash= Line(jan_hash_top, jan_hash_bottom)
    jan_hash.draw(win)
    jan= Text(Point(395,47),"Jan.")
    jan.draw(win)

    feb_hash_top= Point(450, 53)
    feb_hash_bottom= Point(450,47)
    feb_hash= Line(feb_hash_top, feb_hash_bottom)
    feb_hash.draw(win)
    feb= Text(Point(445,47),"Feb")
    feb.draw(win)

    mar_hash_top= Point(500, 53)
    mar_hash_bottom= Point(500,47)
    mar_hash= Line(mar_hash_top, mar_hash_bottom)
    mar_hash.draw(win)

    apr_hash_top= Point(550, 53)
    apr_hash_bottom= Point(550,47)
    apr_hash= Line(apr_hash_top, apr_hash_bottom)
    apr_hash.draw(win)

    may_hash_top= Point(600, 53)
    may_hash_bottom= Point(600,47)
    may_hash= Line(may_hash_top, may_hash_bottom)
    may_hash.draw(win)

    jun_hash_top= Point(650, 53)
    jun_hash_bottom= Point(650,47)
    jun_hash= Line(jun_hash_top, jun_hash_bottom)
    jun_hash.draw(win)

    


    real_list= [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for x in range(len(real_list)-1):    
        for j in range(len(clearlist)-1): #These for make every type of data into it's own list and put those lists in a list
                real_list[x].append(clearlist[j][x])
    print(real_list)
    counter=0
    for i in range(len(real_list[0])):
        day= real_list[0][i] #This is every day 
        act_max= int(real_list[3][i])
        act_min=int(real_list[2][i])

        ave_max= int(real_list[5][i])
        ave_min= int(real_list[4][i])

        rec_max= int(real_list[7][i])
        rec_min= int(real_list[6][i])



#The operations occuring to the x and y values are there to scale the graph 
   
        actual= Line(Point((counter+5*600/50),(act_max*600/150+220)),Point(((counter+5*600/50)),(act_min*600/150+220)))
        average= Line(Point((counter+5*600/50), (ave_max*600/150+220)), Point(((counter+5*600/50)),(ave_min*600/150+220)))
        records= Line(Point((counter+5*600/50), (rec_max*600/150+220)), Point(((counter+5*600/50)), (rec_min*600/150+220)))
        counter=counter+1


        records.draw(win)
        records.setFill("black")
        
        actual.draw(win)
        actual.setFill("red")
        
        average.draw(win)
        average.setFill("yellow")
    title= Text(Point(260,660),"Temperature Plot")
    title.draw(win)
    key= Text(Point(460,600), "Key")
    key.draw(win)

#The keys for each type of data
    act_box= Rectangle(Point(460,580), Point(475, 575))
    act_box.setFill("red")
    act_box.draw(win)

    act_text= Text(Point(465,567),"Actual Temp.")
    act_text.draw(win)

    ave_box= Rectangle(Point(460,549), Point(475, 535))
    ave_box.setFill("yellow")
    ave_box.draw(win)

    ave_text= Text(Point(465,529),"Average Temp. ")
    ave_text.draw(win)

    rec_box= Rectangle(Point(460,499), Point(475, 495))
    rec_box.setFill("black")
    rec_box.draw(win)

    rec_text= Text(Point(465,489),"Record Temp.")
    rec_text.draw(win)
    

    



        
        
        
        
    


def rain_graph():
    clearlist= read_data()
    win= GraphWin("Rainfall Graph",600,600)
    win.setCoords(0,0,600,600)
    win.setBackground("white")

    title= Text(Point(300,580),"Precipitation Plot")
    title.draw(win)

#These are the axes for both the plots
    ave_yaxis_top=Point(50,550)
    ave_yaxis_bottom= Point(50,290)
    ave_yaxis= Line(ave_yaxis_top, ave_yaxis_bottom)
    ave_yaxis.draw(win)

    ave_xaxis_right= Point(590,290)
    ave_xaxis= Line(ave_xaxis_right, ave_yaxis_bottom)
    ave_xaxis.draw(win)

    other_yaxis_top= Point(50,290)
    other_yaxis_bottom= Point(50,10)
    other_yaxis= Line(Point(50,290), Point(50,10))
    other_yaxis.draw(win)

    other_xaxis_left= other_yaxis_bottom
    other_xaxis_right=Point(590,10)
    other_xaxis= Line(other_yaxis_bottom, other_xaxis_right)
    

   

    

#This is where I ask for user input
def main():
    answer= eval(input('''Enter 1 to see the highest and lowest temperatures.
Enter 2 to see the highest rainfall of the year
Enter 3 to see the Record High and Low Temperature and the year they occured
Enter 4 to see a webpage with weather data about Midway
Enter 5 to see a graph showing the temperature info

'''))
    yo= True
    while yo:
        if answer==1:
            data_analyze_temps()  
        elif answer==2:
            rain_data()
        elif answer==3:
            rec_highest_and_lowestTemp()
        elif answer==4:
            browseLocal()
        elif answer==5:
            temp_graph()
        answer= eval(input('''Enter 1 to see the highest and lowest temperatures.
Enter 2 to see the highest rainfall of the year
Enter 3 to see the Record High and Low Temperature and the year they occured
Enter 4 to see a webpage with weather data about Midway
Enter 5 to see a graph showing the temperature info
'''))
main()
            
        
        


    
    
                     
    
    

    

    

    
    

    

    
    

    

    

    
    
    

    

    
    

    
    
    
    
    


    

    

