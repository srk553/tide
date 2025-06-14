root@Ansible:/Docker-images# cat lab15.yaml
- name: Verify BGP neighbors before pushing changes
  hosts: csr1
  gather_facts: no

  tasks:
    - name: Get BGP summary
      ios_command:
        commands:
          - show ip bgp summary
      register: bgp_output

    - name: Debug BGP summary output
      debug:
        var: bgp_output.stdout[0]

    - name: Assert neighbor is established
      assert:
        that:
          - "'10.1.1.2' in bgp_output.stdout[0]"
          - "'Estab' in bgp_output.stdout[0] or 'Established' in bgp_output.stdout[0]"
        fail_msg: "BGP neighbor 10.1.1.2 is not in an Established state!"
root@Ansible:/Docker-images#
