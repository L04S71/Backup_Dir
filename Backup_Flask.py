from flask import Flask, render_template, url_for, g, request, redirect, send_from_directory
import os
from datetime import datetime
import shutil
import glob
import time

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/create_backup', methods=['GET', 'POST'])
def backup():
    if request.method == 'POST':
        file_to_backup = request.form['path1']
        copied_file = request.form['path2']
        make_reserve_arc(file_to_backup, copied_file)
    return render_template("Backup.html")


def make_reserve_arc(source, dest):
    shutil.make_archive(r'backup_' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")), r'zip', source)
    glob1 = glob.glob(r'.\*.zip')
    shutil.move(str(source) + str(glob1[0]), str(dest) + str(glob1[0]))


if __name__ == '__main__':
    app.run()
