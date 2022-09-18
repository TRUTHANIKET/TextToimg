from flask import Flask, redirect ,render_template, request , redirect

from PIL import Image,ImageDraw,ImageFont



app = Flask(__name__)



@app.route("/")
def html():
    
    return render_template("index.html")


@app.route("/",methods=['GET','POST'])
def push():
    text=request.form['text'] 
    data=request.form['data']   
    fontdata=int(data)
    fant=request.form.get('font')
    
    img=Image.new('RGB',(1080,1220),color=(255,255,255))
    print(img.size)
    d=ImageDraw.Draw(img)
    #'static/fonts/katyfont.ttf'
    fnt = ImageFont.truetype(font=fant, size=fontdata)
   
    # fnt=ImageFont.truetype("arial.ttf",15)
    d.text((30,60),text,font=fnt,fill=(61,74,177))
    img.save('static/images/yo.png')

    return render_template("index.html",text=text,data=fontdata)


# @app.route("/show",methods=["GET","POST"])
# def show():
#     alltodo=Todo.query.all()
#     print(alltodo)
    
#     return "this is a show page"

@app.route("/result",methods=["GET","POST"])
def result():
    
    return render_template("result.html")



if __name__=="__main__":
    app.run(debug=True)
    