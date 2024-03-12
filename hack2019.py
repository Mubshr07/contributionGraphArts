import os
from random import randint
import numpy as np
from datetime import datetime, timedelta

# Define the date 
date_2019 = datetime(2019, 1, 6) # year month day
# Get the current date
current_date = datetime.now()
# Calculate the difference in days
difference = current_date - date_2019
days_difference = difference.days
print(f"The number of days from {date_2019.strftime('%d-%B-%Y')} to today is {days_difference} days.")

htmlText= '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta http-equiv="X-UA-Compatible" content="ie=edge"> <title>Mubashir Iqbal | AI Researcher | System Engineer | Qt C++ Software & Web Engineer </title> </head> <body> <a href="https://github.com/Mubshr07" target="_blank"> Mubashir Iqbal | AI Researcher | System Engineer | Qt C++ Software & Web Engineer  </a> </body> </html> '

cppText = """#include <iostream>
using namespace std;

template <typename T>
class Array {
private:
    T* ptr;
    int size;

public:
    Array(T arr[], int s) {
        ptr = new T[s];
        size = s;
        for (int i = 0; i < size; i++)
            ptr[i] = arr[i];
    }

    void print() {
        for (int i = 0; i < size; i++)
            cout << " " << *(ptr + i);
        cout << endl;
    }
};

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    Array<int> a(arr, 5);
    a.print(); // Output: 1 2 3 4 5
    return 0;
}
"""
cssText= """ * { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; }
/* Style the header */
.header {
  background-color: #f1f1f1;
  padding: 30px;
  text-align: center;
  font-size: 35px;
}
/* Container for flexboxes */
.row {
  display: -webkit-flex;
  display: flex;
}
/* Create three equal columns that sits next to each other */
.column {
  -webkit-flex: 1;
  -ms-flex: 1;
  flex: 1;
  padding: 10px;
  height: 300px; /* Should be removed. Only for demonstration */
}
/* Style the footer */
.footer {
  background-color: #f1f1f1;
  padding: 10px;
  text-align: center;
}

"""

jsText= """const tmpl = "<h1>Hi, I'm {{name}}.</h1>";
const data = {
  name: "Mubashir Iqbal"
};
const template = templater(tmpl);
document.write(template(data));
"""

pythonText= """ def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
"""


# 2019 Softwares
dateArray = np.array([ [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
                      [ 0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0 ],
                      [ 0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0 ],
                      [ 0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,0 ],
                      [ 0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0 ],
                      [ 0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0 ],
                      [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ] ] )


indexColumn = 0
indexRows = 0

#days_difference += 1 
for j in range(days_difference, -1, -1):
    #print(" column: {}, row:{}".format(indexColumn, indexRows))
    if (dateArray[indexRows][indexColumn] == 1):
        for i in range(0, 7):
            current_date = datetime.now()
            commit_date = current_date  - timedelta(days=j)
            
            # Format the date in ISO 8601 format
            dateForCommit = commit_date.strftime('%Y-%m-%d %H:%M:%S')
           
            with open("htmlFileText.html", 'a') as file:
                file.write(htmlText)
                file.write('\n')
                        
            with open("qtCppFileText.cpp", 'a') as file:
                file.write(cppText)
                file.write('\n')

            with open("cssFileText.css", 'a') as file:
                file.write(cssText)
                file.write('\n')
            
            with open("jsFileText.js", 'a') as file:
                file.write(jsText)
                file.write('\n')
                
            with open("pythonFileText.py", 'a') as file:
                file.write(pythonText)
                file.write('\n')

            
            #staging
            os.system("git add .")
            commitText = "Saving progress on {} time {}".format(dateForCommit, j)
            commitCmd = 'git commit --date="'+dateForCommit+'" -m "'+commitText+'"'
            
            print(" --------------- ")
            #print(dateForCommit)
            print(commitCmd)
            print(" column: {}, row:{}".format(indexColumn, indexRows))
            print(" --------------- \n")

            # commit
            os.system(commitCmd) 
    
    indexRows += 1
    if(indexRows == 7):
        indexRows = 0
        indexColumn += 1
    if(indexColumn == 51): break

os.system("git push -u origin main") 






