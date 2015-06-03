package main

import "fmt"

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

func (l *LocalChunk) passToRemote(remote *string, address *Address) {
	fmt.Println("passing to remote")
}

func (l *LocalChunk) addChunk(chunk Chunk) {
	fmt.Println("adding chunk")
}

func (l *LocalChunk) compressChunk(chunk Chunk) {
    fmt.Println("compressing chunk")
}

func (l *LocalChunk) splitChunk(chunk Chunk) {
    fmt.Println("splitting chunk")
}

func (l *LocalChunk) loadChunk(chunk Chunk) Chunk {
    return &LocalChunk{}
}

func (l *LocalChunk) transferChunk(chunk Chunk) {
    fmt.Println("transfering chunk")
}

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
