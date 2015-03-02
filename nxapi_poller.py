__author__ = 'sdonkena'
"""
 NX-API-BOT
"""
import requests
import json
import sys

"""
Modify these please
"""
switchuser='admin'
switchpassword='Cisc0123'
url='http://10.105.237.102//ins'
payload={
		"ins_api": {
				"version": "1.2",
				"type": "cli_show",
				"chunk": "0",
				"sid": "1",
				"input": "sh cdp neighbors detail",
				"output_format": "json"
		}
}


#first run the command, keep getting all the mgmt ip interfaces.
ip = "10.105.237.102"
d = [] 
e = {} 
i = 0
print "===============================Device"+str(i)+"======================="

def run_command_on_switch(ip, i):
    i=i+1
    if (ip != 0):
        url = "http://"+ip+"//ins"
        print url
    else:
        return 
    myheaders={'content-type':'application/json'}
    response = requests.post(url,json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    #response = json.loads(requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)))
		#iterate through the JSON output.. and form the global data structure.
    print "result:"
    obj=response["ins_api"]["outputs"]["output"]["body"]["TABLE_cdp_neighbor_detail_info"]["ROW_cdp_neighbor_detail_info"]
    length = len(obj)
    print "length is "
    print length
    print "===============================Device"+str(i)+"======================="
    for a in obj:
        #mgmt_ip=a[0]
        if 'v4mgmtaddr' in a: 
            mgmt_ip=a['v4mgmtaddr']
            d.append(mgmt_ip)
            e[mgmt_ip]=mgmt_ip
        else: 
            mgmt_ip=0
        if 'platform_id' in a:
            print a['platform_id']
        if 'port_id' in a:
            print a['port_id']
        if 'sysname' in a:
            print a['sysname']
        #platform = a['platform_id']
        #plat = platform.encode('utf-8') 

        #if (plat.find("N7K")):
        if (mgmt_ip != "10.105.237.9"):
           if (d.index(mgmt_ip) != 0): 
              sys.exit("exiting") 
           for a in d:
              if (str(a) == str(mgmt_ip)):
                 break 
              if (e.ContainsKey(mgmt_ip)):
									break
              else:
                 run_command_on_switch(mgmt_ip, i)

response = run_command_on_switch(ip, i)