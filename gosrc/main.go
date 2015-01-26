package main

import "fmt"
import "time"

func main() {
    go func() {
        time.Sleep(10 * time.Second)
        fmt.Println("First")
    }()

    go func() {
        time.Sleep(4 * time.Second)
        fmt.Println("Second")
    }()

    go func() {
        time.Sleep(8 * time.Second)
        fmt.Println("Third")
    }()

    go func() {
        time.Sleep(3 * time.Second)
        fmt.Println("Fourth")
    }()

    go func() {
        time.Sleep(1 * time.Second)
        fmt.Println("Fifth")
    }()

    // Eternal Slumber
    fmt.Println("Main")
    time.Sleep(20 * time.Second)
    fmt.Println("Yawn")
}
