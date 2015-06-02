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

func main() {
    dirt := Element{"dirt"}
    world := new(LocalChunk)
    world.summary = &dirt
    fmt.Println("hello")
}
