from flask import Flask, render_template, request
from webargs import fields
from webargs.flaskparser import use_args
app = Flask(__name__)

from saps import saps_dataretrieve

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saps/')
@use_args({"name": fields.Str(required=True)}, location="query")
def saps(args):
    return "Hellosaps" + args["name"]

@app.route("/test" , methods=['GET', 'POST'])
def test():
    if (request.is_json):
        content = request.get_json()
        ic = content['ic']
        negeri = content['negeri']
        daerah = content['daerah']
        sekolah = content['sekolah']
        tahun = content['tahun']
        subj = content['subject']
    else:
        ic = request.form.get('ic')
        negeri = request.form.get('negeri')
        daerah = request.form.get('daerah')
        sekolah = request.form.get('sekolah')
        tahun = request.form.get('tahun')
        subj = request.form.get('subject')
    test = saps_dataretrieve(str(ic),str(negeri), str(daerah), str(sekolah), str(tahun), 'PEPERIKSAAN AKHIR TAHUN', int(subj))
    print(test)
    # return render_template('result.html', data=test) # just to see what select is
    return test

if __name__ == '__main__':
  app.run(host="192.168.0.157",threaded=True, debug=True)
 