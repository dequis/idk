from bottle import route, run, post, request, redirect
from bottle import jinja2_view as view
import butterdb
import math
database = butterdb.Database("emoticons", *(open("dual_ec_drbg").read().strip().split(":")))

@butterdb.register(database)
class Emoticon(butterdb.Model):
    def __init__(self, name, votes):
        self.name = self.field(name)
        self.votes = self.field(votes)

get_all_shit = lambda: sorted(Emoticon.get_instances(), key=lambda x: float(x.votes), reverse=True)

# idk man give me a break i'm too old for this shit
fuck_python2 = lambda x: x.decode("utf-8", "replace") if isinstance(x, bytes) else x

def find_shit(all_shit, name):
    for x in all_shit:
        if fuck_python2(x.name) == fuck_python2(name):
            return x

route('/')(view('index')(lambda: dict(emoticons=get_all_shit())))

DIRECTIONS = {
    'up': 1,
    'down': -1,
    'side': math.pi,
}

@route('/vote/<where>/<what>')
def vote(where, what):
    existing = find_shit(get_all_shit(), what)
    if existing:
        existing.votes = float(existing.votes) + DIRECTIONS.get(where, 0)
        existing.commit()
    return redirect("/")

@post('/add')
@view('index')
def add():
    all_shit = get_all_shit()
    name = request.forms.get('name')
    if find_shit(all_shit, name):
        return dict(emoticons=all_shit, message='duplicate zomg')

    # anti spam!!
    __import__('time').sleep(5)
    Emoticon(fuck_python2(name), 0).commit()
    return redirect("/")

run(host='localhost', port=8080, debug=True, reloader=True)