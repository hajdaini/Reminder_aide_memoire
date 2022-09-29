*Kubernetes exam version 1.19*

<!-- TOC -->

- [Composants Kubernetes](#composants-kubernetes)
    - [Composants du Master](#composants-du-master)
    - [Composants du Worker](#composants-du-worker)
    - [TroubleShooting](#troubleshooting)
- [Les objets simple Kubernetes](#les-objets-simple-kubernetes)
    - [Pod](#pod)
    - [Deployment](#deployment)
        - [Rolling Updates et Rollbacks](#rolling-updates-et-rollbacks)
    - [Service](#service)
    - [namespace](#namespace)
        - [ResourceQuota](#resourcequota)
- [Stockage](#stockage)
    - [Quelques Types](#quelques-types)
        - [hostPath](#hostpath)
        - [secret](#secret)
    - [PersistentVolume et PersistentVolumeClaim](#persistentvolume-et-persistentvolumeclaim)
- [Scheduler](#scheduler)
    - [Nodename](#nodename)
    - [nodeSelector](#nodeselector)
    - [Node Affinity](#node-affinity)
    - [Taints/Tolerances](#taintstolerances)
    - [DaemonSet](#daemonset)
- [Supervision](#supervision)
- [Security](#security)
    - [Auth Mechanisms - Basic](#auth-mechanisms---basic)
    - [Les différents certificats](#les-différents-certificats)
    - [Autoriser un utilisateur à se connecter au cluster](#autoriser-un-utilisateur-à-se-connecter-au-cluster)
    - [KubeConfig](#kubeconfig)
    - [RBAC](#rbac)
        - [Role and RoleBinding](#role-and-rolebinding)
        - [ClusterRole](#clusterrole)
        - [Tester les droits](#tester-les-droits)
    - [TLS bootstrapping](#tls-bootstrapping)
    - [Registry Docker privé](#registry-docker-privé)
    - [SecurityContext (Utilisateur et autorisation dans un conteneur/pod)](#securitycontext-utilisateur-et-autorisation-dans-un-conteneurpod)
    - [Network Policy (Ingress & Egress)](#network-policy-ingress--egress)
- [Upgrade d'un cluster k8s](#upgrade-dun-cluster-k8s)
    - [Upgrade le master](#upgrade-le-master)
    - [Upgrade les workers](#upgrade-les-workers)
- [MEttre le save snapshot](#mettre-le-save-snapshot)
- [Réseau](#réseau)
    - [Fichiers de conf](#fichiers-de-conf)
    - [Ingress (loadbalancer par path)](#ingress-loadbalancer-par-path)
- [Json](#json)
- [Infos certification](#infos-certification)
    - [Commandes supplementaires](#commandes-supplementaires)
    - [Conseils](#conseils)
    - [Preparation](#preparation)
    - [CODE PROMO](#code-promo)

<!-- /TOC -->

# Composants Kubernetes

## Composants du Master

- **etcd** : stocke les informations de configuration sous forme de clé et valeurs

  ```shell
  cat /etc/kubernetes/manifests/etcd.yaml
  ps aux | grep etcd
  ```

- **kube-apiserver** : point d'entrée exposant l'API HTTP Rest de k8s

  ```shell
  cat /etc/kubernetes/manifests/kube-apiserver.yaml
  ps -aux | grep kube-apiserver
  ```

- **kube-controller-manager** : collecteurs d'informations, actions de correctives en cas de besoin

  ```shell
  cat /etc/kubernetes/manifests/kube-controller-manager.yaml
  ps -aux | grep kube-controller-manager
  ```

- **kube-scheduler** : responsable de la répartition et l'utilisation de la charge de travail sur les nœuds

  ```shell
  cat /etc/kubernetes/manifests/kube-scheduler.yaml
  ps -aux | grep kube-scheduler
  ```

## Composants du Worker

- **kubelet** : agent qui s'exécute dans chaque nœud chargé de relayer les informations au Master

  ```shell
  cat /var/lib/kubelet/config.yaml
  ps -aux | grep kubelet
  ```

- **kube-proxy** : active l'abstraction réseau du Service Kubernetes

  ```shell
  kubectl get daemonset -n kube-system
  ```

## TroubleShooting

- Vérifier la validité d'un certificat :

  ```shell
  openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
  ```

- Si problème sur un master alors vérifier l'état des pods dans le namespace `kube-system` et les logs docker :

  ```docker
  kubectl get pods -n kube-system
  docker logs <container id>
  ```

- Si problème sur un worker alors vérifier les logs kubelet

  ```shell
  journalctl -u kubelet -f
  ```

# Les objets simple Kubernetes

lien : [https://kubernetes.io/fr/docs/reference/kubectl/conventions/](https://kubernetes.io/fr/docs/reference/kubectl/conventions/)

## Pod

Groupe d'un ou plusieurs conteneurs, avec un stockage et un réseau partagé. Les conteneurs communiquent plus efficacement entre eux.

```shell
kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run -o yaml
```

## Deployment

- **ReplicaSet** : s'assure que les réplicas spécifiés sont actifs
- **Deployment** : défini l'état désiré  des pods et fournit des maj de Pods et ReplicaSets.

```shell
kubectl run --generator=deployment/v1beta1 nginx --image=nginx --dry-run --replicas=4 -o yaml
``` 

- Scaler le nombre de répliques

  ```shell
  kubectl scale deployment nginx-deployment --replicas=6
  ```

- Autoscale un Deployment

  ```shell
  kubectl autoscale deployment nginx-deployment  --min=2 --max=5
  ```

### Rolling Updates et Rollbacks

Revenir sur une version précédente de votre Deployment 

- Update

  ```shell
  kubectl run nginx --image=nginx:1.16 --replicas=1
  kubectl rollout status deployment.v1.apps/nginx
  kubectl rollout history deployment.v1.apps/nginx
  kubectl set image deployment.v1.apps/nginx nginx=nginx:1.17
  ```

- Rollback

  ```shell
  kubectl rollout undo deployment/myapp-deployment
  ```

## Service

Expose les pods en tant que service réseau, en leurs attribuant leurs propres adresses IP et un nom DNS unique

- **ClusterIP** : IP interne, le service n'est accessible que depuis l'intérieur du cluster.
- **NodePort** : expose le service vers l'extérieur du cluster à l'aide du NAT (ports 30000 à 32767).
- **LoadBalancer** : utilise le LoadBalancer des fournisseurs de cloud.
- **ExternalName** : effectue une simple redirection CNAME (ex : rediriger le trafic vers le dns "example.com").

```shell
kubectl expose deployment/pod <deployment/pod NAME>
    --name : nom du service
    --type : type du service
    --protocol : protocole à utiliser (TCP/UDP) 
    --port : port utilisé par le service 
    --target-port : port utilisé utilisé par le Pod 
    --selector='clé=valeur': le sélecteur utilisé par service 

--dry-run -o yaml
```

## namespace

Clusters virtuels sauvegardés par le même cluster physique

```shell
kubectl create namespace dev-team
kubectl delete namespaces prod-team
# modifier le namespace par défaut
kubectl config set-context --current --namespace=prod-team
kubectl config view | grep namespace
```

### ResourceQuota

Limiter la quantité de ressources dans un namespace

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: mem-cpu-quota
spec:
  hard:
    pods: "2"
    requests.cpu: "1"
    limits.cpu: "2"
    requests.memory: 1Gi
    limits.memory: 2Gi
```

```shell
kubectl apply -f quota.yaml -n=dev-team
```

# Stockage

## Quelques Types

### hostPath

Type de volume qui monte un fichier ou un répertoire du système de fichiers du nœud abritant votre pod

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - name: html
      mountPath: /usr/share/nginx/html

  volumes:
  - name: html
    hostPath: 
      path: /data
      type: DirectoryOrCreate
```

### secret

type de volume utilisé pour transmettre des informations sensibles 

```shell
echo -n '1f2d1e2e67df' > ./password.txt
kubectl create secret generic secret-password --from-file=./password.txt
secret/secret-password created
kubectl get secrets
```

## PersistentVolume et PersistentVolumeClaim

- **PersistentVolume**  élément de stockage dans le cluster
- **PersistentVolumeClaim** : revendiquer l'utilisation des ressources d'un des PV disponible

```yaml
kind: PersistentVolume
apiVersion: v1
metadata:
   name: my-pv 
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /pv-data
    type: DirectoryOrCreate
```


```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
   name: my-pvc
spec:
   accessModes:
      - ReadWriteOnce
   resources:
      requests:
        storage: 500Mi
```


```yaml
# Pod
spec:
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - name: nginx-pvc
      mountPath: "/usr/share/nginx/html"
  volumes:
  - name: nginx-pvc
    persistentVolumeClaim:
      claimName: my-pvc
```

## Sécurité Pods

## SecurityContext (Utilisateur et autorisation dans un conteneur/pod)

```yaml
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: ["sleep", "3600"]
    securityContext:
      runAsUser: 1000
      capabilities:
        add: ["SYS_TIME"]
```

## Network Policy (Ingress & Egress)

- Ingress : Connexion entrante
- Egress : Connexion sortante

![network-policies.jpg](./images/network-policies.jpg)


```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: api-pod
    ports:
    - protocol: TCP
      port: 3306
```

> CNI => flannel ne supporte pas les NetworkPolicies

# Scheduler

Contraindre ou privilégié un pod pour ne s'exécuter que sur des nœuds particuliers

## Nodename

Nom du nœud qui accueillera le pod

```yaml
apiVersion: v1
kind: pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: worker-1
```

## NodeSelector

Label du nœud sur lequel on souhaite recevoir notre pod

1. Créer un label d'un pod 

   ```shell
   # Rajouter un moins à la fin pour supprimer le label
   kubectl label node worker-1 ntype=html
   ```

2. Supprimer un label d'un pod 

   ```shell
   kubectl label node worker-1 ntype-
   ```

3. Lister les labels

   ```shell
   kubectl get nodes worker-1 --show-labels
   ```

4. Créer le pod 

   ```yaml
   # ... Pod
   spec:
     nodeSelector:
       ntype: html
   ```


## Node Affinity

Fonctionnalités avancées pour limiter le placement de pods sur des nœuds, 2 états actuels :

- **`requiredDuringSchedulingIgnoredDuringExecution`**
- **`preferredDuringSchedulingIgnoredDuringExecution`**

Détails :

- **`During Scheduling`** : état où un pod n'existe pas encore
  - **`required`** : éxige que le nœud respecte les règles d'affinité. Si non respect des alors pod non planifié.
  - **`preferred`** : si aucun nœud n'est trouvé. Le scheduler placera le pod sur n'importe quel autre nœud disponible.
- **`During Execution`** : état lorsqu'un pod est déjà exécuté, l'état est toujours à `Ignored`, donc les pods continueront à fonctionner sans aucun impact.

```yaml
# ... Pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: ntype
            operator: NotIn
            values:
            - virus
            - malware
```

## Taints/Tolerances

- **`Taints`** : Définir des restrictions sur les pods pouvant être planifiés sur un nœud
  Les types d'effet de `Taints` :
  - **`NoSchedule`** : le pod ne sera pas programmé sur le nœud marqué par un rejet.
  - **`PreferNoSchedule`** : évite de placer le pod sur le nœud marqué par un rejet, mais ne le garanti pas.
  - **`NoExecute`** : si le pod est déjà en cours d'exécution sur le nœud marqué par un rejet, il est alors expulsé.

- **`Tolerances`** : rendre un pod tolérant à node Taint


1. Mettre une Taint sur un node

   ```shell
   # Rajouter un moins à la fin pour supprimer la Taint
   kubectl taint nodes worker-1 hold=virus:NoSchedule
   kubectl describe node | grep 'Name:\|Taints:'
   ```


2. Créer un pod tolérant :

   ```yaml
   # ... Pod
   spec:
     tolerations:
     - key: "hold"
       operator: "Equal"
       value: "virus"
   ```


## DaemonSet

Garantit qu'une copie du pod est toujours présente dans tous les nœuds du cluster

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-daemonset
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```

# Supervision


Metrics Server (MC) => demande à kubelet qui récupère les métriques grâce au sous composant cAdvisor => envoie les métriques à MC => MC stocke dans la RAM


- Vérifiez l'état/logs du pod de metrics 

  ```shell
  kubectl get pods -n kube-system | grep metrics
  kubectl logs metrics-server-77dd877444-hcqrt  -n kube-system
  ```

- Supervision pods et nodes

  ```
  kubectl top nodes
  kubectl top pod
  ```

# Security

## Auth Mechanisms - Basic

Ajouter des utilisateurs depuis un fichier csv

`/tmp/users/user-details.csv` :

```textile
password123,user1,u0001
password123,user2,u0002
```

`/etc/kubernetes/manifests/kube-apiserver.yaml` : 

```yaml
spec:
  containers:
  - command:
    - kube-apiserver
    - --basic-auth-file=/tmp/users/user-details.csv
    volumeMounts:
    - mountPath: /tmp/users
      name: usr-details
      readOnly: true
  volumes:
  - hostPath:
      path: /tmp/users
      type: DirectoryOrCreate
    name: usr-details
```

## Les différents certificats

![certificats.jpg](./images/certificats.jpg)


|      Certificate Path               | CN Name | Organization |
|:------------------------------------|---------|--------------|
| /etc/kubernetes/pki/apiserver.(crt/key) | kube-apiserver |
| /etc/kubernetes/pki/ca.(crt/key) | kubernetes |
| /etc/kubernetes/pki/apiserver-kubeletclient.(crt/key) | kube-apiserver-kubelet-client | system:masters |
| /etc/kubernetes/pki/apiserver-etcd-client.(crt/key) | kube-apiserver-etcd-client | system:masters |


## Autoriser un utilisateur à se connecter au cluster

1. Récupérer ou créer le certificat du user à envoyer au serveur api :

   ```shell
   openssl genrsa -out jane.key 2048
   openssl req -new -key jane.key -subj "/CN=jane" -out jane.csr
   ```

2. Créer un CertificateSigningRequest (certificat du user en base 64) :
   - D'abord récupérer la clé en base64
   
     ```shell
     cat jane.csr | base64 -w 0
     ```
   - Créer le CertificateSigningRequest:

     ```shell
     cat <<EOF | kubectl apply -f -
     apiVersion: certificates.k8s.io/v1
     kind: CertificateSigningRequest
     metadata:
       name: jane
     spec:
       request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZVzVuWld4aE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTByczhJTHRHdTYxakx2dHhWTTJSVlRWMDNHWlJTWWw0dWluVWo4RElaWjBOCnR2MUZtRVFSd3VoaUZsOFEzcWl0Qm0wMUFSMkNJVXBGd2ZzSjZ4MXF3ckJzVkhZbGlBNVhwRVpZM3ExcGswSDQKM3Z3aGJlK1o2MVNrVHF5SVBYUUwrTWM5T1Nsbm0xb0R2N0NtSkZNMUlMRVI3QTVGZnZKOEdFRjJ6dHBoaUlFMwpub1dtdHNZb3JuT2wzc2lHQ2ZGZzR4Zmd4eW8ybmlneFNVekl1bXNnVm9PM2ttT0x1RVF6cXpkakJ3TFJXbWlECklmMXBMWnoyalVnald4UkhCM1gyWnVVV1d1T09PZnpXM01LaE8ybHEvZi9DdS8wYk83c0x0MCt3U2ZMSU91TFcKcW90blZtRmxMMytqTy82WDNDKzBERHk5aUtwbXJjVDBnWGZLemE1dHJRSURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBR05WdmVIOGR4ZzNvK21VeVRkbmFjVmQ1N24zSkExdnZEU1JWREkyQTZ1eXN3ZFp1L1BVCkkwZXpZWFV0RVNnSk1IRmQycVVNMjNuNVJsSXJ3R0xuUXFISUh5VStWWHhsdnZsRnpNOVpEWllSTmU3QlJvYXgKQVlEdUI5STZXT3FYbkFvczFqRmxNUG5NbFpqdU5kSGxpT1BjTU1oNndLaTZzZFhpVStHYTJ2RUVLY01jSVUyRgpvU2djUWdMYTk0aEpacGk3ZnNMdm1OQUxoT045UHdNMGM1dVJVejV4T0dGMUtCbWRSeEgvbUNOS2JKYjFRQm1HCkkwYitEUEdaTktXTU0xMzhIQXdoV0tkNjVoVHdYOWl4V3ZHMkh4TG1WQzg0L1BHT0tWQW9FNkpsYWFHdTlQVmkKdjlOSjVaZlZrcXdCd0hKbzZXdk9xVlA3SVFjZmg3d0drWm89Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=
       signerName: kubernetes.io/kube-apiserver-client
       expirationSeconds: 86400  # one day
       usages:
       - client auth
   EOF
   ```
3. Approuver l'utilisateur :

   ```shell
   kubectl get csr
   kubectl certificate approve jane
   ```

4. Donner à l'utilisateur le fichier ca.crt

## KubeConfig

Cette page montre comment configurer l'accès à plusieurs clusters à l'aide de fichiers de configuration

> Ici on prétend que l'utilisateur possède déjà les droits nécessaires dans le cluster

Sans KubeConfig, il faudrait utiliser les options suivantes dans la commande kubectl :

```textile
kubectl get pods
  --server my-kube-playground:6443
  --client-key admin.key
  --client-certificate admin.crt
  --certificate-authority ca.crt
```

Avec `~/.kube/config` :

```yaml
apiVersion: v1
kind: Config
preferences: {}

clusters:
- name: my-kube-playground
  cluster:
    certificate-authority: ca-crt
    # ou la clé en base64
    certificate-authority-data: Y201bGRHVnpNQjRYRFRFNU1Ea3lOVEEzTlRJME1s....
    server: https://my-kube-playground:6443

contexts:
- name: admin@my-kube-playground
  context:
    cluster: my-kube-playground
    user: admin
    # On peut surcharger le namespace par défaut
  
users:
- name: admin
  user:
    client-certificate : admin.crt
    client-key : admin.key
    # ou la clé en base64
    client-certificate-data: LS0tLS1345E
    client-key-data : LSDF345ERFSDF

current-context: admin@my-kube-playground
```

basculer entre les clusters :

```shell
kubectl config view
kubectl config set-context dev-frontend admin@my-kube-playground
```

## RBAC

Certaines ressources K8S peuvent être namespacées

```yaml
kubectl api-resources --namespaced=true
```

Les autres types sont des ressources qui sont ne pas associées à un namespace (nodes, pv, etc ...) 

### Role and RoleBinding

Ne peut accorder l'accès aux ressources namespacées (donc accorde les permissions sur 1 seul namespace max)

**Pas d'options pour --namespace pour les roles**

```shell
kubectl create role pod-reader --verb=get,list,watch --resource=pods 
```

```shell
kubectl create rolebinding user-read-binding --role=pod-reader --user=user-read --namespace=tata
```

### ClusterRole 

Peut aussi accorder des accès aux ressources non namespacées (peut être utilisé pour tous les namespaces)

```shell
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods 
```

```shell
kubectl create rolebinding user-read-binding --clusterrole=pod-reader --user=user-read --namespace=tata
```

### Tester les droits

```shell
kubectl get pod --as dev-user -n tata
yes
kubectl auth can-i create deployments --as dev-user -n tata
no
```

## TLS bootstrapping

Ajouter un nœud à notre cluster manuellement :

1. Create the token

  ```shell
  cat > bootstrap-token-09426c.yaml <<EOF
  apiVersion: v1
  kind: Secret
  metadata:
    # Name MUST be of form "bootstrap-token-<token id>"
    name: bootstrap-token-09426c
    namespace: kube-system
  
  # Type MUST be 'bootstrap.kubernetes.io/token'
  type: bootstrap.kubernetes.io/token
  stringData:
    # Human readable description. Optional.
    description: "The default bootstrap token generated by 'kubeadm init'."
  
    # Token ID and secret. Required.
    token-id: 09426c
    token-secret: x262bbbe835dx21k
  
    # Expiration. Optional.
    expiration: 2021-03-10T03:22:11Z
  
    # Allowed usages.
    usage-bootstrap-authentication: "true"
    usage-bootstrap-signing: "true"
  
    # Extra groups to authenticate the token as. Must start with "system:bootstrappers:"
    auth-extra-groups: system:bootstrappers:node03
  EOF
  
  
  kubectl create -f bootstrap-token-09426c.yaml
  ```

2. enable certificate creation

  ```shell
  kubectl create clusterrolebinding crb-to-create-csr --clusterrole=system:node-bootstrapper --group=system:bootstrappers
  ```

3. Create the kubelet config on the worker node

  ```shell
  cat <<EOF | sudo tee /tmp/bootstrap-kubeconfig
  apiVersion: v1
  clusters:
  - cluster:
      certificate-authority: /etc/kubernetes/pki/ca.crt
      server: https://172.17.0.68:6443
    name: bootstrap
  contexts:
  - context:
      cluster: bootstrap
      user: kubelet-bootstrap
    name: bootstrap
  current-context: bootstrap
  kind: Config
  preferences: {}
  users:
  - name: kubelet-bootstrap
    user:
      token: 09426c.x262bbbe835dx21k
  EOF
  ```

  ```shell
  cat > /etc/systemd/system/kubelet.service <<-EOF
  [Unit]
  Description=Kubernetes Kubelet
  Documentation=https://github.com/kubernetes/kubernetes
  
  [Service]
  ExecStart=/usr/bin/kubelet \
    --bootstrap-kubeconfig=/tmp/bootstrap-kubeconfig \
    --kubeconfig=/var/lib/kubelet/kubeconfig \
    --register-node=true \
    --v=2
  Restart=on-failure
  StandardOutput=file:/var/kubeletlog1.log
  StandardError=file:/var/kubeletlog2.log
  RestartSec=5
  
  [Install]
  WantedBy=multi-user.target
  EOF
  ```

  4. Enable auto approve

  ```shell
  kubectl create clusterrolebinding crb-to-approve-csr --clusterrole=system:certificates.k8s.io:certificatesigningrequests:nodeclient --group=system:bootstrappers
  ```

  5. Enable auto approve

  ```shell
  cat > crb-node-autorotate-csr.yaml <<EOF
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    name: crb-autorenew-csr-for-nodes
  subjects:
  - kind: Group
    name: system:nodes
    apiGroup: rbac.authorization.k8s.io
  roleRef:
    kind: ClusterRole
    name: system:certificates.k8s.io:certificatesigningrequests:selfnodeclient
    apiGroup: rbac.authorization.k8s.io
  EOF

  kubectl create -f crb-node-autorotate-csr.yaml
  ```shell


## Registry Docker privé

```shell
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: <your-private-image>
  imagePullSecrets:
  - name: regcred
```


# Upgrade d'un cluster k8s

D'abord un upgrade du master puis un upgrade des workers un par un

***Exemple*** : Upgrade version 1.11 => 1.13, on doit faire un upgrade incrémental par version mineur donc 1.11 => 1.12 => 1.13 

## Upgrade le master

1. Vérifier la version possible à upgrade :

  ```shell
  kubeadm upgrade plan
  ```

2. Upgrade de kubeadm puis de kubelet

  ```shell
  apt-get upgrade -y kubeadm=1.12.0-00
  kubeadm upgrade apply v1.12.0
  apt-get upgrade -y kubelet=1.12.0-00
  systemctl restart kubelet
  ```

3. Vérifiez la version version
  
  ```shell
  kubectl get nodes
  ```

## Upgrade les workers


1. Rendre le worker unschedulable et déplacez les pods dans un autre worker 

  ```shell
  kubectl drain node1
  ```

2. Upgrade

  ```shell
  apt-get upgrade -y kubeadm=1.12.0-00 && kubelet=1.12.0-00
  kubeadm upgrade node config --kubelet-version v1.12.0
  systemctl restart kubelet
  ```

3. Rendre le pod schedulable
  
  ```shell
  kubectl uncordon node1
  ```

# MEttre le save snapshot


# Réseau

## Fichiers de conf

- cni

  ```shell
  # Binaire
  ls /opt/cni/bin
  # Fichier de conf
  cat /etc/cni/net.d/net-script.conf
  ```

- Plage ip des pods

  ```shell
  kubectl get pods -n kube-system
  # Une fois que vous avez récupéré le pod cni 
  kubectl logs  -n kube-system <pod-name> <container-name> | grep ipalloc-range
  kubectl logs <pod-name> weave -n kube-system 
  ```

- Plage ip des services

  ```shell
  ps aux | grep ip-range
  ```

- Plage ip des nœuds :

  ```shell
  ip addr
  ```

- CoreDNS

  ```shell
  cat /etc/coredns/Corefile
  ```

- Le type de kube-proxy :

  ```shell
  kubectl logs -n kube-system kube-proxy-2dgr9 | grep 'ipvs\|userspace\|firewalld\|iptables'
  ```

> le fichier `/etc/hosts` prend le dessus sur le fichier `/etc/resolv.conf`

# Json

[https://kubernetes.io/fr/docs/reference/kubectl/cheatsheet/](https://kubernetes.io/fr/docs/reference/kubectl/cheatsheet/)

- Récupérer l'image du premier conteneur de toutes les images

  ```shell
  kubectl get pods -o jsonpath='{.items[*].spec.containers[0].image}'
  ```

- Récupérer le nom du node et la capacité cpu avec un saut à la ligne

  ```shell
  kubectl get nodes -o jsonpath='{.items[*].metadata.name}{"\n"}{.items[*].status.capacity.cpu}'
  ```
  Résultat :
  
  ```textile
  master node01
  4      4
  ```

- Les boucles

  ```shell
  kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.capacity.cpu}{"\n"}{end}'
  ```
  Résultat :
  
  ```textile
  master  4
  node01  4
  ```
  
- Trier les PVs en ordre croissant seulon leur capacité de stockage et n'afficher que le nom et la capacité de stockage sous forme de colonnes 

  ```shell
  kubectl get pv --sort-by=.spec.capacity.storage  -o=custom-columns=NAME:.metadata.name,CAPACITY:.spec.capacity.storage
  ```

  ```textile
  NAME       CAPACITY
  pv-log-4   40Mi
  pv-log-1   100Mi
  pv-log-2   200Mi
  pv-log-3   300Mi
  ```

- Obtenir le nom context du user "aws-user"

  ```shell
  kubectl config view --kubeconfig=my-kube-config -o jsonpath="{.contexts[?(@.context.user=='aws-user')].name}"
  ```


# Infos certification

## Commandes supplementaires

- Récupérer l'api url :
  ```shell
  kubectl cluster-info | grep -E 'Kubernetes master|Kubernetes control plane' | awk '/http/ {print $NF}'
  ```
- Récupérer le certificat nécessaire pour s'authentifier auprès du cluster:
  ```shell
  kubectl get secret <secret name> -o jsonpath="{['data']['ca\.crt']}" | base64 --decode'
  ```

## Conseils

- TOUJOURS vérifier sur quel cluster vous êtes car l'exam se déroule sur plusieurs clusters
- Hiérarchiser les questions car les questions sont indépendantes et n’ont pas non plus le même coefficient donc ne pas hésiter à privilégier les questions faciles qui rapportent

## Preparation

Exercice/Doc : 

- [https://github.com/dgkanatsios/CKAD-exercises](https://github.com/dgkanatsios/CKAD-exercises)
- [https://github.com/arush-sal/cka-practice-environment](https://github.com/arush-sal/cka-practice-environment)
- [https://github.com/walidshaari/Kubernetes-Certified-Administrator](https://github.com/walidshaari/Kubernetes-Certified-Administrator)


## CODE PROMO

Coupoun : DCUBEOFFER
