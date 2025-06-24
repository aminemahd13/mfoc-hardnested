# Convert hex dump to 1K .mfd binary file for MIFARE Classic 1K cards
def create_1k_mfd_file(output_file):
    # Original MIFARE Mini (20 blocks = 320 bytes)
    blocks = [
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ]

    # Convert blocks to binary
    binary_data = b""
    for block in blocks:
        hex_data = block.replace(" ", "")
        binary_data += bytes.fromhex(hex_data)

    # Pad to 1024 bytes
    if len(binary_data) < 1024:
        padding = b"\x00" * (1024 - len(binary_data))
        binary_data += padding

    # Write to file
    with open(output_file, "wb") as f:
        f.write(binary_data)

# Create padded MFD file for 1K card
create_1k_mfd_file("mycard_1k.mfd")
