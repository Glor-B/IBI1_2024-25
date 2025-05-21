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
    columns = ['Namespace', 'name', 'id', 'is_a']
)
max_dom.set_index('Namespace', inplace = True)

for terms in term:
    namespace = terms.getElementsByTagName('namespace')[0].firstChild.nodeValue
    name = terms.getElementsByTagName('name')[0].firstChild.nodeValue
    id = terms.getElementsByTagName('id')[0].firstChild.nodeValue
    is_a = len(terms.getElementsByTagName('is_a'))
    if namespace not in max_dom.index:
        max_dom.loc[namespace,'is_a'] = [is_a]
        max_dom.loc[namespace,'name'] = [name]
        max_dom.loc[namespace, 'id'] = [id]
        # print(max)
    else:
        if max_dom.loc[namespace,'is_a'][0] < is_a:
            max_dom.loc[namespace,'is_a'] = [is_a]
            max_dom.loc[namespace,'name'] = [name]
            max_dom.loc[namespace,'id'] = [id]
        elif max_dom.loc[namespace, 'is_a'][0] == is_a:
            max_dom.loc[namespace,'is_a'].append(is_a)
            max_dom.loc[namespace,'name'].append(name)
            max_dom.loc[namespace,'id'].append(id)

end_dom = datetime.now()
difference_dom = end_dom - start_dom
print("DOM processing:")
print('[Biological process]')
for i in range(len(max_dom.loc['biological_process','is_a'])):
    print('Name:', max_dom.loc['biological_process', 'name'][i], 'id:', max_dom.loc['biological_process', 'id'][i], 'is_a number:',max_dom.loc['biological_process', 'is_a'][i])
print('[Molecular function]')
for i in range(len(max_dom.loc['molecular_function','is_a'])):
    print('Name:', max_dom.loc['molecular_function', 'name'][i], 'id:', max_dom.loc['molecular_function', 'id'][i], 'is_a number:',max_dom.loc['molecular_function', 'is_a'][i])
print('[Cellular component]')
for i in range(len(max_dom.loc['cellular_component','is_a'])):
    print('Name:', max_dom.loc['cellular_component', 'name'][i], 'id:', max_dom.loc['cellular_component', 'id'][i], 'is_a number:',max_dom.loc['cellular_component', 'is_a'][i])
print('Time of processing:', difference_dom, '\n')

start_sax = datetime.now()
parser = xml.sax.make_parser()

# dataframe to store isamax and according terms for each namespace
max_sax = pd.DataFrame(
    columns = ['Namespace', 'name', 'id', 'is_a']
)
max_sax.set_index('Namespace', inplace = True)

class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''
        self.name = ''
        self.id = ''
        self.is_a = 0
    
    def startElement(self, tag, attributes):
        self.currentdata = tag
        
    def characters(self, content):
        if self.currentdata == 'namespace':
            self.namespace += content
            #print(self.namespace)
        elif self.currentdata == 'name':
            self.name += content
        elif self.currentdata == 'is_a':
            self.is_a += 1
        elif self.currentdata == 'id':
            self.id += content
    
    def endElement(self, tag):
        # print(tag == 'term')
        if tag == 'term':
            # print(self.namespace not in max.index)
            if self.namespace not in max_sax.index:
                max_sax.loc[self.namespace,'is_a'] = [self.is_a]
                max_sax.loc[self.namespace,'name'] = [self.name]
                max_sax.loc[self.namespace, 'id'] = [self.id]
        # print(max)
            else:
                if max_sax.loc[self.namespace,'is_a'][0] < self.is_a:
                    max_sax.loc[self.namespace,'is_a'] = [self.is_a]
                    max_sax.loc[self.namespace,'name'] = [self.name]
                    max_sax.loc[self.namespace, 'id'] = [self.id]
                    # print(max)
                elif max_sax.loc[self.namespace, 'is_a'][0] == self.is_a:
                    max_sax.loc[self.namespace,'is_a'].append(self.is_a)
                    max_sax.loc[self.namespace,'name'].append(self.name)
                    max_sax.loc[self.namespace, 'id'].append(self.id)
            self.is_a = 0
            self.namespace = ''
            self.name = ''
            self.id = ''
        self.currentdata = ''

Handler = TermHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

end_sax = datetime.now()
difference_sax = end_sax - start_sax

print("SAX processing:")
print('[Biological process]')
for i in range(len(max_sax.loc['biological_process', 'is_a'])):
    print('Name:', max_sax.loc['biological_process', 'name'][i], 'id:', max_sax.loc['biological_process', 'id'][i], 'is_a number:', max_sax.loc['biological_process', 'is_a'][i])
print('[Molecular function]')
for i in range(len(max_sax.loc['molecular_function','is_a'])):
    print('Name:', max_sax.loc['molecular_function', 'name'][i], 'id:', max_sax.loc['molecular_function', 'id'][i], 'is_a number:', max_sax.loc['molecular_function', 'is_a'][i])
print('[Cellular component]')
for i in range(len(max_sax.loc['cellular_component','is_a'])):
    print('Name:', max_sax.loc['cellular_component', 'name'][i], 'id:', max_sax.loc['cellular_component', 'id'][i], 'is_a number:', max_sax.loc['cellular_component', 'is_a'][i])
print('Time of processing:', difference_sax)

# SAX is quicker that DOM