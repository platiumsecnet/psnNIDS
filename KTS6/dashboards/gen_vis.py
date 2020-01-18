#!/usr/bin/python3

import json
import yaml
import copy
with open('table_template.json') as f:
    d = json.load(f)
with open('pie_template.json') as f:
    d1 = json.load(f)
 
with open('define_protocol.yaml', 'r') as stream:
    try:
        fp = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

json_table = d[0]
json_pie = d1[0]
new_json_list = []
for proto in fp:
    for field in fp[proto]:
        new_json = copy.deepcopy(json_table)
        if fp[proto][field] == 'table':
            new_json['_id'] = json_table['_id'] + proto + field
            new_json['_source']['title'] = proto.upper() + '-Top20' + field
            k = json.loads(d[0]['_source']['visState'])
            k['title'] = proto.upper() + '-Top20' + field
            k['aggs'][1]['params']['field'] = '{}.{}.keyword'.format(proto, field)
            #k['aggs'][1]['params']['customLabel'] = field
            new_json['_source']['visState'] = json.dumps(k)
            k = json.loads(new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON'])
            k['index'] = 'logstash-{}-*'.format(proto)
            new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON'] = json.dumps(k)
            #new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON']['index'] = 'logstash-{}-*'.format(proto)
            new_json_list.append(new_json)

        elif fp[proto][field] == 'pie':
            new_json = copy.deepcopy(json_pie)
            new_json['_id'] = json_pie['_id'] + proto + field
            new_json['_source']['title'] = proto.upper() + '-Top20' + field
            k = json.loads(d1[0]['_source']['visState'])
            k['title'] = proto.upper() + '-Top20' + field
            k['aggs'][1]['params']['field'] = '{}.{}.keyword'.format(proto, field)
            #k['aggs'][1]['params']['customLabel'] = field
            new_json['_source']['visState'] = json.dumps(k)
            k = json.loads(new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON'])
            k['index'] = 'logstash-{}-*'.format(proto)
            new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON'] = json.dumps(k)
            #new_json['_source']['kibanaSavedObjectMeta']['searchSourceJSON']['index'] = 'logstash-{}-*'.format(proto)
            new_json_list.append(new_json)


print(json.dumps(new_json_list))
        
                
