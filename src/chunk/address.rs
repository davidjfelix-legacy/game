enum AddressBlock {
    U8(u8),
    U16(u16),
    U32(u32),
    U64(u64),
}

struct Address {
    x: AddressBlock,
    y: AddressBlock,
    z: AddressBlock,
    depth: u8,
}
