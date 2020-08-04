from rdflib import Graph, plugin
from rdflib.serializer import Serializer

import rdflib

g = rdflib.Graph()
g.parse("event-covid-19-v0.2.json", format="json-ld")
buffer = g.serialize()
with open('./event-covid-19-v0.2.owl', 'wb') as f:
    f.write(buffer)