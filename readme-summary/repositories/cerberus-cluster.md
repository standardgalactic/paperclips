# cerberus-cluster

Summary:

The cerberus-cluster repository addresses a specific issue encountered when terminating a node running NFS due to hardware failure. The problem arises because the site.yml playbook fails and the sudo umount /nfs/scratch command hangs. 

Solution:
1. Modify the ansible inventory file (/etc/ansible/hosts) on the controller with elevated privileges (sudo).
   a. Update the [nfs] group hostname to point to another node in the cluster that will serve as the NFS server.
   Example entry: <instance name> ansible_user=opc role=nfs
   b. If the failed node still appears in the [compute_configured] group, remove it from this list.
2. Execute the fix_nfs.sh script to resolve the hanging umount issue.

KEYWORDS:
cerberus-cluster, NFS, Ansible, inventory file, playbook failure, hardware failure, compute configured, fix_nfs.sh, cluster management, automation tools.
