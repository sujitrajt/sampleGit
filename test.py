import redis

myHostname = "<Your Host Name>"
myPassword = "<Your Access Key>"
r = redis.StrictRedis(host='sujitrajt.redis.cache.windows.net',port=6380,db=0,password='LnLBk8s3p97NyQFDt3kjTLeKY95PfTaxYAzCaCzU6iE=',ssl=True)


result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.get("Message")
print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])