# kubernetes-client

Welcome in this Git repository.

Work is in progress but the aim of this repo is to find several samples for accessing and interacting with a Kubernetes cluster through several SDK, different languages.

Do you know you can connect and interactif with a cluster thanks to a Service Account(SA)?

```
export CLUSTER_IP=<your-cluster>
export TOKEN=$(kubectl get secret $(kubectl get sa  ${TEAM_SA} -n ${NAMESPACE_SA} -o yaml -ojsonpath='{.secrets[].name}') -n ${NAMESPACE_SA} -o jsonpath='{.data.token}' | base64 -D)

kubectl --insecure-skip-tls-verify=true --server=https://${CLUSTER_IP}:443 --token=${TOKEN}  get ns
```

In this repository you can do the same things for multiple programming languages.