#!/usr/bin/python3

import sys,json,yaml;
import objectpath;
import glob
from termcolor import colored

file_path=sys.argv[1]
#print(file_path)

with open("define_protocols.yaml", 'r') as stream:
    try:
        fp = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
    i = 1
    for protocol in fp:
        found_proto = False
        fields = dict(fp[protocol])
        #print(fields)
        #print("file_path: " + file_path)
        for filename in glob.glob(file_path):            
            #print(file_path)
            #print("file_name: " + filename)
            with open(filename) as f:
                for line in f:
                    j_content = json.loads(line)
                    if protocol == j_content["event_type"]:
                        found_proto = True
                        #print("Found protocol " + j_content["event_type"])
                        proto_tree = objectpath.Tree(j_content[protocol])
                        for field in fp[protocol]:
                            keyword = '$..' + field
                            result_tuple = tuple(proto_tree.execute(keyword))
                            #print("Found " + protocol + "_" + field + ": ")
                            #print(result_tuple)
                            if len(result_tuple) > 0:
                                fields.pop(field, None)
                            #if field in j_content:
                            #    print("Found " + protocol + "_" + field)
                            #else:
                            #    print("Not found " + protocol + "_" + field)
        if found_proto == False:
            print(colored('FAILED ', 'red'), colored(protocol, 'red'))
        else:
            if len(fields) > 0:
                for field in fields:
                    print(colored("FAILED ", "red"), colored(protocol, 'red'), colored(". Not found field ", 'red'), colored(field, 'red'))
            else:
                print(colored("PASSED ", "green"), colored(protocol, 'green'))
    
