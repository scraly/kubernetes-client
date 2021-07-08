import os
from kubernetes import client

# TOKEN
## You can use a Service Account (SA) token and generate a token in order to access to your cluster with necessary rights
# $ export SECRET_NAME_SA =`kubectl get sa ${TEAM_SA} - n $NAMESPACE_SA - ojsonpath = "{ .secrets[0].name }"`
# $ export TOKEN_SA =`kubectl get secret $SECRET_NAME_SA - n test-ns - ojsonpath = '{.data.token}' | base64 - d`
token = "<my-token>"

# KUBE
configuration = client.Configuration()
configuration.api_key["authorization"] = token
configuration.api_key_prefix['authorization'] = 'Bearer'
## you can execute kubectl cluster-info in order to know your Kubernetes cluster endpoint
configuration.host = 'https://my-cluster.my-region.toto.io:443'
configuration.ssl_ca_cert = 'k8s/aks/ca.crt'

# Kubernetes client connection
v1 = client.CoreV1Api(client.ApiClient(configuration))

# Display the list of Pods for all namespaces
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
