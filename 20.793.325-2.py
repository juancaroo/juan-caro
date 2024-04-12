
def compararS_vlans(switch, vlans_esperadas, native_vlan_esperada):
    info = vlan_switch[switch]
    vlans_switch = set(info["VLANs"])
    native_vlan_switch = info["Native_VLAN"]

    if vlans_switch == vlans_esperadas and native_vlan_switch == native_vlan_esperada:
        return "Las VLANs y la VLAN nativa son iguales y cumplen con el requerimiento."
    else:
        return "Las VLANs o la VLAN nativa son diferentes y no cumplen con el requerimiento."

vlan_switch = {
    "SW1": {"VLANs": [10, 20, 30], "Native_VLAN": 99},
    "SW2": {"VLANs": [40, 50, 60], "Native_VLAN": 200}
}

for switch, info in vlan_switch.items():
    print(f"- Switch: {switch}")
    print(f"  VLANs: {info['VLANs']}")
    print(f"  Native VLAN: {info['Native_VLAN']}")
    print(comparar_vlans(switch, {10, 100, 30} if switch == "SW1" else {40, 50, 60}, 99 if switch == "SW1" else 200))
    print()




