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

type LocalChunk struct {
    Chunk
    address Address
    center Vec3f64
    children [8]Chunk
    child_number uint8
    entities []Entity
    mass float64
    parent Chunk
    scale uint8
    structure uint64
    summary *Element
}

func (l *LocalChunk) addChunk(chunk *Chunk) {
    fmt.Println("adding chunk")
}

type empty struct {}

func (l *LocalChunk) tick() {
    sem := make(chan empty, len(l.children) + len(l.entities))
    for _, c := range l.children {
        go func (c Chunk) {
            c.tick();
        }(c);
    }
    for _, e := range l.entities {
        go func (e Entity) {
            e.tick();
        }(e);
    }
    for i := 0; i < (len(l.children) + len(l.entities)); i++ {
        <- sem
    }

}

type RemoteChunk struct {
    Chunk
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
