from flask import Flask,render_template,request
import ibm_db

app = Flask(__name__)


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;UID=sdf32418;PWD=NA3rHLfbyWWtcdZI;SECURITY=ssl;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt",'','')
print(ibm_db.active(conn))
@app.route("/")
def index():
     return render_template("index.html")
@app.route("/contact")
def contact():
     return render_template("contact.html")
@app.route("/login", methods=["GET","POST"])
def login():
     if request.method == "POST":
          uname = request.form['username']
          pword = request.form['password']
          print(uname,pword)
          sql = 'SELECT * FROM REGISTER WHERE USERNAME=? AND PASSWORD=?'
          stmt = ibm_db.prepare(conn, sql)
          ibm_db.bind_param(stmt, 1,uname)
          ibm_db.bind_param(stmt, 2,pword)
          ibm_db.execute(stmt)
          out = ibm_db.fetch_assoc(stmt)
          print(out)
          if out==False:
               msg = "INVALID CREDENTIALS"
               return render_template("login.html",login_message =msg)
          else:
               role = out['ROLE']

               if role == 0:
                    return render_template("adminprofile.html")
               elif role ==1:
                    return render_template("studentprofile.html")
               else:
                    return render_template("facultyprofile.html")
          return render_template("login.html")
@app.route("/profile")
def profile():
     return render_template("profile.html")
@app.route("/signup")
def signup():
     return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug= True,host="0.0.0.0")
