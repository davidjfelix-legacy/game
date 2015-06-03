package main

type Chunk interface {
	addChunk(chunk Chunk)
	compressChunk(chunk Chunk)
	splitChunk(chunk Chunk)
	tick()
}
