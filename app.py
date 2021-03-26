from flask import Flask, render_template, Response

app = Flask(__name__)



@app.route('/', defaults={"input_name" : "file1"})
@app.route('/<input_name>/')
@app.route('/<input_name>/<int:range1>/<int:range2>')
def home(input_name=None, range1=None, range2=None):
    filename = f"./src/files/{input_name}.txt"

    #here for special case file 4 we need to display the content as html 
    #so it will directly send to Response
    if input_name == "file4":
        with open(filename, 'r', encoding="utf-16") as e:
            content = e.read()
        return Response(content, mimetype='text/html')

    #else for normal files we can you common generic code 
    else:
        #the empty list will pass to HTML for extracting each item
        mylist = []
        with open(filename, 'r') as f:
            #loop checks if user has pass input range for selected lines 
            #and append that lines into mylist
            #if user did not pass the inputs it will go ahead and append all elements
            for num, line in enumerate(f):
                if range1 and range2:
                    if num in range(range1, range2+1):
                        mylist.append(' '.join(list(filter(lambda x: x not in {'\t', '\n'}, line.split()))))                  
                else:
                    mylist.append(' '.join(list(filter(lambda x: x not in {'\t', '\n'}, line.split()))))
        return render_template("index.html", file_name=input_name, file_data=mylist )

if __name__ == '__main__':
    app.run(debug=True)