import xml.dom.minidom
import pandas as pd
from datetime import datetime, timedelta
import xml.sax
start_dom = datetime.now()
DOMTree = xml.dom.minidom.parse('go_obo.xml')

# get the only one root
collection = DOMTree.documentElement
# get all the 'terms' elements
term = collection.getElementsByTagName('term')

# dataframe to store isamax and according terms for each namespace
max_dom = pd.DataFrame(
    columns = ['Namespace', 'id', 'is_a']
)
max_dom.set_index('Namespace', inplace = True)

for terms in term:
    namespace = terms.getElementsByTagName('namespace')[0].firstChild.nodeValue
    id = terms.getElementsByTagName('id')[0].firstChild.nodeValue
    """ defs = terms.getElementsByTagName('def')
    defstr = defs.getElementsByTagName('defstr') """
    is_a = len(terms.getElementsByTagName('is_a'))
    # print(type(is_a))
    # print(namespace, id, is_a)
    # print(max.loc[max['Namespace'] == namespace,'is_a'].iloc[0])
    # print(max.loc[max['Namespace'] == namespace,'is_a'].iloc[0] < is_a)
    if namespace not in max_dom.index:
        max_dom.loc[namespace,'is_a'] = is_a
        max_dom.loc[namespace,'id'] = id
        # print(max)
    else:
        if max_dom.loc[namespace,'is_a']< is_a:
            max_dom.loc[namespace,'is_a'] = is_a
            max_dom.loc[namespace,'id'] = id

end_dom = datetime.now()
difference_dom = end_dom - start_dom
print("DOM processing:")
print('[Biological process] GO id:', max_dom.loc['biological_process', 'id'], 'is_a number:', max_dom.loc['biological_process', 'is_a'])
print('[Molecular function] GO id:', max_dom.loc['molecular_function', 'id'], 'is_a number:', max_dom.loc['molecular_function', 'is_a'])
print('[Cellular component] GO id:', max_dom.loc['cellular_component', 'id'], 'is_a number:', max_dom.loc['cellular_component', 'is_a'])
print('Time of processing:', difference_dom)

start_sax = datetime.now()
parser = xml.sax.make_parser()
#parser.setFeature(xml.sax.handlerfeature_namespace,0)

# dataframe to store isamax and according terms for each namespace
max_sax = pd.DataFrame(
    columns = ['Namespace', 'id', 'is_a']
)
max_sax.set_index('Namespace', inplace = True)

class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''
        self.id = ''
        self.is_a = 0
    
    def startElement(self, tag, attributes):
        self.currentdata = tag
        
    def characters(self, content):
        if self.currentdata == 'namespace':
            self.namespace += content
            #print(self.namespace)
        elif self.currentdata == 'id':
            self.id = content
        elif self.currentdata == 'is_a':
            self.is_a += 1
    
    def endElement(self, tag):
        # print(tag == 'term')
        if tag == 'term':
            # print(self.namespace not in max.index)
            if self.namespace not in max_sax.index:
                max_sax.loc[self.namespace,'is_a'] = self.is_a
                max_sax.loc[self.namespace,'id'] = self.id
        # print(max)
            else:
                if max_sax.loc[self.namespace,'is_a'] < self.is_a:
                    max_sax.loc[self.namespace,'is_a'] = self.is_a
                    max_sax.loc[self.namespace,'id'] = self.id
                    # print(max)
            self.is_a = 0
            self.namespace = ''
        self.currentdata = ''

Handler = TermHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

end_sax = datetime.now()
difference_sax = end_sax - start_sax
print("SAX processing:")
print('[Biological process] GO id:', max_sax.loc['biological_process', 'id'], 'is_a number:', max_sax.loc['biological_process', 'is_a'])
print('[Molecular function] GO id:', max_sax.loc['molecular_function', 'id'], 'is_a number:', max_sax.loc['molecular_function', 'is_a'])
print('[Cellular component] GO id:', max_sax.loc['cellular_component', 'id'], 'is_a number:', max_sax.loc['cellular_component', 'is_a'])
print('Time of processing:', difference_sax)