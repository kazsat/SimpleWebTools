from flask import request, redirect, url_for, render_template, flash
from simplewebtools import app, db
from simplewebtools.models import Entry
from simplewebtools.models import SqlResult
from simplewebtools.sqlbeautify import SQLBeautifier
from simplewebtools.textsorter import TextSorter

@app.route('/')
def show_home():
    return render_template('home.html')


@app.route('/memo')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

# @app.route('/')
# def show_boot_sample():
#     return render_template('boot_sample.html')


@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/sql-beautifier')
def show_sqlbeautifier():
    return render_template('sql_beautifier.html')
    # , beautified_sql=beautified_sql)


@app.route('/beautify', methods=['POST'])
def beautify_sql():

    original_sql = request.form['original-sql']

    sqlb = SQLBeautifier()
    sqlb.set_original_sql(original_sql)
    sqlb.beautify()

    beautified_sql = sqlb.get_beautified_sql()

    flash('Your SQL was successfully beautified')

    return render_template('sql_beautifier.html', original_sql=original_sql, beautified_sql=beautified_sql)

    # entry = Entry(
    #         title=request.form['title'],
    #         text=request.form['text']
    #         )
    # db.session.add(entry)
    # db.session.commit()
    #
    # id = db.Column(db.Integer, primary_key=True)
    # original_sql = db.Column(db.Text)
    # beautified_sql = db.Column(db.Text)
    # entry_user = db.Column(db.Text)
    # entry_date = db.Column(db.Date)
    # update_user = db.Column(db.Text)
    # update_date = db.Column(db.Date)

    # return redirect(url_for('show_sqlbeautifier'), beautified_sql=beautified_sql)
    # return redirect(url_for('show_sqlbeautifier'), beautified_sql='aaa')
    # return redirect(url_for('show_sqlbeautifier'))



@app.route('/text-sorter')
def show_textsorter():
    return render_template('textsorter.html')


@app.route('/sort', methods=['POST'])
def sort():
    original_text = request.form['original-text']

    texts = TextSorter()
    texts.set_original_text(original_text)

    result_text = texts.text_sort()

    return render_template('textsorter.html', original_text=original_text, result_text=result_text)


@app.route('/dupeliminator')
def show_dupeliminator():
    return render_template('dupeliminator.html')


@app.route('/eliminate')
def eliminate():
    return render_template('dupeliminator.html')



