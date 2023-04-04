import struct


def main(binary_data):
    result = {"A1": struct.unpack(">i", binary_data[4:8])[0],
              "A2": struct.unpack(">B", binary_data[8:9])[0],
              "A3": [],
              "A4": struct.unpack(">b", binary_data[17:18])[0],
              "A5": struct.unpack(">q", binary_data[18:26])[0],
              "A6": {"C1": "", "C2": {"D1": []}}
              }

    a3_size = struct.unpack(">I", binary_data[9:13])[0]
    a3_address = struct.unpack(">I", binary_data[13:17])[0]
    for i in range(0, a3_size):
        result["A3"].append({
            "B1": struct.unpack(">B",
                                binary_data[a3_address:a3_address + 1])[0],
            "B2": struct.unpack(">B",
                                binary_data[a3_address + 1:a3_address + 2])[0],
            "B3": struct.unpack(">b",
                                binary_data[a3_address + 2:a3_address + 3])[0]
        })
        a3_address += 3

    c1_size = struct.unpack(">I", binary_data[26:30])[0]
    c1_address = struct.unpack(">H", binary_data[30:32])[0]
    for i in range(0, c1_size):
        result["A6"]["C1"] += \
            str(struct.unpack(">c",
                              binary_data[c1_address:c1_address + 1])[0])[2:3]
        c1_address += 1

    c2_size = struct.unpack(">I", binary_data[32:36])[0]
    c2_address = struct.unpack(">H", binary_data[36:38])[0]
    for i in range(0, c2_size):
        result["A6"]["C2"]["D1"].append(
            struct.unpack(">f", binary_data[c2_address:c2_address + 4])[0])
        c2_address += 4

    result["A6"]["C2"]["D2"] = struct.unpack(">f", binary_data[38:42])[0]
    result["A6"]["C2"]["D3"] = struct.unpack(">q", binary_data[42:50])[0]
    result["A6"]["C2"]["D4"] = struct.unpack(">f", binary_data[50:54])[0]

    result["A6"]["C3"] = struct.unpack(">I", binary_data[54:58])[0]
    result["A6"]["C4"] = struct.unpack(">q", binary_data[58:66])[0]

    result["A6"]["C5"] = []
    result["A6"]["C5"].append(struct.unpack(">d", binary_data[66:74])[0])
    result["A6"]["C5"].append(struct.unpack(">d", binary_data[74:82])[0])

    result["A6"]["C6"] = {"E1": []}
    c6_address = struct.unpack(">I", binary_data[82:86])[0]
    for i in range(0, 6):
        result["A6"]["C6"]["E1"].append(
            struct.unpack(">H",
                          binary_data[c6_address:c6_address + 2])[0])
        c6_address += 2
    result["A6"]["C6"]["E2"] = \
        struct.unpack(">B", binary_data[c6_address:c6_address + 1])[0]
    result["A6"]["C7"] = struct.unpack(">B", binary_data[86:87])[0]
    result["A6"]["C8"] = struct.unpack(">b", binary_data[87:88])[0]

    return result
