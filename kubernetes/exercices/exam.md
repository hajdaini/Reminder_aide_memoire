### Test 1

1. Create a deployment named nginx-deployment of three pods running image nginx with a memory limit of 200MB.
2. Expose this deployment under the name nginx-service inside our cluster on port 4444, so point the service port 4444 to pod ports 80.
3. Spin up a temporary pod named pod1 of image hajdaini/alpine, and request the default nginx page on port 4444 of our nginx-service using curl.
4. Spin up a temporary pod named pod2 of image hajdaini/alpine in namespace test1, and request the default nginx page on port 4444 of our nginx-service .

```shell
kubectl run --generator=deployment/v1beta1 nginx-deployment --image=nginx --replicas 3 --limits='memory=200Mi'
kubectl expose deployment nginx-deployment --type=ClusterIP --name=nginx-service --port=4444 --target-port=80

## HTTP code 200
kubectl run --generator=run-pod/v1 pod1 --image=hajdaini/alpine:curl -ti --rm --  http://nginx-service:4444

# HTTP code 404 because different namespace
kubectl create namespace test1
kubectl run --generator=run-pod/v1 pod2 --namespace=test1 --image=hajdaini/alpine:curl -ti --rm --  http://nginx-service:4444
```
