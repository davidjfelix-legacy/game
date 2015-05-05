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

type Chunk interface {
    addChunk(chunk *Chunk)
    tick()
}

type Entity struct {
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

type LocalChunk struct {
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

func (l *LocalChunk) addChunk(chunk *Chunk) {
    fmt.Println("adding chunk")
}

func (l *LocalChunk) tick() {
    fmt.Println("ticking")
}

type RemoteChunk struct {
    addr string
}

func (r *RemoteChunk) addChunk(chunk *Chunk) {
    fmt.Println("adding chunk")
}

func (r *RemoteChunk) tick() {
    fmt.Println("ticking")
}

func main() {
    dirt := Element{"dirt"}
    world := new(LocalChunk)
    world.summary = &dirt
    fmt.Println("hello")
}
