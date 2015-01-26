package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    listener, err := net.Listen("tcp", "localhost:41537")

    if err != nil {
        fmt.Println("Error Listening: ", err.Error())
        os.Exit(1)
    }

    defer listener.Close()
    fmt.Println("Listening on localhost:41537")

    for {
        conn, err := listener.Accept()
        if err != nil {
            fmt.Println("Error accepting: ", err.Error())
            os.Exit(1)
        }
        go handleRequest(conn)
    }
}

func handleRequest(conn net.Conn) {
    buf := make([]byte, 1024)
    _, err := conn.Read(buf)
    if err != nil {
        fmt.Println("Error reading: ", err.Error())
    }

    conn.Write([]byte("Message received.\n"))
    conn.Close()
}
