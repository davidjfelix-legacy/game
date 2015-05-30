package main

import "fmt"

type Element struct {
    name string
}

type Entity interface {
    tick()
}

type PlayerEntity struct {
    contents Chunk
    velocity Vec3f64
    location Vec3f64
    rotation Vec3f64
}

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

type empty struct {}


func main() {
    dirt := Element{"dirt"}
    world := new(LocalChunk)
    world.summary = &dirt
    fmt.Println("hello")
}
