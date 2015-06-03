package main

import "fmt"

type RemoteChunk struct {
	Chunk
	addr string
}

func (r *RemoteChunk) addChunk(chunk Chunk) {
	fmt.Println("adding chunk")
}

func (r *RemoteChunk) compressChunk(chunk Chunk) {
    fmt.Println("compressing chunk")
}

func (r *RemoteChunk) splitChunk(chunk Chunk) {
    fmt.Println("splitting chunk")
}

func (r *RemoteChunk) tick() {
	fmt.Println("ticking")
}
