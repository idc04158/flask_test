from flask import Flask, render_template, request 
app = Flask(__name__)
@app.route('/')
def homepage_con() -> 'html': 
    print("Homepage") #cmd 에 찍힘
    return render_template("m_reg.html")

#http:localhost/m_reg/

@app.route('/m_reg/', methods=['POST'])
def add_member_controller() -> 'html': 
    name = request.form['m_name']
    print(name)
    addr = request.form['m_addr'] 
    print(addr)
    return render_template("return.html", n=name, a=addr)

app.run(debug=True) 


"""

from flask import Flask, render_template, request #flask 플러그인 불러오기
app = Flask(__name__) #flask프레임워크의 특수기능 불러옴 app은 이름을 바꿀 수 있지만 보통 그냥 app으로 씀
@app.route('/',  methods=['POST'])#post로 전송된 것을 받음
def add_member_controller() -> 'html': #ulr을 뭘 써서 들어갔냐에 따라서..?
    print("from m_reg.html")#cmd창에 결과가 찍힘
    return "seccess!" #브라우저에 결과 찍힘
app.run(debug=True) #어플 실행시켜서 웹서버를 띄움

@app.route('/m_search/')
def search_member_con() -> 'html': 
    print("search page")
    return "searchpage!" 

"""