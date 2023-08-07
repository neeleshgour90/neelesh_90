from flask import Flask,url_for,redirect

app= Flask(__name__)

@app.route("/home")
def home():
 return "WELCOME ALL"    
@app.route("/hello")
def hello():
   return "HELLO WORLD"
@app.route("/HII")
def HII():
   return "HELLO ALL FACULTIES WELCOME TO FDP"
@app.route("/user/enter")
def user(enter):
   if enter == "WELCOME":
      return redirect(url_for("home"))
   elif enter == "hello":
      return redirect(url_for("hello"))
   else:
      return redirect(url_for("HII"))
   

if __name__ == "__main__":
    app.run(debug = True )