import feedparser
from flask import render_template, Markup
from app import app

RSS = "http://feeds.libsyn.com/53948/rss"

alaaventura = feedparser.parse(RSS)
recientes = alaaventura.get("entries")[0:12]


@app.route("/")
@app.route("/index/")
def inicio():
    
    pod_feed = alaaventura.get("feed")
    pod_resumen = pod_feed.get("summary")
    pod_resumen = Markup(pod_resumen.replace("\n", "<br>"))

    kwargs = {
        "pod_titulo":  pod_feed.get("title"),
        "pod_resumen": pod_resumen,
        "recientes": recientes,
    }

    return render_template("index.html", **kwargs)