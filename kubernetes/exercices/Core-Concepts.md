# Core Concepts

### Create a namespace called 'mynamespace' and a pod with image nginx called nginx on this namespace

Documentation link used : [https://kubernetes.io/docs/reference/kubectl/conventions/](https://kubernetes.io/docs/reference/kubectl/conventions/)

- **Without yaml**

  ```shell
  kubectl create namespace mynamespace
  kubectl run --generator=run-pod/v1 nginx --image=nginx --namespace=mynamespace
  ```

- **With yaml**

  ```shell
  kubectl run --generator=run-pod/v1 nginx --image=nginx --namespace=mynamespace   --dry-run -o yaml > pod.yaml
  ```


### Create a busybox pod (using kubectl command) that runs the command "env". Run it and see the output

- **Without yaml**

  ```shell
  kubectl run --generator=run-pod/v1 busybox  --image=busybox --restart=Never -- env
  kubectl logs busybox
  ```

- **With yaml**


  ```shell
  kubectl run --generator=run-pod/v1 busybox  --image=busybox --dry-run -o yaml >   pod.yaml
  ```

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    labels:
      run: busybox
    name: busybox
  spec:
    containers:
    - image: busybox
      name: busybox
      command: ["env"]
  ```

  ```shell
  kubectl create -f pod.yaml
  kubectl logs busybox
  ```

### Get the YAML for a new ResourceQuota called 'myrq' with hard limits of 1 CPU, 1G memory and 2 pods without creating it

Command that helped me to found the command :

```shell
kubectl create --help
# and see the Available Commands
kubectl create quota --help
# and see the example
```

Solution :

```shell
kubectl create quota myrq --hard=count/pods=2,cpu=1,memory=1G --dry-run -o yaml
```

### Create a pod with image nginx called nginx and allow traffic on port 80

```shell
kubectl run --generator=run-pod/v1 nginx --image=nginx --expose=true --port='80'
```

### Change pod's image to nginx:1.7.1

```shell
kubectl set image pod nginx nginx=nginx nginx=nginx:1.7.1
kubectl describe pods nginx | grep image
```

### Get nginx pod's ip created in previous step, use a temp busybox image to wget its '/'

```shell
kubectl get pods nginx -o wide
kubectl run --generator=run-pod/v1 busybox  --image=busybox --restart=Never -- wget http://10.44.0.1
kubectl logs busybox
```

### Execute a simple shell on the nginx pod

```shell
kubectl exec -ti nginx -- /bin/sh
```

### Create a busybox pod that echoes 'hello world' and then exits and have the pod deleted automatically when it's completed

```shell
kubectl run busybox --image=busybox -it --rm=true --restart=Never -- echo 'hello world'
```

### Create an nginx pod and set an env value as 'var1=val1'. Check the env value existence within the pod

```shell
kubectl run --generator=run-pod/v1 nginx --image=nginx --env="var1=val1"
kubectl exec -ti nginx -- env | grep var1
```
