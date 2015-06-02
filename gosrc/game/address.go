package main

type Address struct {
    x uint64
    y uint64
    z uint64
    depth uint8
}

func (a *Address) getTreeCoords() []uint8 {
    coords := []uint8{}
    var coord uint8
    for  i := uint8(0); i < a.depth; i++ {
        coord = 0 
        coords = append(coords, coord) 
    }
    return coords
}
