from flask import Flask, render_template, request, redirect
app = Flask(__name__)

responses = [{'Name': 'Chungus', 'Question 1': 'B', 'Question 2': 'B', 'Question 3': 'B', 'Question 4': 'B', 'Question 5': 'B', 'Question 6': 'B', 'Question 7': 'B', 'Question 8': 'B', 'Question 9': 'B'},{'Name': 'T-series', 'Question 1': 'A', 'Question 2': 'A', 'Question 3': 'A', 'Question 4': 'A', 'Question 5': 'A', 'Question 6': 'A', 'Question 7': 'A', 'Question 8': 'A', 'Question 9': 'A'}]

@app.route('/')
def student():
   print(responses)
   return render_template('client.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.to_dict()
      responses.append(result)
      return render_template("result.html", result=result)
  
@app.route('/match', methods=['POST','GET'])
def match():
   if request.method=='POST':
      max_same = 0
      counts = []
      person = responses[len(responses) - 1]
      match = {'Name': 'nobody'}

     
      if len(responses) > 2:
         for r in range(len(responses) - 2): #indexes of all items except end
            current_dict = responses[r]
            count_same = 0
            if current_dict["Question 1"] == person["Question 1"]:
               count_same += 1
            if current_dict["Question 2"] == person["Question 2"]:
               count_same += 1
            if current_dict["Question 3"] == person["Question 3"]:
               count_same += 1
            if current_dict["Question 4"] == person["Question 4"]:
               count_same += 1 
            if current_dict["Question 5"] == person["Question 5"]:
               count_same += 1
            if current_dict["Question 6"] == person["Question 6"]:
               count_same += 1
            if current_dict["Question 7"] == person["Question 7"]:
               count_same += 1
            if current_dict["Question 8"] == person["Question 8"]:
               count_same += 1
            if current_dict["Question 9"] == person["Question 9"]:
               count_same += 1 
               
            if count_same > max_same:
               max_same = count_same
               match = responses[r]
               
               
              # return redirect("https://chat-project-fa27d.firebaseapp.com/")      
               
      return "Your Match: " + match["Name"] + "\n" +' <p><a href="https://chat-project-fa27d.firebaseapp.com/" a>Click Here to Chat with Your Match</a> '
   

                #countSame = 0  
                #for d in dictionary:
                     
                    #countSame++ if same
                    #counts.append(countSame) 

                    #if countSame > max_same:
                        #max_same = countSame
                        #match = d
if __name__ == '__main__':
   app.run(debug = True)





