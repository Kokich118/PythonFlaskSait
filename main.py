from flask import Flask, render_template, url_for, request, redirect, session

from requests import Register_request, Comments_request, Game_request_comment, Game_request_data, Games_request, \
    Index_request_login, Index_request_admin, Input_request, Insert_game_admin, Game_delete_request, Update_request_game

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b39eb86d154f0a58f10ecaf2f1903eaeb412cf65'
app.config['UPLOAD_FOLDER'] = './static/image/games/'


@app.route("/")
def index():
    data = Games_request.request()

    out = request.args.get('OUT')
    if out != None:
        session.clear()

    id = session.get('id')
    output = 0
    admin = 0
    name = ""
    if id != None:
        output = 1
        admin = Index_request_admin.request(id)
        name = Index_request_login.request(id)

    if request.args.get('BlockTrue') == '1':
       return render_template("index.html", game_data=data, BlockTrue=1, Output=output, admin=admin, name=name)

    if request.args.get('BlockTrue') == '2':
       return render_template("index.html", game_data=data, BlockTrue=2, Output=output, admin=admin, name=name)

    return render_template("index.html", game_data=data, Output=output, admin=admin, name=name)


@app.route("/input", methods={'POST', 'GET'})
def input():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        id = Input_request.request(login, password)
        if id != 0:
            session['id'] = id
            return redirect(url_for('.index', BlockTrue=1))
        else:
            return render_template("input.html", login=1)


    return render_template("input.html", login=0)


@app.route("/register", methods={'POST', 'GET'})
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        email = request.form.get('mail')
        if password != password2:
            return render_template("register.html", BlockError=2)
        if Register_request.request(login, password, email) == 1:
            return redirect(url_for('.index', BlockTrue=2))
        else:
            return render_template("register.html", BlockError=1)
    return render_template("register.html")


@app.route("/game", methods={'POST', 'GET'})
def game():
    if request.method == 'POST':
        id_game = request.form.get('id')
        value = Game_request_data.request(id_game)
        if session.get('id') != None:
            Game_request_comment.request(id_game, session['id'], request.form.get('text'), request.form.get('grade'))
            comments = Comments_request.request(id_game)
            return render_template("game.html", value=value[0], BlockTrue=1, comments=comments)
        else:
            comments = Comments_request.request(id_game)
            return render_template("game.html", value=value[0], BlockNull=1, comments=comments)
    id_game = request.args.get('id')
    value = Game_request_data.request(id_game)
    comments = Comments_request.request(id_game)
    return render_template("game.html", value=value[0], comments=comments)


@app.route("/panel_admin", methods={'POST', 'GET'})
def panel_admin():
    global games_data, status
    games_data = Games_request.request()
    games_data.reverse()
    if request.method == 'POST':
        status = request.form.get('status')

        if status == '1':
            return render_template("panel_admin.html", status=status, games_data=games_data)

        if status == '2':
            id = request.form.get('id')
            game_data = Game_request_data.request(id)
            return render_template("panel_admin.html", status=status, game_data=game_data[0], out='1')

        if status == '3':
            id = request.form.get('id')
            photo = Game_delete_request.request(id)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], photo[0][0]))
            games_data = Games_request.request()
            games_data.reverse()
            return render_template("panel_admin.html", status='1', games_data=games_data, delete='1')

        if status == '4':
            return render_template("panel_admin.html", status=status, games_data=games_data, out='1')

        if status == '5':
            name = request.form.get('name')
            cost = request.form.get('cost')
            text = request.form.get('text')
            file = request.files["file"]
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Insert_game_admin.request(name, cost, text, filename)
            games_data = Games_request.request()
            games_data.reverse()
            return render_template("panel_admin.html", status='1', games_data=games_data, BlockAddTrue='1')

        if status == '6':
            id = request.form.get('id')
            name = request.form.get('name')
            cost = request.form.get('cost')
            text = request.form.get('text')
            file = request.files['file']
            filename = file.filename
            if filename == '':
                Update_request_game.requestNotFile(id, name, text, cost)
            else:
                photo = Game_request_data.photo(id)
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], photo[0][0]))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                Update_request_game.request(id, name, text, cost, filename)
            return render_template("panel_admin.html", status='1', games_data=games_data, change='1')


if __name__ == "__main__":
    app.run()