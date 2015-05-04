package main

import "fmt"

type Element struct {
    name string
}

type Vec3f64 struct {
    x float64
    y float64
    z float64
}

type Address struct {
    x uint64
    y uint64
    z uint64
    depth uint8
}

type Chunk struct {
    address Address
    center Vec3f64
    children [8]*Chunk
    child_number uint8
    //entities vec
    mass float64
    parent *Chunk
    scale uint8
    structure uint64
    summary *Element
}

func main() {
    dirt := Element{"dirt"}
    world := new(Chunk)
    world.summary = &dirt
    fmt.Println("hello")
}
