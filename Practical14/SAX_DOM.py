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
    columns = ['Namespace', 'name', 'is_a']
)
max_dom.set_index('Namespace', inplace = True)

for terms in term:
    namespace = terms.getElementsByTagName('namespace')[0].firstChild.nodeValue
    name = terms.getElementsByTagName('name')[0].firstChild.nodeValue
    is_a = len(terms.getElementsByTagName('is_a'))
    if namespace not in max_dom.index:
        max_dom.loc[namespace,'is_a'] = [is_a]
        max_dom.loc[namespace,'name'] = [name]
        # print(max)
    else:
        if max_dom.loc[namespace,'is_a'][0] < is_a:
            max_dom.loc[namespace,'is_a'] = [is_a]
            max_dom.loc[namespace,'name'] = [name]
        elif max_dom.loc[namespace, 'is_a'][0] == is_a:
            max_dom.loc[namespace,'is_a'].append(is_a)
            max_dom.loc[namespace,'name'].append(name)

end_dom = datetime.now()
difference_dom = end_dom - start_dom
print("DOM processing:")
print('[Biological process]')
for i in range(len(max_dom.loc['biological_process','is_a'])):
    print('Name:', max_dom.loc['biological_process', 'name'][i], 'is_a number',max_dom.loc['biological_process', 'is_a'][i])
print('[Molecular function]')
for i in range(len(max_dom.loc['molecular_function','is_a'])):
    print('Name:', max_dom.loc['molecular_function', 'name'][i], 'is_a number',max_dom.loc['molecular_function', 'is_a'][i])
print('[Cellular component]')
for i in range(len(max_dom.loc['cellular_component','is_a'])):
    print('Name:', max_dom.loc['cellular_component', 'name'][i], 'is_a number',max_dom.loc['cellular_component', 'is_a'][i])
print('Time of processing:', difference_dom, '\n')

start_sax = datetime.now()
parser = xml.sax.make_parser()

# dataframe to store isamax and according terms for each namespace
max_sax = pd.DataFrame(
    columns = ['Namespace', 'name', 'is_a']
)
max_sax.set_index('Namespace', inplace = True)

class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''
        self.name = ''
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
    
    def endElement(self, tag):
        # print(tag == 'term')
        if tag == 'term':
            # print(self.namespace not in max.index)
            if self.namespace not in max_sax.index:
                max_sax.loc[self.namespace,'is_a'] = [self.is_a]
                max_sax.loc[self.namespace,'name'] = [self.name]
        # print(max)
            else:
                if max_sax.loc[self.namespace,'is_a'][0] < self.is_a:
                    max_sax.loc[self.namespace,'is_a'] = [self.is_a]
                    max_sax.loc[self.namespace,'name'] = [self.name]
                    # print(max)
                elif max_sax.loc[self.namespace, 'is_a'][0] == self.is_a:
                    max_sax.loc[self.namespace,'is_a'].append(self.is_a)
                    max_sax.loc[self.namespace,'name'].append(self.name)
            self.is_a = 0
            self.namespace = ''
            self.name = ''
        self.currentdata = ''

Handler = TermHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

end_sax = datetime.now()
difference_sax = end_sax - start_sax
print("SAX processing:")
print('[Biological process]')
for i in range(len(max_sax.loc['biological_process','is_a'])):
    print('Name:', max_sax.loc['biological_process', 'name'][i], 'is_a number',max_sax.loc['biological_process', 'is_a'][i])
print('[Molecular function]')
for i in range(len(max_sax.loc['molecular_function','is_a'])):
    print('Name:', max_sax.loc['molecular_function', 'name'][i], 'is_a number',max_sax.loc['molecular_function', 'is_a'][i])
print('[Cellular component]')
for i in range(len(max_sax.loc['cellular_component','is_a'])):
    print('Name:', max_sax.loc['cellular_component', 'name'][i], 'is_a number',max_sax.loc['cellular_component', 'is_a'][i])
print('Time of processing:', difference_sax)

# SAX is quicker that DOM