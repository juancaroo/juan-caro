
vlan_switch = {
    "SW1": {"VLANs": [10, 20, 30], "Native_VLAN": 99},
    "SW2": {"VLANs": [40, 50, 60], "Native_VLAN": 200}
}

print("Asociaciones VLAN-Switch:")
for switch, info in vlan_switch.items():
    print("- Switch:", switch)
    print("  VLANs:", info["VLANs"])
    print("  Native VLAN:", info["Native_VLAN"])
    print()

