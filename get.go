package main

import (
	"fmt"
	"net/http"
    "bytes"
    "io/ioutil"
)

func main() {
    url := "http://localhost:5000/api/paths"
    fmt.Println("URL:>", url)

    var jsonStr = []byte(`shall we go?`)
    req, err := http.NewRequest("GET", url, bytes.NewBuffer(jsonStr))
    req.Header.Set("X-Custom-Header", "myvalue")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("response Status:", resp.Status)
    fmt.Println("response Headers:", resp.Header)
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))
}