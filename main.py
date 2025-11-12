from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def root():
   markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
   return render_template('index.html',markers=markers )
if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)

class F:
    def read(self, filename):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                for linea in f:
                    print(linea.strip())
        except FileNotFoundError:
            print ("El archivo no existe")
f = F()
f.read("DIVIPOLA.csv")

