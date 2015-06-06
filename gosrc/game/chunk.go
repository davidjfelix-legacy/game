package main

type Chunk interface {
	addChunk(chunk Chunk)
	compressChunk(chunk Chunk)
	removeChunk(chunk Chunk)
	splitChunk(chunk Chunk)
	tick()
}
