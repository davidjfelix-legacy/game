package main

import "fmt"

type Chunk interface {
	addChunk(chunk *Chunk)
	tick()
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

func (l *LocalChunk) passToRemote(remote *string, address *Address) {
	fmt.Println("passing to remote")
}

func (l *LocalChunk) addChunk(chunk *Chunk) {
	fmt.Println("adding chunk")
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
